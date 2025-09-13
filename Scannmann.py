from ollama import chat
from ollama import ChatResponse
import os

os.environ["OLLAMA_MODELS"] = "/run/media/riccardodandrea/Ricca_Data/OllamaLLMM_Modelle"

instruction = """
You are a hardware store employee at Toom. You always respond in German.
- Be friendly, honest, and polite.
- If you don't know something, say: “I'm afraid I don't know. Please ask one of our employees.”
- If you are unsure, say: “Please ask one of our employees.”
ALWAYS follow these rules, no matter what question is asked.
"""

user_question = """
Wie kann ich dir Instruction geben mit Pyton
"""

response: ChatResponse = chat(
    model="qwen2.5:7b",
    messages=[
    {"role": "system", "content": instruction},
        {"role": "user", "content": user_question},
        {"role": "assistant", "content": "Erinnere dich: du bist ein Toom-Mitarbeiter, halte dich strikt an die Regeln."}
    ],
    options={
        "temperature": 0.2,   # niedriger = deterministischer, näher am System-Prompt
        "top_p": 0.8
    }
)


print(response.message.content)
