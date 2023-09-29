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
    response = ""
    response_dict = openai.ChatCompletion.create(
        model=MODEL,          
        messages = conversation,
        temperature=2,
    )
    
    # Get the response that chat gpt gave us
    response = response_dict['choices'][0]['message']['content']

    return response


while True:
    user_message = input("You:\t")
    conversation.append({
        "role": "system",
        "content": "You are a helpful, humble expert."
    })
    conversation.append({
        "role": "user",
        "content": user_message
    })

    gpt_response = gptResponse(user_message)
    conversation.append(gpt_response)

    if user_message.lower() == "exit":
        break
