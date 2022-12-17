import string
import secrets

alphabet = string.ascii_letters + string.digits + string.punctuation
SECRET_KEY = ''.join(secrets.choice(alphabet) for i in range(50))
print(SECRET_KEY)
