import openai

# Set up the API key for OpenAI
openai.api_key = "YOUR_OPENAI_API_KEY"
# The charging from openai will be shown at https://platform.openai.com/account/usage , notice that every api calls will be charged.

# Define the prompt for the chatbot
history_message = [{"role": "system", "content": "You are a helpful assistant."}]

# Define a function to generate a response from the chatbot
def generate_response(model, history_message):
    response = model.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=history_message
    )
    message = response['choices'][0]['message']['content']
    return message


while True:
    prompt = input("User: ")
    history_message.append({"role": "user", "content": prompt})
    chatbot_response = generate_response(openai, history_message)
    history_message.append({"role": "assistant", "content": chatbot_response})
    print("ChatGPT:", chatbot_response)
