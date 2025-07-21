import random
crm_profiles = {
    "john_doe": {
        "name": "John Doe",
        "email": "john@example.com",
        "previous_issue": "loan query"
    },
    "jane_smith": {
        "name": "Jane Smith",
        "email": "jane@example.com",
        "previous_issue": "internet not working"
    }
}

knowledge_base = {
    "balance": "To check your balance, go to the mobile app and select 'My Account'.",
    "loan": "You can apply for or inquire about loans through our online portal or nearest branch.",
    "billing": "Visit the billing section on our website to resolve any billing issues.",
    "internet": "Please try restarting your modem. If the issue persists, contact support.",
    "plan upgrade": "You can upgrade your plan via the app or by calling our helpline.",
    "ticket": "A support ticket has been raised. Our team will get in touch with you shortly."
}

escalation_keywords = ["not working", "complaint", "angry", "talk to human", "real person"]

conversation_log = []

feedback_log = []


def get_crm_profile(user_id):
    return crm_profiles.get(user_id, {
        "name": "Guest",
        "email": "guest@support.com",
        "previous_issue": "none"
    })

def preprocess_input(user_input):
    return user_input.lower().strip()

def get_bot_response(user_query):
    for keyword, response in knowledge_base.items():
        if keyword in user_query:
            return response
    return None  # No match

def check_escalation(user_query):
    return any(keyword in user_query for keyword in escalation_keywords)

def collect_feedback(query, response):
    fb = input("🤖 Was this answer helpful? (yes/no): ").strip().lower()
    feedback_log.append({"query": query, "response": response, "feedback": fb})

def start_ai_ebpl(user_id="john_doe"):
    profile = get_crm_profile(user_id)
    print(f"\n👋 Welcome {profile['name']}! How can I assist you today?\n(Previous issue: {profile['previous_issue']})")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("AI-EBPL: 👋 Thank you! Have a nice day.")
            break

        user_query = preprocess_input(user_input)
        conversation_log.append(user_query)

        if check_escalation(user_query):
            print("AI-EBPL: Transferring you to a human agent for better assistance... 🙋‍♂️")
            continue

       
        response = get_bot_response(user_query)
        if response:
            print("AI-EBPL:", response)
        else:
            print("AI-EBPL: I’m sorry, I couldn't understand that. Let me connect you to a human agent.")
            continue

       
        collect_feedback(user_query, response)

if __name__ == "__main__":
    start_ai_ebpl("john_doe")