import json
import uuid
from store.history import get_message_history
from flask import current_app
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import ConfigurableFieldSpec
from langchain_core.runnables.history import RunnableWithMessageHistory

def generate_chat_response(data):
    model_name = current_app.config['CHAT_OPEN_AI']['DEFAULT_MODEL']
    temperature = current_app.config['CHAT_OPEN_AI']['DEFAULT_TEMPERATURE']
    model = ChatOpenAI(model=model_name, temperature=temperature, openai_api_key=current_app.config["OPENAI_API_KEY"])
    instructions = load_instructions()
    
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", instructions),
            MessagesPlaceholder(variable_name="history"),
            ("user", "{input}")
        ]
    )
    runnable = prompt | model

    runnable_with_message_history = RunnableWithMessageHistory(
        runnable,
        get_message_history,
        input_messages_key="input",
        history_messages_key="history",
        history_factory_config=[
            ConfigurableFieldSpec(
                id="conversation_id",
                annotation=str,
                name="Conversation ID",
                description="Unique identifier for the conversation.",
                default="",
                is_shared=True,
            ),
        ],
    )

    conversation_id = data.get("conversation_id", str(uuid.uuid4()))
    response = runnable_with_message_history.invoke(
        {"input": data["prompt"]},
        config={"configurable": {"conversation_id": conversation_id}},
    )
    
    return {
        "conversation_id": conversation_id,
        "commands": json.loads(response.content.strip())
    }

def load_instructions():
    with open('instructions.txt', 'r') as file:
        return file.read()