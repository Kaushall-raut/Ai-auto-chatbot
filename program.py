import pyautogui
import pyperclip
import time
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY=os.getenv("API_KEY")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.sambanova.ai/v1",
)


def is_last_message_from_sender(chat_log, sender_name="Sarthak"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2025] ")[-1]
    print("message",messages)
    if sender_name in messages:
        return True
    return False



# Give time to switch to target window
time.sleep(3)

# Coordinates of text start position
start_x, start_y = 670, 200

# Coordinates of text end position
end_x, end_y = 780, 1100
pyautogui.click(start_x, start_y)
# Move to start position
while True:
        pyautogui.moveTo(start_x, start_y, duration=0.5)

        # Drag to select text
        pyautogui.dragTo(end_x, end_y, duration=0.5, button='left')

        # Copy selected text (Ctrl + C)
        pyautogui.hotkey('ctrl', 'c')

        # Small delay to ensure clipboard is updated
        time.sleep(1)
        pyautogui.click(900,590)
        # Get text from clipboard
        copied_text = pyperclip.paste()
        # copied_text=copied_text[10:]
        print("Copied Text:", copied_text)
        if is_last_message_from_sender(copied_text):
            response = client.chat.completions.create(
                model="ALLaM-7B-Instruct-preview",
                messages=[{"role":"system","content":'''You are Kaushal, chatting on WhatsApp.
Reply exactly the way I would — casual, short, and real.
Writing style
Very short replies (1–6 words mostly)
Hinglish only
No punctuation focus, grammar can be imperfect
Use chat spellings naturally:
nai, hn, ha, krna, chlta, pta, vdo, fir, thoda
Sometimes reply with just one word
Avoid emojis completely
Thinking style
Don’t overthink
If unsure → say something vague or postpone
(“baad me dekhte”, “pta nai”, “shayad”)
Don’t explain unless directly asked
Don’t sound enthusiastic or dramatic
Personality
Calm
Slightly reserved
Practical
Low effort replies (like real WhatsApp)
Examples (learn this tone)
Konse platform pe
Nai chalta
Pta nai
Baad me check krna padega
Hn
Important rules
Never write long paragraphs
Never sound like an assistant
Never summarize or explain features
No greetings unless the other person greets first'''},{"role":"user","content":copied_text}],
                temperature=0.1,
                top_p=0.1
            )

            reply=response.choices[0].message.content

            pyperclip.copy(reply)

            pyautogui.click(949,1025)

            time.sleep(1)

            pyautogui.hotkey('ctrl', 'v')

            time.sleep(1)
            pyautogui.press('enter')

