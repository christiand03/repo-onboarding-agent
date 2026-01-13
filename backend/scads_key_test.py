import os 

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Secret key und base-url "https://llm.scads.ai/v1" in der .env setzen, dann lassen sich alle 
# Modelle, die verfügbar sind anzeigen
client = OpenAI(
    base_url=os.getenv("SCADSLLM_URL"),
    api_key=os.getenv("SCADS_AI_KEY")
)

print("""
Available models:
""")
for model in client.models.list().data:
    print(model.id)

# model_name = "alias-ha"

# # Use model
# response = client.chat.completions.create(messages=[{"role":"user","content":"Tell me a joke!"}],model=model_name)

# # Print the joke
# print("""
# Your joke:
# """)
# joke = response.choices[0].message.content
# print(joke)
