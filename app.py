from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8216575089:AAEh2oUW3nN0TRq3T3Zw1f9GwFK3yah523Y"
CHAT_ID = "7407364153"

def send_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if not data:
        return "no json", 400

    symbol = data.get("symbol", "-")
    tf = data.get("tf", "-")
    signal = data.get("signal", "-")
    zone = data.get("zone", "-")

    # 🔹 Новые поля из Pine v6
    htf_trend = data.get("htf_trend", "-")
    bos = data.get("bos", "-")
    impulse = data.get("impulse", "-")
    zone_size = data.get("zone_size_atr", "-")
    age = data.get("age", "-")

    entry = data.get("entry", "-")
    sl = data.get("sl", "-")
    tp = data.get("tp", "-")

    direction = "🟢 LONG" if signal == "LONG" else "🔴 SHORT"

    message = f"""📊 {symbol} ({tf})

{direction}

📦 Zone: {zone}
📈 H4 Trend: {htf_trend}
📌 BOS: {bos}
⚡ Impulse: {impulse}

📐 Zone Size (ATR): {zone_size}
⏳ Zone Age: {age} bars

🎯 Entry: {entry}
🛑 SL: {sl}
💰 TP (HTF): {tp}
"""

    send_telegram(message)

    return "ok"

if __name__ == "__main__":
    app.run()
