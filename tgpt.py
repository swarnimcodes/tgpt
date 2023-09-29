import openai
import os

MODEL = "gpt-3.5-turbo-0613"

openai_api_key: str | None = os.environ.get("OPENAI_API_KEY_MASTERSOFT")

if openai_api_key is None:
    print("OpenAI API key not found!")
else:
    openai.api_key = openai_api_key

conversation = []

def gptResponse(user_message):
    response_dict = openai.ChatCompletion.create(
        model=MODEL,          
        messages = conversation,
        temperature=0.7,
        max_tokens=100
    )
    

    return response_dict


while True:
    conversation.append({
        "role": "system",
        "content": "You are a helpful, humble expert."
    })
    
    user_message = input("You:\t")
    conversation.append({
        "role": "user",
        "content": user_message
    })

    # response = response_dict['choices'][0]['message']['content']
    gpt_response = gptResponse(user_message)
    gpt_message = gpt_response['choices'][0]['message']['content']
    conversation.append({
        "role": "assistant",
        "content": gpt_message
    })
    print(f"GPT:\t{gpt_message}")

    if user_message.lower() == "exit":
        break
