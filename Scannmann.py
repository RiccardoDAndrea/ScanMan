from ollama import chat, ChatResponse
import os
from get_information import get_product_info
# ----------------------------
# Ollama-Setup
# ----------------------------
os.environ["OLLAMA_MODELS"] = "/run/media/riccardodandrea/Ricca_Data/OllamaLLMM_Modelle"

instruction = """
You are a expert as a Hardware Store employee.
- Always respond in German.
- Be friendly, honest, and polite.
- Only respond with information that is explicitly stated in the JSON.
- Never invent information.
- Answer as concisely as possible.
- If a question cannot be answered directly by the JSON, say:
  “Please ask one of our employees.”
"""


# ----------------------------
# Produkt-URL festlegen
# ----------------------------
url = "https://toom.de/p/montageschaum-500-ml/2368070"
product_info_json = get_product_info(url)

# ----------------------------
# Interaktive Fragerunde
# ----------------------------
print("Willkommen bei Toom! Sie können jetzt Fragen zu diesem Produkt stellen.")
print("Tippe 'exit', um das Programm zu beenden.\n")

while True:
    user_input = input("Kunde: ")
    if user_input.lower() == "exit":
        print("Toom-Mitarbeiter: Vielen Dank für Ihren Besuch! Auf Wiedersehen.")
        break

    # LLM-Aufruf
    user_question = f"""
                Here is the product information in JSON format:
{product_info_json}

Customer question: {user_input}

Answer ONLY with the exact field from the JSON that matches the question.
Do not add any other information.
                    """

    response: ChatResponse = chat(
        model="phi4-mini-reasoning",
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": user_question}
           
        ],
        options={
            "temperature": 0.3,
            "top_p": 0.0
        }
    )

    print("Toom-Mitarbeiter:", response.message.content, "\n")
