from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8216575089:AAEh2oUW3nN0TRq3T3Zw1f9GwFK3yah523Y"
CHAT_ID = "7407364153"

@app.route("/", methods=["POST"])
def webhook():
    data = request.json

    if not data:
        return "No JSON", 400

    symbol = data.get("symbol", "—")
    tf = data.get("tf", "—")
    signal = data.get("signal", "—")
    zone = data.get("zone", "—")
    htf_trend = data.get("htf_trend", "—")
    bos = data.get("bos", "—")
    impulse = data.get("impulse", "—")
    zone_size = data.get("zone_size_atr", "—")
    age = data.get("age", "—")
    entry = data.get("entry", "—")
    sl = data.get("sl", "—")

    emoji = "🟢" if signal == "LONG" else "🔴"

    message = f"""
📊 {symbol} ({tf})

{emoji} {signal}

📦 Zone: {zone}
📈 H4 Trend: {htf_trend}
📌 BOS: {bos}
⚡ Impulse: {impulse}

📐 Zone Size (ATR): {zone_size}
⏳ Zone Age: {age} bars

🎯 Entry: {entry}
🛑 SL: {sl}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, json=payload)

    return "OK", 200


@app.route("/", methods=["GET"])
def home():
    return "Bot is running", 200
