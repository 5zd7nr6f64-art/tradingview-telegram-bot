from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8216575089:AAEh2oUW3nN0TRq3T3Zw1f9GwFK3yah523Y"
CHAT_ID = "7407364153"

@app.route("/", methods=["POST"])
def webhook():
    data = request.json

    if not data:
        return "No JSON received", 400

    try:
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

        message = (
            f"📊 {symbol} ({tf})\n\n"
            f"{emoji} {signal}\n\n"
            f"📦 Zone: {zone}\n"
            f"📈 H4 Trend: {htf_trend}\n"
            f"📌 BOS: {bos}\n"
            f"⚡ Impulse: {impulse}\n\n"
            f"📐 Zone Size (ATR): {zone_size}\n"
            f"⏳ Zone Age: {age} bars\n\n"
            f"🎯 Entry: {entry}\n"
            f"🛑 SL: {sl}"
        )

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }

        response = requests.post(url, json=payload)

        print("Telegram response:", response.text)

        return "OK", 200

    except Exception as e:
        print("ERROR:", str(e))
        return "Error", 500


@app.route("/", methods=["GET"])
def home():
    return "Bot is running", 200
