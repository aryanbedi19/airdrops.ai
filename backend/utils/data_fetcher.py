import requests

def fetch_airdrops(wallet_address):
    airdrops = []
    networks = ["ethereum", "bsc", "polygon", "solana", "avalanche"]
    for network in networks:
        response = requests.get(f"https://api.airdropdata.com/{network}/airdrops?wallet={wallet_address}")
        if response.status_code == 200:
            airdrops.extend(response.json())
    return airdrops
