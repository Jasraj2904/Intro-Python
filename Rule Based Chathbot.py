import re ,  random
from colorama import Fore , init
init(autoreset=True)
destinations = {
    "Beaches" : ["Maldives", "Bora Bora", "Maui"],
    "Mountains" : ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "Cities" : ["Paris", "Tokyo", "New York"]
}
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts!"
]
def normalize_input(user_input):
    return re.sub(r'[^\w\s]', '', user_input).lower()
def recommend():
    print(Fore.CYAN + "Chatbot: What type of destination are you interested in? (Beaches, Mountains, Cities)")
    user_input = input("You: ")
    normalized_input = normalize_input(user_input)
    for category in destinations:
        if category.lower() in normalized_input:
            print(Fore.GREEN + f"Chatbot: Here are some {category} destinations you might like:")
            for place in destinations[category]:
                print(Fore.YELLOW + f"- {place}")
            return
    print(Fore.RED + "Chatbot: Sorry, I don't have recommendations for that category.")
    recommend()
def tell_joke():
    print(Fore.CYAN + "Chatbot: Here's a joke for you:")
    print(Fore.YELLOW + random.choice(jokes))
def show_help():
    print(Fore.CYAN + "Chatbot: You can ask for travel recommendations or a joke! Just type 'recommend' or 'joke'.")
print(Fore.CYAN + "Chatbot: Hello! Type 'help' for options or 'bye' to exit.")
while True:
    user_input = input("You: ")
    normalized_input = normalize_input(user_input)
    if "bye" in normalized_input:
        print(Fore.CYAN + "Chatbot: Goodbye!")
        break
    elif "recommend" in normalized_input:
        recommend()
    elif "joke" in normalized_input:
        tell_joke()
    elif "help" in normalized_input:
        show_help()
    else:
        print(Fore.RED + "Chatbot: I didn't understand that. Type 'help' for options.")
if __name__ == "__main__":
    pass
def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")
    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")
    show_help()    
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")
    show_help()
    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)
        
        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")