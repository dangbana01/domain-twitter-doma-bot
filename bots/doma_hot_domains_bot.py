import os
import tweepy
import schedule
import time
from pathlib import Path
from dotenv import load_dotenv
from utils.domain_utils import fetch_expired_domains_from_godaddy, filter_domains

# Load .env from config folder
env_path = Path(__file__).resolve().parent.parent / "config" / ".env"
load_dotenv(dotenv_path=env_path)

# Fetch Twitter keys
API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Validate Twitter keys
missing = [k for k, v in {
    "API_KEY": API_KEY,
    "API_KEY_SECRET": API_KEY_SECRET,
    "ACCESS_TOKEN": ACCESS_TOKEN,
    "ACCESS_TOKEN_SECRET": ACCESS_TOKEN_SECRET
}.items() if v is None]

if missing:
    raise ValueError(f"Missing keys in .env: {missing}")

print("All Twitter keys loaded successfully ✅")

# Tweepy authentication
auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Bot logic
def run_bot():
    try:
        # Fetch expired domains
        domains = fetch_expired_domains_from_godaddy(limit=20)

        # Filter domains (example: minimum price $0, no keyword filter)
        filtered_domains = filter_domains(domains, min_price=0, keyword=None)

        for domain in filtered_domains:
            tweet_text = f"🔥 New expired domain alert: {domain['domain']} - Last bid ${domain.get('price', 'N/A')}"
            print("Tweeting:", tweet_text)
            api.update_status(tweet_text)

    except Exception as e:
        print("Error in bot:", e)

# Run immediately once on start
run_bot()

# Schedule the bot every 6 hours
schedule.every(6).hours.do(run_bot)

print("Bot started... Fetching expired domains every 6 hours.")

# Run continuously
while True:
    schedule.run_pending()
    time.sleep(60)
