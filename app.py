from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "LINE Webhook is running"

@app.route("/webhook", methods=['POST'])
def webhook():
    data = request.get_json()
    print("LINE Webhook Data:", data)  # ดูข้อมูลจาก LINE ที่ส่งมา
    return "OK", 200

if __name__ == "__main__":
    app.run()
