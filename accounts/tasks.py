import ghasedak
from kavenegar import *


def sendMessage(phone, code):
    text = f"""«سامانه یادبود مجازی»
    رمزعبور شما:
    {code}""".encode('utf-8')
    sms = ghasedak.Ghasedak("7feb891becf5111c6bcfe2b1760390a9b7201a950e45e91ec79030862b7b6302")
    response = sms.send({'message': text, 'receptor': phone, 'linenumber': '10008566'})
    print('+' * 10, 'New Code', '+' * 10)
    print(code, phone)
    print(response)
    print('+' * 10, 'New Code', '+' * 10)
    if response:
        return code
    else:
        return response


def sendMessage1(phone, code):
    api = KavenegarAPI('706D423758354D2B485652432B436C324F34412B454D59493549686234414534413157777178726D30486F3D')
    text = f"""«سامانه یادبود مجازی»
    رمزعبور شما:
    {code}""".encode('utf-8')
    params = {'sender': '1000596446', 'receptor': phone, 'message': text}
    response = api.sms_send(params)
    print('+' * 10, 'New Code', '+' * 10)
    print(code, phone)
    print(response)
    print('+' * 10, 'New Code', '+' * 10)
    if response[0]['messageid']:
        return code
    else:
        return False
