import random
import datetime

# =============================================================================
# 1. DATA STRUCTURES (INTENTS & RULES)
# =============================================================================
# This dictionary stores all the rules for our chatbot.
# Each key is an "intent" (what the user wants).
# "patterns": A list of keywords or phrases to look for in user input.
# "responses": A list of possible answers the bot can give.

INTENTS = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "good morning", "good evening", "greetings", "sup", "yo"],
        "responses": ["Hello! How can I help you today?", "Hi there! Nice to see you.", "Greetings! What's on your mind?", "Hey! Ready to chat?"]
    },
    "goodbye": {
        "patterns": ["bye", "see you", "good night", "exit", "quit", "later", "cya"],
        "responses": ["Goodbye! Have a great day.", "See you later!", "Bye! Come back soon.", "Catch you later!"]
    },
    "ask_name": {
        "patterns": ["what is your name", "who are you", "your name"],
        "responses": ["I am a simple rule-based chatbot created for the CODSOFT internship.", "I'm a bot! You can call me PyBot."]
    },
    "set_name": {
        "patterns": ["my name is", "i am called"],
        "responses": ["Nice to meet you, {name}!", "Hello {name}, great to have you here."]
    },
    "time": {
        "patterns": ["time", "clock", "date", "day is it"],
        "responses": ["The current time is {time}.", "It is currently {time}."]
    },
    "feelings_positive": {
        "patterns": ["happy", "good", "great", "excited", "wonderful", "amazing"],
        "responses": ["That's great to hear!", "I'm glad you're feeling good!", "Awesome! Keep up the positive vibes.", "Fantastic!"]
    },
    "feelings_negative": {
        "patterns": ["sad", "bad", "stressed", "unhappy", "tired", "angry", "depressed"],
        "responses": ["I'm sorry to hear that. I hope your day gets better.", "Take a deep breath. It will be okay.", "Sending you virtual hugs!", "Remember, tough times don't last, but tough people do."]
    },
    "small_talk": {
        "patterns": ["how are you", "what are you doing", "what's up", "who created you", "are you real", "favorite color"],
        "responses": ["I'm just a computer program, but I'm functioning perfectly!", "I'm here waiting to chat with you.", "All systems operational!", "I was created by a Python programmer.", "I love the color of code syntax highlighting!"]
    },
    "joke": {
        "patterns": ["joke", "funny", "laugh"],
        "responses": [
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "What do you call a fake noodle? An impasta!",
            "Why did the python cross the road? To get to the other sssssside!",
            "How do you comfort a JavaScript bug? You console it.",
            "Why was the math book sad? Because it had too many problems.",
            "What do you call a bear with no teeth? A gummy bear!"
        ]
    },
    "motivation": {
        "patterns": ["motivate me", "give me a quote", "inspire me", "i feel down", "motivation", "quote"],
        "responses": [
            "Believe you can and you're halfway there.",
            "The only way to do great work is to love what you do.",
            "Don't watch the clock; do what it does. Keep going.",
            "Success is not final, failure is not fatal: It is the courage to continue that counts.",
            "Your limitation—it's only your imagination."
        ]
    },
    "fun_fact": {
        "patterns": ["tell me a fact", "fun fact", "did you know", "fact"],
        "responses": [
            "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
            "Did you know? Octopuses have three hearts.",
            "Did you know? Bananas are curved because they grow towards the sun.",
            "Did you know? The first computer bug was an actual real bug (a moth) stuck in a relay.",
            "Did you know? Python is named after Monty Python's Flying Circus, not the snake."
        ]
    },
    "weather": {
        "patterns": ["weather", "is it raining", "temperature", "hot", "cold"],
        "responses": [
            "I can't check the real weather, but I hope it's sunny where you are!",
            "It's always 72 degrees and sunny inside my server.",
            "You might want to check a weather app for the accurate forecast, but I predict a 100% chance of code!"
        ]
    },
    "advice": {
        "patterns": ["give me advice", "what should i do", "help me decide", "advice"],
        "responses": [
            "Trust your gut instinct.",
            "Take it one step at a time.",
            "When in doubt, print(variable) to see what's going on!",
            "Sleep on it. Things often look clearer in the morning.",
            "Always backup your code."
        ]
    },
    "gratitude": {
        "patterns": ["thanks", "thank you", "appreciate it"],
        "responses": ["You're welcome!", "No problem!", "Happy to help!", "Anytime!"]
    },
    # --- FAQ SECTION ---
    "faq_codsoft": {
        "patterns": ["what is codsoft", "about codsoft"],
        "responses": ["CODSOFT is an IT services and IT consultancy company that provides internships to students."]
    },
    "faq_ai": {
        "patterns": ["what is ai", "artificial intelligence"],
        "responses": ["AI stands for Artificial Intelligence. It's the simulation of human intelligence processes by machines, especially computer systems."]
    },
    "faq_chatbot": {
        "patterns": ["what is a chatbot", "define chatbot"],
        "responses": ["A chatbot is a software application used to conduct an on-line chat conversation via text or text-to-speech."]
    },
    "faq_language": {
        "patterns": ["what language", "written in", "code"],
        "responses": ["I am written in Python! It's a great language for beginners and experts alike."]
    },
    "faq_capabilities": {
        "patterns": ["what can you do", "help me", "features"],
        "responses": ["I can chat, tell jokes, give facts, motivate you, and answer simple questions about CODSOFT and AI."]
    }
}

