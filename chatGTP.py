import openai
from playsound import playsound 
from gtts import gTTS
import os
# Set up the OpenAI API key
openai.api_key = ""

# Use the GPT-3 engine
engine = "text-davinci-003"

# Set up the prompt
prompt = "OpenIA:"

def help():
    print("\n talk    - Read the last answer.")
    print(" engines - To print engines list.")
    print(" exit    - Exit this program.\n")

def engines():
    global engine
    engines= openai.Engine.list()
    print ("Engine select : " + engine)   
    n = 0
    for e in engines.data:
        print("   " + str(n) + " ) " + e.id)
        n=n+1

## Options to select engine 
    # option = input("Select number of engine : ")
    # if option < str(n):
    #     print("Engine selected : " + str(engines.data[int(option)].id))
    #     engine = str(engines.data[int(option)].id)
    # else:    
    #     print("Number not valid!!")
     
print(" Type help to options\n")


while True:
    # Get user input
    user_input = input("\033[;34m    Me: \033[;0m ")

    # Check if the user wants to exit the chatbot
    if user_input.lower() == "help":
        help()
        continue
    if user_input.lower() == "engines":
        engines()
        continue
    if user_input.lower() == "exit":
        break
    if user_input.lower() == "talk":
        text = str(response['choices'][0]['text'])
        tts = gTTS(text, lang='es')
        with open(".tmp.mp3","wb") as file:
            tts.write_to_fp(file)
        playsound(".tmp.mp3")
        os.remove(".tmp.mp3")
        continue

    # Generate a response to the user input using the GPT-3 engine
    response = openai.Completion.create(
        engine=engine,
        prompt=user_input,
        max_tokens=1024,
        n = 1,
        stop = None
    )

    # Print the prompt and the response
    print(f"\033[0;36m{prompt}\033[;32m\n{response['choices'][0]['text']}\033[;0m")
