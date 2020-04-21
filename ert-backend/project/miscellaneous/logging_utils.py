from config.settings.base import info_logger, error_logger


def print_debug(*args):
    # dt = datetime.now().strftime("[%d/%b/%Y %H:%M:%S]")
    # print(dt + " DEBUG ", args)
    s = ""
    for item in args:
        if item is not None:
            s += str(item)
            s += " "
    s += "\n"
    info_logger.info(s)
    # dt = datetime.now().strftime("[%d/%b/%Y %H:%M:%S]")
    # _print_in_logfile(dt + " DEBUG " + s)


def print_error(*args):
    # dt = datetime.now().strftime("[%d/%b/%Y %H:%M:%S]")
    # print(dt + " ERROR ", args)
    s = ""
    for item in args:
        if item is not None:
            s += str(item)
            s += " "
    s += "\n"
    error_logger.error(s)
    # _print_in_logfile(dt + " ERROR " + s)


def show_error(e=None, extra_str=None):
    try:
        import os, sys

        if e is not None:
            #  print_error(e)
            error_logger.exception(e)

        if extra_str is not None:
            info_logger.error("custom extra info: " + extra_str)
            # print_debug(extra_str)

        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        m_str = str(exc_type) + " " + str(fname ) + " " + str(exc_tb.tb_lineno)
        # print_error(m_str)
        info_logger.error(m_str)

        # _print_in_logfile(m_str)
    except Exception as e:
        print(e)
