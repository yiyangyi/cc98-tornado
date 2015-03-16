import smtplib
import email

charset            =  'utf-8'
send_mail_host     =  'smtp_host'
send_mail_user     =  'smtp_user'
send_mail_username = u'send_mail_username'
send_mail_password =  'send_mail_password'
send_mail_postfix  =  'send_mail_postfix'
get_mail_user      =  'get_mail_user'
get_mail_postfix   =  'get_mail_postfix'
get_mail_host      =  'get_mail_host'

def send(sub, content, receiver = get_mail_user + get_mail_postfix):
    send_mail_address = send_mail_username + '<' + send_mail_user + '@' + send_mail_postfix + '>'
    msg = email.mime.text.MIMEText(content, 'html', charset)
    msg["Subject"] = email.header.Header(sub, charset)
    msg["From"]    = send_mail_address
    msg["to"]      = to_address = receiver
    try:
        stp = smtplib.SMTP()
        stp.connect(send_mail_host)
        stp.login(send_mail_user, send_mail_password)
        stp.sendmail(send_mail, to_address, msg.as_string())
        stp.close()
        return True
    except Exception e:
        print(e)
        return False



