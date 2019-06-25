# -*- coding:utf-8 -*-
__author__ = 'Leonardo'
__date__ = '2019/3/28 21:56'
from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MyMooc.settings import EMAIL_FROM


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_boby = ''

    if send_type == 'register':
        email_title = 'MyMOOC激活链接'
        email_boby = "MyMOOC的新成员您好，欢迎来到MyMOOC-超棒的在线教育平台。我们非常开心您的加入并且祝您学有所成。" \
                     "请点击此链接以确认您的邮件地址：http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_title, email_boby, EMAIL_FROM, [email])
        if send_status:
            pass

    elif send_type == 'forget':
        email_title = 'MyMOOC密码重置链接'
        email_boby = "MyMOOC的成员您好，" \
                     "请点击此链接以重置您的账号密码：http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_title, email_boby, EMAIL_FROM, [email])
        if send_status:
            pass

    elif send_type == "update_email":
        email_title = "MyMOOC邮箱修改验证码"
        email_body = "MyMOOC的成员您好，您的邮箱验证码为: {0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
