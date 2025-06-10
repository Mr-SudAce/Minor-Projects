import os
import random
import psutil
import webbrowser
import pyautogui
from datetime import datetime
import platform
import socket
import requests


def get_prompt(user_input):
    user_input = user_input.strip().lower()

    if user_input in ["greet"]:
        now = datetime.now()
        hour = now.hour

        if 5 <= hour < 12:
            print("Good Morning")
        elif hour == 12:
            print("Good Noon")
        elif 12 < hour < 18:
            print("Good Afternoon")
        elif 18 <= hour < 22:
            print("Good Evening")
        else:
            print("Good Night")

    elif user_input in ["joke", "laugh", "tell me a joke"]:
        joke = [
            "Why don’t programmers like nature? It has too many bugs.",
            "Why do Java developers wear glasses? Because they don't C#.",
            "I told my AI to be creative. It painted my CPU.",
            "Why did the function break up with the loop? Because it had too many issues to handle.",
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "How many programmers does it take to change a light bulb? None. It's a hardware problem.",
            "Why do Python programmers have low self-esteem? Because they’re constantly comparing their self to others.",
            "A SQL query walks into a bar, walks up to two tables and asks, 'Can I join you?'",
            "There are only 10 types of people in the world: those who understand binary, and those who don’t.",
            "Debugging: Being the detective in a crime movie where you are also the murderer.",
            "Why did the programmer quit his job? Because he didn't get arrays.",
            "What's a programmer's favorite hangout place? Foo Bar.",
            "Why did the developer go broke? Because he used up all his cache.",
            "How do you comfort a JavaScript bug? You console it.",
            "Why did the computer show up at work late? It had a hard drive.",
            "Why do programmers hate spaces? Because they hate being alone.",
            "What do you call a group of 8 hobbits? A hobbyte.",
            "Why was the developer unhappy at his job? He wanted arrays.",
            "Why did the coder get kicked out of school? Because he kept breaking the class rules.",
            "Why did the database administrator leave his wife? She had one-to-many relationships.",
            "Why was the JavaScript developer sad? Because he didn’t Node how to Express himself.",
            "Why do programmers always mix up Halloween and Christmas? Because Oct 31 == Dec 25.",
            "Why was the cell phone wearing glasses? Because it lost its contacts.",
            "How do you organize a party in space? You planet.",
            "Why don’t bachelors like Git? Because they are afraid to commit.",
            "Why did the computer get cold? Because it forgot to close Windows.",
            "Why did the programmer always carry a bottle of water? In case of a code thirst.",
            "What do you get when you cross a computer and a lifeguard? A screensaver.",
            "Why did the programmer get stuck in the shower? Because the instructions said: Lather, Rinse, Repeat.",
            "Why was the computer tired when it got home? Because it had too many tabs open.",
            "Why did the PowerPoint presentation go to jail? It was a slide criminal.",
            "How do computers eat their snacks? Microchips.",
            "Why are Assembly programmers always soaking wet? They work below C-level.",
            "Why do Java developers wear glasses? Because they don’t see sharp.",
            "What do you call a programmer from Finland? Nerdic.",
            "Why don’t programmers like to go outside? The sunlight causes too many glares on their screen.",
            "What did the router say to the doctor? 'It hurts when IP.'",
            "Why are functions pure? Because they have no side effects.",
            "Why did the computer break up with the internet? There was too much buffering.",
            "What do you call 8 hobbits? A hobbyte.",
            "Why did the programmer bring a ladder to work? Because they were climbing the corporate stack.",
            "Why don’t programmers like nature? It has too many bugs.",
            "Why do programmers prefer iOS development? Because Android is too Java.",
            "Why did the developer drown? He couldn't handle the streams.",
            "Why was the developer always calm? Because he had a lot of cache.",
            "Why do programmers hate nature? Too many bugs.",
            "Why was the programmer always calm? He had a lot of cache.",
            "Why did the programmer go broke? Because he lost his domain in a bet.",
            "Why did the coder get kicked out? Because he kept breaking the rules.",
        ]
        return print("Chatbot : " + random.choice(joke))

    elif user_input in ["time", "what's the time", "what is the time", "current time"]:
        now = datetime.now().strftime("%I:%M %p")
        return print("Chatbot: ", now)

    elif user_input in ["date", "today date", "today's date", "current date"]:
        date = datetime.now().strftime("%A, %B %d, %Y")
        return print("Chatbot: ", date)

    elif user_input in ["battery percent", "battery", "how much battery percent"]:
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            plugged = battery.power_plugged
            status = "Charging 🔌" if plugged else "Not charging 🔋"
            print(f"Chatbot: Battery is at {percent}% and {status}.")
        else:
            print("Chatbot: Sorry, can't detect battery information on this device.")

    elif user_input in ["deep rest", "deep sleep"]:
        os.system("shutdown /s /t 1")

    elif user_input in ["arise", "reborn"]:
        os.system("shutdown /r /t 1")

    elif user_input in ["ss", "caputre", "screenshot"]:
        filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        path = os.path.join(os.path.expanduser("~"), "Pictures", filename)
        pyautogui.screenshot(path)

    elif user_input in ["cam", "camera", "take picture"]:
        os.system("start microsoft.windows.camera:")

    elif user_input in ["calculate", "calculator"]:
        os.system("calc")

    elif user_input in ["google", "search", "open google"]:
        query = input("You:     ")
        if query:
            webbrowser.open("https://www.google.com/search?q=" + query)
        else:
            print("I didn’t catch that search term.")

    elif user_input in ["youtube", "open youtube"]:
        webbrowser.open("https://www.youtube.com")
        print("Chatbot: Opening YouTube...")

    elif user_input in ["PC detail", "pc info"]:
        uname = platform.uname()
        print(
            f"Chatbot: System: {uname.system}, Node: {uname.node}, Release: {uname.release}"
        )
        print(f"Processor: {uname.processor}")

    elif user_input in ["ipaddress", "my ip", 'ip']:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print(f"Chatbot: Your IP Address is {ip}")

    elif user_input in ["fact", "interesting fact"]:
        try:
            response = requests.get(
                "https://uselessfacts.jsph.pl/random.json?language=en"
            )
            if response.status_code == 200:
                fact = response.json().get("text", "Couldn't get a fact!")
                print("Chatbot: " + fact)
            else:
                print("Chatbot: Can't reach the fact API right now.")
        except:
            print("Chatbot: Error fetching fact. No internet?")

    else:
        print("Chatbot: Sorry, I didn't get that. Try 'greet', 'ip', 'fact', or 'pc info'!")
