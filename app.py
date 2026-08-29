
from flask import Flask, jsonify, request, render_template

from nlp_engine import get_response

from flask_cors import CORS
from datetime import datetime
import random
memory = {}

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/api/live-data")
def live_data():
    return jsonify({
        "time": datetime.now().strftime("%H:%M:%S"),
        "users": random.randint(1, 10)
    })

@app.route("/api/ai", methods=["POST"])
def ai():
    data = request.get_json(force=True)

    print("DATA =", data)

    text = data.get("message") or data.get("text", "")

    text = text.strip().lower()
    memory["last_message"] = text

    print("TEXT =", repr(text))

    responses = {
    "hello": "Hello 👋",
    "hi": "Hi there 👋",

    "ሰላም": "ሰላም ነው 😊",
    "ሰላም ነው": "ሰላም ነው 😊",

    "ማነህ": "እኔ የ AbaMela AI ረዳት ነኝ 🤖",
    "አንተ ማነህ": "እኔ የ AbaMela AI ረዳት ነኝ 🤖",

    "what is ai": "AI means Artificial Intelligence 🤖",
    "who are you": "I am your AI assistant 🤖",

    "what is my name": "I don't know your name yet 😊",
    "who is my name": "I don't know your name yet 😊",

    "who i am": "You are my user 😊",

    "thanks": "You're welcome 😊",
    "thank you": "You're welcome 😊",
    "bye": "Goodbye 👋",
    "good morning": "Good morning ☀️",
    "good night": "Good night 🌙",

    "አመሰግናለሁ": "እንኳን ደስ አለኝ 😊",
    "አመሰግናለው": "እንኳን ደስ አለኝ 😊",

    "ደህና ሁን": "ደህና ሁን 👋",

    "እንደምን አደርክ": "ደህና አድሬያለሁ 😊",
    "እንደምን ዋልክ": "ደህና ውዬያለሁ 😊",

    "good afternoon": "Good afternoon 🌞",
    "good evening": "Good evening 🌆",
    "how are you": "I'm fine, thank you 😊",
    "how are you doing": "I'm doing great 😊",
    "welcome": "Welcome 😊",

    "እንዴት ነህ": "ደህና ነኝ 😊",
    "ደህና ነህ": "አዎ ደህና ነኝ 😊",
    "እንኳን ደህና መጣህ": "አመሰግናለሁ 😊",
    "እንኳን ደህና መጣችሁ": "እንኳን ደህና መጣችሁ 😊",
        "ደህና አደር": "መልካም እንቅልፍ 🌙",

    "time": "Current time feature is coming soon ⏰",
    "what time is it": "Current time feature is coming soon ⏰",
    "date": "Current date feature is coming soon 📅",
    "today": "Today feature is coming soon 📅",

    "ሰዓቱ ስንት ነው": "የሰዓት ባህሪ በቅርቡ ይጨመራል ⏰",
    "ዛሬ ቀኑ ስንት ነው": "የቀን ባህሪ በቅርቡ ይጨመራል 📅",
    "ዛሬ ምን ቀን ነው": "የቀን ባህሪ በቅርቡ ይጨመራል 📅",

    "what can you do": "I can chat, answer questions, and help you 😊",
    "help": "Ask me anything. I'll do my best 🤖",
    "about": "I am AbaMela AI Assistant 🤖",
    "version": "AbaMela AI V6 🚀",

    "ምን ትችላለህ": "ጥያቄዎችን እመልሳለሁ፣ እረዳሃለሁ 😊",
    "እርዳኝ": "ምን እንደምትፈልግ ጻፍ 😊",
    "ስለ አባ መላ": "እኔ AbaMela AI ረዳት ነኝ 🤖",
    "ስሪት": "AbaMela AI Version 6 🚀",

    "goodbye": "See you later 👋",
    "see you": "See you again 😊",
    "welcome back": "Welcome back 😊",
    "nice": "Thank you 😊",

    "እስከ ማግኘት": "ደህና ሁን 👋",
    "እንኳን በደህና መጣህ": "አመሰግናለሁ 😊",
    "ጥሩ ነው": "ደስ ብሎኛል 😊",
    "በጣም ጥሩ": "አመሰግናለሁ 🌹",

    "yes": "Great 😊",
    "no": "Okay 👍",
    "ok": "Okay 😊",
    "okay": "Okay 😊",

                    "አዎ": "ጥሩ 😊",
        "አይ": "እሺ 👍",
        "እሺ": "እሺ 😊",
        "እሺ አባ መላ": "እሺ 😊🌹",
    }

        # STEP 5 — Simple Memory 🧠

    if text.startswith("my name is "):
        name = text.replace("my name is ", "", 1).strip()

        if name:
            memory["name"] = name
            return jsonify({"response": f"Nice to meet you, {name} 😊"})

    elif "what is my name" in text:
        if "name" in memory:
            return jsonify({"response": f"Your name is {memory['name']} 😊"})
        else:
            return jsonify({"response": "I don't know your name yet 😊"})

    # STEP 6 — Context Memory 🧠

    if text.startswith("i like "):
        item = text.replace("i like ", "", 1).strip()

        if item:
            memory["favorite"] = item
            return jsonify({
                "response": f"Nice! I remember that you like {item} 😊"
            })

    elif "what do i like" in text:
        if "favorite" in memory:
            return jsonify({
                "response": f"You like {memory['favorite']} 😊"
            })
        else:
            return jsonify({
                "response": "I don't know what you like yet 😊"
            })

    # ከዚህ በታች የቀድሞ if/elif logic እንዳለ ይቀጥላል

    if "hello" in text:
        return jsonify({"response": "Hello 👋"})

    elif "hi" in text:
        return jsonify({"response": "Hi there 👋"})

    elif "ሰላም" in text:
        return jsonify({"response": "ሰላም ነው 😊"})

    elif "ai" in text:
        return jsonify({"response": "AI means Artificial Intelligence 🤖"})

    elif "ማነህ" in text or "አንተ ማነህ" in text:
        return jsonify({"response": "እኔ የ AbaMela AI ረዳት ነኝ 🤖"})

    elif "what time is it" in text or "time" in text:
        current_time = datetime.now().strftime("%H:%M:%S")
        return jsonify({"response": f"Current time is {current_time} ⏰"})

    elif "date" in text or "today" in text:
        current_date = datetime.now().strftime("%Y-%m-%d")
        return jsonify({"response": f"Today's date is {current_date} 📅"})

    elif "ሰዓቱ ስንት ነው" in text:
        current_time = datetime.now().strftime("%H:%M:%S")
        return jsonify({"response": f"አሁን ሰዓቱ {current_time} ነው ⏰"})

    elif "ዛሬ ቀኑ ስንት ነው" in text or "ዛሬ ምን ቀን ነው" in text:
        current_date = datetime.now().strftime("%Y-%m-%d")
        return jsonify({"response": f"ዛሬ ቀኑ {current_date} ነው 📅"})

    # ከዚህ በታች ያለውን የቀድሞ return እንዳለ ተወው

    reply = responses.get(text, "አልገባኝም 🤖")

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)




















































































































































































































































































































+0

