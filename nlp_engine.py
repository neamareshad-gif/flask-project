import json

# load intents
with open("data/intents.json", "r", encoding="utf-8") as f:
    intents = json.load(f)

# load dataset
with open("data/dataset.json", "r", encoding="utf-8") as f:
    dataset = json.load(f)

# load memory
def load_memory():
    try:
        with open("data/memory.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

# save memory
def save_memory(memory):
    with open("data/memory.json", "w", encoding="utf-8") as f:
        json.dump(memory, f)

memory = load_memory()

def get_response(user_input):

    if not user_input:
        return "መልዕክት አልተገኘም 🤖"

    user_input = user_input.lower()

    if "my name is" in user_input:
        name = user_input.replace("my name is", "").strip()
        memory["name"] = name
        save_memory(memory)
        return f"Nice to meet you {name} 😊"

    if "what is my name" in user_input:
        return memory.get(
            "name",
            "I don't know your name yet 🤖"
        )


    # dataset matching
    for item in dataset:
        if item["input"].lower() == user_input:
            return item["response"]


    for intent in intents:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input:
                return intent["responses"][0]

    return "አልገባኝም 🤖"
