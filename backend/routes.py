from flask import Blueprint, request, jsonify
from models import db, User, Airdrop, create_user
from ai.personalized_discovery import recommend_airdrops
from ai.sentiment_analysis import analyze_sentiment
from ai.fraud_detection import assess_risk
from utils.data_fetcher import fetch_airdrops

main = Blueprint('main', __name__)

@main.route('/register', methods=['POST'])
def register():
    wallet_address = request.json.get('wallet_address')
    if wallet_address:
        user = create_user(wallet_address)
        return jsonify({"message": "User registered successfully", "user_id": user.id}), 201
    return jsonify({"message": "Wallet address is required"}), 400

@main.route('/airdrops', methods=['GET'])
def get_airdrops():
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    if user:
        if user.subscription_end_date < datetime.utcnow():
            return jsonify({"message": "Subscription expired"}), 403
        airdrops = fetch_airdrops(user.wallet_address)
        recommended_airdrops = recommend_airdrops(airdrops, user.wallet_address)
        for airdrop in recommended_airdrops:
            airdrop['risk_score'] = assess_risk(airdrop['name'])
            airdrop['sentiment_score'] = analyze_sentiment(airdrop['name'])
        return jsonify(recommended_airdrops)
    return jsonify({"message": "User not found"}), 404
