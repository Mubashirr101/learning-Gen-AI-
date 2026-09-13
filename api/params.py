import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)
# tempratures
# for temprature in [0,1,1]:
#     response = client.chat.completions.create(
#         model="openai/gpt-oss-20b",
#         messages=[
#             {"role": "user", "content": "what color is a strawberry?"}
#         ],
#         temperature=temprature
#     )
#     print(f"temp {temprature}: {response.choices[0].message.content}")

# max tokens
# for tokens in [20,80,95]:
#     response = client.chat.completions.create(
#         model = "openai/gpt-oss-20b",
#         messages=[
#             {"role":"user","content":"color of strawberry"}
#         ],
#         max_tokens= tokens
#     )
#     print(f"max-tokens {tokens}: {response.choices[0].message.content}")

# top p
for p in [1,0.1,0.5]:
    response = client.chat.completions.create(
        model = "openai/gpt-oss-20b",
        messages=[
            {"role":"user","content":"whats the color of strawberry?"}
        ],
        top_p=p
    )
    print(f"priority {p}: {response.choices[0].message.content}")
