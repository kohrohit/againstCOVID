import json
import logging
import datetime

logger = logging.getLogger("project")


def log_requests_and_exceptions(func):
    """
        A function decorator to check whether to log exceptions to file based on status codes of response.
        Also, log all the incoming request body.
    """

    def wrapper(*args, **kwargs):
        request, response_obj = func(*args, **kwargs)
        try:
            logging_data_body = {
                "request_url": request._current_scheme_host + request.path,
                "request_data": response_obj.renderer_context['request'].data,
                "response_data": response_obj.data,
                "is_exception": response_obj.exception,
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "status_code": None,
                "reason_phrase": None
            }
            if response_obj.status_code not in [200, 201, 301, 302]:
                logging_data_body['status_code'] = response_obj.status_code
                logging_data_body['reason_phrase'] = response_obj.reason_phrase
            logger.debug(json.dumps(logging_data_body))
        except:
            pass
        return response_obj
    return wrapper


class MiddlewareMixin(object):
    """
        A Mixin to handle old Middleware's of Django (<=1.9)
    """

    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class ErrorLoggingMiddleWare(MiddlewareMixin):
    """
        Custom MiddleWare which will intercept each http response and if any error occurs it will log the complete error
        stack to a log file along with the Request Body
    """

    @log_requests_and_exceptions
    def process_response(self, request, response):
        return request, response
