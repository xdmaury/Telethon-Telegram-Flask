from flask import Flask, request, jsonify
import asyncio
from telegram_utils import send_message, start

app = Flask(__name__)

@app.route('/send-message', methods=['POST'])
def send_message_route():
    try:
        data = request.json
        user_id = data.get('user_id')
        message = data.get('message')

        if not user_id or not message:
            return jsonify({"error": "Both 'user_id' and 'message' are required."}), 400


        asyncio.run(send_message(user_id, message))
        return jsonify({"success": f"Message sent to {user_id}."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    asyncio.run(start())
    app.run(debug=True, port=5001, host='0.0.0.0')
