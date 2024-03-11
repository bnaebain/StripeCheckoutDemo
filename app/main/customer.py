import logging
import sqlite3, hashlib, os
import stripe
import json
import uuid
from main.config import get_stripe_private_key
from flask import jsonify

stripe.api_key = get_stripe_private_key()

def stripe_customerCreate(name, phone, email):
    print("Creating Customer")

    try:
        
        # Create a PaymentIntent with the order amount and currency
        customer = stripe.Customer.create(
            name= name,
            phone = phone,
            email = email,
        )
        print("Customer Response")
        print(customer)
        print("")
        customerID = customer['id']
        return customerID

    except Exception as e:
        return jsonify(error=str(e)), 403