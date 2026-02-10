from flask import Flask, request
import requests

app = Flask(__name__)

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

    # извлекаем поля
    symbol = data.get("symbol", "—")
    timeframe = data.get("timeframe", "—")
    signal_type = data.get("type", "—")
    setup = data.get("setup", "—")
    trend = data.get("trend", "—")
    entry = data.get("entry", "—")
    stop = data.get("stop", "—")
    tp = data.get("tp", "—")
    rr = data.get("rr", "—")
    quality = data.get("quality", "—")
    confidence = data.get("confidence", "—")

    direction_emoji = "🟢" if signal_type.upper() == "LONG" else "🔴"

    message = (
        f"📊 {symbol} ({timeframe})\n\n"
        f"{direction_emoji} {signal_type}\n"
        f"📦 Setup: {setup}\n"
        f"📈 Trend: {trend}\n\n"
        f"🎯 Entry: {entry}\n"
        f"🛑 SL: {stop}\n"
        f"💰 TP: {tp}\n"
        f"⚖️ RR: {rr}\n\n"
        f"⭐ Quality: {quality}\n"
        f"📊 Confidence: {confidence}"
    )

    send_telegram(message)
    return "ok"

@app.route("/")
def home():
    return "Bot is running"

