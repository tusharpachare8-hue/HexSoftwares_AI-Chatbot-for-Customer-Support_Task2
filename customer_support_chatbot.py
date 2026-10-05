# AI Chatbot for Customer Support
# Task 2 - Hex Softwares AI Internship
# Made by Tushar Prakash Pachare

import re
import difflib

company_name = "ShopEasy"

# this is how much a word has to match to count as a "typo match"
fuzzy_cutoff = 0.8
min_word_len_for_fuzzy = 4

# all the intents (questions) the bot can answer
# each one has some keywords and a reply
intents = [
    {
        "name": "greeting",
        "keywords": ["hi", "hello", "hey", "namaste", "greetings"],
        "reply": "Hello! Welcome to " + company_name + " support. How can I help you today?",
    },
    {
        "name": "return_refund",
        "keywords": ["return", "refund", "exchange", "replace", "replacement", "cancel"],
        "reply": "We offer a 7-day return policy on most items. Go to 'My Orders', choose the item "
                 "and click 'Return'. Refunds are processed within 5-7 working days.",
    },
    {
        "name": "order_status",
        "keywords": ["order", "track", "tracking", "status", "package", "parcel"],
        "reply": "You can track your order from 'My Orders' in your account using your order ID. "
                 "You will also get tracking updates by SMS and email.",
    },
    {
        "name": "delivery_time",
        "keywords": ["delivery", "deliver", "shipping", "ship", "arrive", "dispatch"],
        "reply": "Standard delivery takes 3-5 working days. Express delivery takes 1-2 working days "
                 "in select cities.",
    },
    {
        "name": "payment",
        "keywords": ["payment", "pay", "upi", "card", "cod", "cash", "netbanking"],
        "reply": "We accept UPI, debit/credit cards, net banking and Cash on Delivery.",
    },
    {
        "name": "working_hours",
        "keywords": ["hours", "open", "timing", "timings", "close", "closing", "working"],
        "reply": "Our customer support is available Monday to Saturday, 9:00 AM to 6:00 PM.",
    },
    {
        "name": "contact_support",
        "keywords": ["contact", "call", "phone", "email", "human", "agent", "complaint", "help"],
        "reply": "You can reach our support team at support@shopeasy.example or call 1800-000-000 "
                 "(toll-free) during working hours.",
    },
    {
        "name": "thanks",
        "keywords": ["thanks", "thank", "thankyou", "thx"],
        "reply": "You're welcome! Is there anything else I can help you with?",
    },
    {
        "name": "goodbye",
        "keywords": ["bye", "goodbye", "exit", "quit", "later"],
        "reply": "Thank you for contacting us. Have a great day!",
    },
]

fallback_reply = ("Sorry, I didn't understand that. You can ask me about orders, returns and "
                   "refunds, delivery, payments, working hours, or contacting support.")


def clean_text(text):
    # lowercase everything and remove punctuation, then split into words
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text.split()


def is_keyword_match(word, keyword_list):
    # exact match first
    if word in keyword_list:
        return True
    # if its a longer word, allow for small typos using difflib
    if len(word) >= min_word_len_for_fuzzy:
        matches = difflib.get_close_matches(word, keyword_list, n=1, cutoff=fuzzy_cutoff)
        if len(matches) > 0:
            return True
    return False


def get_bot_reply(user_message):
    words = clean_text(user_message)

    if len(words) == 0:
        return "Please type a message so I can help you."

    # check every intent and count how many keywords matched
    best_match = None
    best_count = 0

    for intent in intents:
        count = 0
        for word in words:
            if is_keyword_match(word, intent["keywords"]):
                count = count + 1
        if count > best_count:
            best_count = count
            best_match = intent

    if best_match is None:
        return fallback_reply

    return best_match["reply"]


def print_banner():
    print("=" * 50)
    print(f"      {company_name.upper()} CUSTOMER SUPPORT CHATBOT")
    print("=" * 50)
    print("Ask me about orders, returns, delivery, payments,")
    print("working hours, or contacting support.")
    print("Type 'exit' anytime to quit.\n")


def main():
    print_banner()
    print(f"Bot: Hi! I'm the {company_name} support assistant. How can I help you today?\n")

    while True:
        user_message = input("You: ").strip()

        if user_message.lower() == "exit":
            print("\nBot: Thank you for contacting us. Have a great day!")
            break

        if user_message == "":
            print("Bot: Please type a message so I can help you.\n")
            continue

        reply = get_bot_reply(user_message)
        print(f"Bot: {reply}\n")


if __name__ == "__main__":
    main()