import random 
import re
import string

def validate_email(email):
    if email is None:
        return False

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

  # generate a random number for the token
def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
    

# validate_phone
def validate_phone_update(existing_phone, new_phone):
    if new_phone == "":
        new_phone = phone

    # new phone is not provided
    if new_phone is None:
        return True

    # must add new phone number
    if new_phone is not None and existing_phone is not None:
        print("ERROR : Cannot input a new phone number because one already exists")
        return False

    return False


# Email Sender function
def send_email(subject, receiver, text_body, html_body):
    sender = os.getenv("MAIL_USERNAME")
    password = os.getenv("MAIL_PASSWORD")


    if not sender or not password:
        print("email credentail missing in .env")
        return False
    msg = MIMEMultipart("alternative")
    msg ["Subject"] = subject

    
