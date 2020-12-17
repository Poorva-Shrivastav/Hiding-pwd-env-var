import os

email = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASSWORD')

print(email)
print(password)