from django.core.signing import Signer

signer = Signer()

def generate_email_verification_token(user):
    return signer.sign(user.pk)

def verify_email_verification_token(token):
    try:
        user_pk = signer.unsign(token)
        return user_pk
    except:
        return None
