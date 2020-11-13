from time import sleep

def sleep_and_print(secs):
    sleep(secs)
    print("task done")
    return True

def send_email(x):
    pass

# from time import sleep
# from django.core.mail import send_mail

# def sleep_and_print(secs):
#     sleep(secs)
#     print('Task ran!')
#     return True

# def send_email(to):
#     send_mail(
#         subject = 'Links of the day!',
#         message = 'Links of the day ... TODO!',
#         from_email = 'email@example.com',
#         recipient_list = [to]
#     )