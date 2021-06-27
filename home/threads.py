import threading
from django.conf import settings
from django.core.mail import send_mail

class Send_mail_thread(threading.Thread):

    def __init__(self, email, token):
        self.email = email
        self.token = token
        threading.Thread.__init__(self)

    def run(self):
        try:
            subject = "Link to verify the your Account"
            message = f"Hi! here's the link to activate your account http://localhost:8000/verify/{self.token}"
            email_from = settings.EMAIL_HOST_USER
            print("Email send initiated")
            send_mail(subject , message ,email_from ,[self.email])
            print("Email has been Sent")
        except Exception as e:
            print(e)