from flask import Blueprint, request, jsonify
from services.chat_service import generate_chat_response

chat_blueprint = Blueprint('chat_api', __name__)

@chat_blueprint.route("/api/chat/commands", methods=["POST"])
def chat_commands():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Invalid request, no data provided."}), 400
    
    if 'prompt' not in data:
        return jsonify({"error": "Invalid request, 'prompt' is missing"}), 400
    
    result = generate_chat_response(data)

    return jsonify(result), 200