import json
import requests
from config.settings.base import get_secret
from miscellaneous.logging_utils import show_error


email_sender = {
    'default': 'tech@ert.com',
    'tech': 'tech@ert.com',
    'account': ''
}

# LMD_TEAM = ['9922919009', '8669990017']
LMD_TEAM = [] #for staging
TECH_SUPPORT_TEAM = []


def get_order_place_msg_for_member(quantity, order_id):
    msg = 'Thanks for ordering with ERT'
    return msg


def get_order_place_msg_for_lmd(member_name, quantity, order_id, member_asset_address, amount, member_number,
                                order_date, partner_name):

    msg = 'NEW ORDER ALERT!!!' + "\n" + "OrderID: " + order_id + "\n" + "Partner: " + partner_name + "\n" + 'Quantity: '\
          + str(quantity) + "\n" + 'Amount: ' + str(amount) + "\n" + 'Member: ' + member_name + "\n" + "Address: "\
          + member_asset_address + "\n" + "Member Mobile: " + member_number + "\n" + "Date: " + order_date

    return msg


def get_signup_msg_for_lmd(member_name, username, mobile_number, email):

    msg = 'NEW SIGNUP NOTIFICATION' + "\n" + "Member Name: " + member_name + "\n" + "Username: " + username + "\n"\
          + "Mobile Number: " + str(mobile_number) + "\n" + "Email: " + str(email)

    return msg


def get_unavailability_refuelers_msg_for_lmd(member_name, username, mobile_number, asset_address):

    msg = 'Alert Notify Me' + "\n" + "Member Name: " + member_name + "\n" + "Username: " + username + "\n"\
          + "Mobile Number: " + str(mobile_number) + "\n" + "Asset Address: " + str(asset_address)

    return msg


def send_sms(message, numbers: [], mode=1):
    try:
        if len(numbers) < 1:
            return
        url = get_secret("NODE_NOTIFICATION_URL") + "api/node/send_msg"
        datum = {
            'numbers': json.dumps(numbers),
            'message': message,
            'provider': mode
        }
        req = requests.post(url, data=datum)
        return req.status_code is 200
    except Exception as e:
        show_error(e)
        print('Msg Service Failed')
        return False


def send_email(subject, message, to_email: [], from_email):
    try:
        if len(to_email) < 1:
            return
        url = get_secret("NODE_NOTIFICATION_URL") + "api/node/send_email"
        datum = {
            'to': json.dumps(to_email),
            'message': message,
            'from_email': from_email,
            'subject': subject
        }
        req = requests.post(url, data=datum)
        return req.status_code is 200
    except Exception as e:
        show_error(e)
        print('Email Service Failed')
        return False
