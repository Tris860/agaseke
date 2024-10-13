from flask import Flask, render_template
from flask import Flask,Blueprint,render_template,request
import requests

views = Blueprint('views',__name__)
@views.route('/')
def home():
    return render_template('index.html')



@views.route('/pay', methods=['POST'])
def pay():
    amount = request.form['amount']
    # Replace with your MTN API credentials and endpoint
    api_url = "https://api.mtn.com/v1/payments"
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Content-Type": "application/json"
    }
    data = {
        "amount": amount,
        "currency": "RWF",
        "externalId": "123456",
        "payer": {
            "partyIdType": "MSISDN",
            "partyId": "250XXXXXXXXX"  # Replace with the payer's phone number
        },
        "payerMessage": "Payment for services",
        "payeeNote": "Thank you for your payment"
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 201:
        return "Payment successful!"
    else:
        return "Payment failed!"