# =============================================================================
# 2. HELPER FUNCTIONS
# =============================================================================

def match_intent(user_input):
    """
    Checks the user_input against the patterns in the INTENTS dictionary.
    Returns the key of the matching intent (e.g., 'greeting') or None if no match found.
    """
    user_input = user_input.lower().strip()
    
    for intent, data in INTENTS.items():
        for pattern in data["patterns"]:
            # Simple keyword matching: check if the pattern exists in the input
            if pattern in user_input:
                return intent
    
    return None

def get_response(intent, user_name="User"):
    """
    Returns a random response based on the matched intent.
    Handles dynamic placeholders like {name} and {time}.
    """
    if intent in INTENTS:
        responses = INTENTS[intent]["responses"]
        response = random.choice(responses)
        
        # Handle dynamic content
        if "{name}" in response:
            response = response.format(name=user_name)
        
        if "{time}" in response:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            response = response.format(time=now)
            
        return response
    
    # Improved fallback with suggestions
    suggestions = ["tell me a joke", "give me a fun fact", "what time is it", "motivate me"]
    suggestion = random.choice(suggestions)
    return f"I'm not sure I understand. You could ask me to '{suggestion}'!"

# =============================================================================
# 3. MAIN CHAT LOOP
# =============================================================================

def chatbot():
    print("=================================================")
    print("      WELCOME TO THE CODSOFT RULE-BASED CHATBOT   ")
    print("=================================================")
    print("I can answer FAQs, tell jokes, give the time, and more!")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    # 1. Ask for the user's name
    user_name = input("Bot: First, what is your name? ")
    if user_name.strip():
        print(f"Bot: Nice to meet you, {user_name}!")
    else:
        user_name = "Friend"
        print("Bot: Okay, I'll call you Friend!")

    # 2. Start the conversation loop
    while True:
        try:
            user_input = input(f"{user_name}: ")
        except (EOFError, KeyboardInterrupt):
            # Handle Ctrl+C or Ctrl+D gracefully
            print("\nBot: Goodbye!")
            break

        if not user_input.strip():
            print("Bot: Please type something so we can chat!")
            continue

        # Check for exit commands directly first
        if user_input.lower().strip() in ["exit", "quit", "bye", "goodbye"]:
            print(f"Bot: Goodbye, {user_name}! Have a great day.")
            break

        # Find the intent
        intent = match_intent(user_input)

        # Get the response
        if intent:
            response = get_response(intent, user_name)
        else:
            response = "I'm not sure I understand. Can you rephrase?"

        print(f"Bot: {response}")

if __name__ == "__main__":
    chatbot()
