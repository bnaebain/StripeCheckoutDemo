import logging
import sqlite3, hashlib, os
import stripe
import json
import uuid
from main.config import get_stripe_private_key
from flask import jsonify

stripe.api_key = get_stripe_private_key()

def stripe_paymentIntent(amount, currency, email, customerID):
    print("Creating Payment Intent")

    try:
        
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount= int(amount*100),
            currency=currency,
            receipt_email=email,
            customer=customerID,
            setup_future_usage='on_session',
            # In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
            automatic_payment_methods={
                'enabled': True,
            },
        )
        print("Intent Request")
        print(intent)
        print("")
        return jsonify({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify(error=str(e)), 403