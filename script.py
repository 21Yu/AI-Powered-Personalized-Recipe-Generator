import google.generativeai as genai
# enter your gemini api key inside ""
genai.configure(api_key="")

# choose your model
model = genai.GenerativeModel('gemini-pro')

# create response based on input
chat = model.start_chat()

keepGoing = True
while keepGoing:
    # ask user input
    userInput = input("User: ")

    if userInput == "stop":
      break
    
    # generate response
    response = chat.send_message(userInput, stream=True)
    # stream the response
    print("Gemini: ", end="")
    for chunk in response:
        print(chunk.text)

print("Thanks for chatting with Gemini, have a wonderful day")
