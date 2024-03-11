import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_port():
    return os.environ.get("PORT", 8080)


# def get_adyen_merchant_account():
#     adyen_merchant_account = os.environ.get("ADYEN_MERCHANT_ACCOUNT")

#     if not adyen_merchant_account:
#         raise Exception("Missing ADYEN_MERCHANT_ACCOUNT in .env")

#     return adyen_merchant_account


def get_stripe_private_key():
    stripe_private_key = os.environ.get("STRIPE_PRIVATE_KEY")

    if not stripe_private_key:
        raise Exception("Missing STRIPE_PRIVATE_KEY in .env")

    return stripe_private_key


def get_stripe_public_key():
    stripe_public_key = os.environ.get("STRIPE_PUBLIC_KEY")

    if not stripe_public_key:
        raise Exception("Missing STRIPE_PUBLIC_KEY in .env")

    return stripe_public_key


# def get_stripe_hmac_key():
#     stripe_hmac_key = os.environ.get("ADYEN_HMAC_KEY")

#     if not stripe_hmac_key:
#         raise Exception("Missing ADYEN_HMAC_KEY in .env")

#     return stripe_hmac_key


# def get_supported_integration():
#     return ['dropin', 'card', 'ideal', 'klarna', 'directEbanking', 'alipay', 'boletobancario',
#                           'sepadirectdebit', 'dotpay', 'giropay', 'ach', 'paypal', 'applepay']



    # Check to make sure variables are set
    # if not merchant_account or not checkout_apikey or not client_key or not hmac_key:
    #     raise Exception("Incomplete configuration in .env")