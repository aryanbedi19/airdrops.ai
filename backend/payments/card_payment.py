import stripe
from config import Config

stripe.api_key = Config.STRIPE_API_KEY

def process_card_payment(card_info, amount, user_id):
    try:
        charge = stripe.Charge.create(
            amount=int(amount * 100),  # amount in cents
            currency="usd",
            source=card_info["id"],
            description=f"Subscription payment for user {user_id}"
        )
        return charge["status"] == "succeeded"
    except stripe.error.StripeError as e:
        print(f"Stripe error: {e}")
        return False
