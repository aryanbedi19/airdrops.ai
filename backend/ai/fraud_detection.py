import openai
from config import Config

openai.api_key = Config.OPENAI_API_KEY

def assess_risk(airdrop_name):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Assess the risk of the following airdrop: {airdrop_name}",
        max_tokens=50
    )
    risk_score = float(response.choices[0].text.strip())
    return risk_score
