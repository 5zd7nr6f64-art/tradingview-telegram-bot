from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("8216575089:AAEh2oUW3nN0TRq3T3Zw1f9GwFK3yah523Y")
CHAT_ID = os.environ.get("7407364153")

def send_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)

@app.route("/webhook", methods=["POST"])
def webhook():
    text = request.get_data(as_text=True)
    if not text:
        return "no data"
    send_telegram(text)
    return "ok"

@app.route("/")
def home():
    return "Bot is running"
