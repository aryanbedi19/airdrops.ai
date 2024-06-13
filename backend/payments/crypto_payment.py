import requests
from config import Config

def process_crypto_payment(wallet_address, user_id, amount):
    url = f"https://api.moonpay.com/v1/transactions"
    payload = {
        "wallet_address": wallet_address,
        "amount": amount,
        "currency": "usd",
        "crypto_currency": "eth"
    }
    headers = {
        "Authorization": f"Bearer {Config.MOONPAY_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.status_code == 201
