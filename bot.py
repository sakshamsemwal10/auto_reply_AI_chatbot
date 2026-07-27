import os
import time
import pyautogui
import pyperclip
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
    

pyautogui.click(1137 , 1072)
time.sleep(1) 

def is_last_message_from_sender(chat_log, sender_name="Akshat"):
    last_message = chat_log.strip().splitlines()[-1]
    return sender_name in last_message

last_processed_message = ""

while True: 
    time.sleep(5) 

    pyautogui.moveTo(1159,239)
    pyautogui.dragTo(1184,933, duration=1.0, button='left')

    pyautogui.hotkey("ctrl", "c")
    time.sleep(1)

    chat_history = pyperclip.paste()

    pyautogui.click(815,975 )
    time.sleep(0.2)


    if not chat_history.strip():
        print("Clipboard is empty.")
        continue

    latest_message = chat_history.strip().splitlines()[-1]

    print("New message detected")
    print(latest_message)

    if latest_message == last_processed_message:
        continue

    last_processed_message = latest_message

    if is_last_message_from_sender(chat_history):


        prompt = f"""
       You are generating a WhatsApp reply.

        Instructions:
        - Read the conversation carefully.
        - Reply only to the latest message.
        - Use previous messages only for context.
        - Match the language being used (English, Hindi, or Hinglish).
        - Keep the reply short and natural.
        - Sound like a real person, not an AI assistant.
        - Do not over-explain.
        - Do not repeat previous messages.
        - Keep the reply under 20 words.
        - Output only the reply text.

        Conversation:
        {chat_history}
        """
        reply = ""
        print("Calling Gemini...")
        try:
            response = client.models.generate_content(
                model = "gemini-3.6-flash",
                contents=prompt
        )
            print("Response received.")
            reply = response.text.strip()
            print("Gemini finished.")  
            if not reply:
                continue
            pyperclip.copy(reply)

        except Exception as e:
            print("Gemini Error:", e)

        if reply:
            print(reply) 

            pyautogui.click(815,975 )   
            time.sleep(0.5)

            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.5)

            pyautogui.press("enter") 
            time.sleep(1)

            print("Reply sent successfully.")
            time.sleep(1)


 
    