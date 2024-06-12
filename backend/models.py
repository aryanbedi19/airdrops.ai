from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wallet_address = db.Column(db.String(128), unique=True, nullable=False)
    subscription_end_date = db.Column(db.DateTime, nullable=False)

class Airdrop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.String(256))
    claim_url = db.Column(db.String(256))
    logo_url = db.Column(db.String(256))
    network = db.Column(db.String(64))
    value = db.Column(db.Float)
    percentage = db.Column(db.Float)
    sentiment_score = db.Column(db.Float)
    risk_score = db.Column(db.Float)

def create_user(wallet_address):
    subscription_end_date = datetime.utcnow() + timedelta(days=30)
    user = User(wallet_address=wallet_address, subscription_end_date=subscription_end_date)
    db.session.add(user)
    db.session.commit()
    return user
