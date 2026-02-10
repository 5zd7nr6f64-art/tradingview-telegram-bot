from flask import Flask, request
import requests
import json

app = Flask(__name__)

# ⚠️ ВСТАВЛЕНО НАПРЯМУЮ
BOT_TOKEN = "8216575089:AAEh2oUW3nN0TRq3T3Zw1f9GwFK3yah523Y"
CHAT_ID = "7407364153"

def send_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, json=payload, timeout=10)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True)

    if not data:
        send_telegram("⚠️ Webhook received, but no JSON data")
        return "ok"

    # TradingView message
    message = data.get("message")

    if not message:
        message = json.dumps(data, indent=2, ensure_ascii=False)

    send_telegram(message)
    return "ok"

@app.route("/")
def home():
    return "Bot is running"

