import openai
from config import Config

openai.api_key = Config.OPENAI_API_KEY

def recommend_airdrops(airdrops, wallet_address):
    descriptions = [airdrop['description'] for airdrop in airdrops]
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Given the following airdrop descriptions: {descriptions}, which airdrops would you recommend for a user with wallet address {wallet_address}?",
        max_tokens=100
    )
    recommendations = response.choices[0].text.strip().split("\n")
    return [airdrop for airdrop in airdrops if airdrop['name'] in recommendations]
