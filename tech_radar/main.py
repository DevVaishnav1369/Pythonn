import json
import random
from datetime import datetime
from instagrapi import Client
import time

USERNAME = "your_username"
PASSWORD = "your_password"

def load_data():
    with open("data.json", "r") as file:
        return json.load(file)

def generate_caption():
    data = load_data()

    tool = random.choice(data["tools"])
    job = random.choice(data["jobs"])
    trend = random.choice(data["trends"])

    today = datetime.now().strftime("%B %d, %Y")

    caption = f"""
🔥 DAILY TECH RADAR – {today}

🛠 Tool:
{tool}

💼 Job:
{job}

🚀 Trend:
{trend}

Follow for daily tech updates 🚀
"""

    return caption

def post_to_instagram():
    cl = Client()
    cl.login(USERNAME, PASSWORD)

    caption = generate_caption()

    cl.photo_upload("image.jpg", caption)

    print("✅ Posted successfully!")

if __name__ == "__main__":
    post_to_instagram()
