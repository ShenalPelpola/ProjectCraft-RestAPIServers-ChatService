from flask import current_app
from langchain_community.chat_message_histories import RedisChatMessageHistory

def get_message_history(conversation_id: str) -> RedisChatMessageHistory:
    return RedisChatMessageHistory(conversation_id, url=current_app.config["REDIS_URL"])