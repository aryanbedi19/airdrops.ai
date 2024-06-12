import openai
from config import Config

openai.api_key = Config.OPENAI_API_KEY

def analyze_sentiment(airdrop_name):
    airdrop_descriptions = {
        "Airdrop1": "This is a great airdrop with lots of potential!",
        "Airdrop2": "This airdrop seems risky and not worth the time.",
    }
    description = airdrop_descriptions.get(airdrop_name, "")
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Analyze the sentiment of the following airdrop description: {description}",
        max_tokens=50
    )
    sentiment_score = float(response.choices[0].text.strip())
    return sentiment_score
