from pyfcm import FCMNotification


def test_send():
    fcm_token = ""
    app_id = 'app'
    message_title = 'Test'
    message_body = 'foobar. '
    message_data = {
        "title": 'my notif',
        "message": 'my notif msg',
        "some_id": "123",
        "some_text": "extra",
    }
    send_single_fcm_message2(app_id, fcm_token, message_title, message_body, message_data)


fcm_url = "https://fcm.googleapis.com/fcm/send"


def send_single_fcm_message2(app_id, fcm_token, message_title, message_body, message_data):
    app_id = 'petrol_pump'
    fcm_server_key = ""
    try:
        push_service = FCMNotification(api_key=fcm_server_key)
        # print("sending android fcm notification")
        result = push_service.notify_single_device(registration_id=fcm_token,
                                                   data_message=message_data,
                                                   message_body=message_body,
                                                   message_title=message_title,
                                                   time_to_live=15,
                                                   click_action="OpenNotificationActivity",
                                                   low_priority=False)
        # print(result)
        # to try sending notification on iOS device
        # if ios_also:
        #     sendIOSFcmNotification(app_id, fcm_token, message_title, message_body)
    except Exception as e:
        print(e)


def send_single_fcm_message(app_id, fcm_token, message_title, message_body, ios_also=True):
    app_id = 'petrol_pump'
    fcm_server_key = ""
    try:
        push_service = FCMNotification(api_key=fcm_server_key)
        print("sending android fcm notification")
        result = push_service.notify_single_device(registration_id=fcm_token,
                                                   data_message={'title': message_title, 'message': message_body},
                                                   time_to_live=15, click_action="OpenSplashActivity",
                                                   low_priority=False)
    except Exception as e:
        print(e)
