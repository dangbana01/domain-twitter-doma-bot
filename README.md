Domain Twitter Doma Bot

A Python bot that fetches live expired domains from GoDaddy Auctions and posts them automatically on Twitter. Ideal for domain investors looking for real-time alerts.

Features

Fetches live expired domains from GoDaddy.

Filters domains by price or keyword.

Tweets new domains automatically.

Runs immediately on start and then every 6 hours.

Easy setup via .env file for API keys.

Setup & Installation

Clone the repo

git clone https://github.com/dangbana01/domain-twitter-doma-bot.git
cd domain-twitter-doma-bot


Create a virtual environment

python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # macOS/Linux


Install dependencies

pip install -r requirements.txt


Configure API keys

Create a .env file in config/:

# Twitter API keys
API_KEY=your_api_key
API_KEY_SECRET=your_api_key_secret
ACCESS_TOKEN=your_access_token
ACCESS_TOKEN_SECRET=your_access_token_secret

# GoDaddy API keys (optional)
GODADDY_API_KEY=your_godaddy_api_key
GODADDY_API_SECRET=your_godaddy_api_secret


⚠️ Do not commit .env to GitHub for security reasons.

Run the Bot
python -m bots.doma_hot_domains_bot


The bot will fetch and tweet domains immediately, then continue every 6 hours.

Project Structure
domain-twitter-doma-bot/
│
├─ bots/
│   ├─ doma_hot_domains_bot.py      # live domain alerts bot
│   └─ doma_namebio_bot.py          # optional, NameBio bot
│
├─ config/
│   └─ .env                        # API keys (not committed)
│
├─ utils/
│   └─ domain_utils.py             # domain fetching & filtering
│
└─ requirements.txt                # Python dependencies

Notes

Avoid tweeting the same domain twice by using a local cache (future improvement).

Make sure your IP isn’t blocked by GoDaddy if running frequently.

Currently, NameBio integration is optional; the bot works with GoDaddy only.

License

MIT License



If you want, I can also write a .env.example file so contributors know exactly what keys to add without exposing your secrets.

Do you want me to do that next?
