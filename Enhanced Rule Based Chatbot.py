import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "Beaches": ["Maldives", "Bora Bora", "Maui"],
    "Mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "Cities": ["Paris", "Tokyo", "New York"]
}

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts!"
]

def normalize_input(user_input):
    return re.sub(r'[^\w\s]', '', user_input).lower()

def recommend():
    print(Fore.CYAN + "TravelBot: What type of destination? (Beaches, Mountains, Cities)")
    user_input = input(Fore.YELLOW + "You: ")
    normalized_input = normalize_input(user_input)

    for category in destinations:
        if category.lower() in normalized_input:
            print(Fore.GREEN + f"TravelBot: Here are some {category} destinations:")
            for place in destinations[category]:
                print(Fore.YELLOW + f"- {place}")
            return

    print(Fore.RED + "TravelBot: Sorry, I don't have that category.")

def tell_joke():
    print(Fore.CYAN + "TravelBot: Here's a joke:")
    print(Fore.YELLOW + random.choice(jokes))

def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))

    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Carry basic medicines.")
    print(Fore.GREEN + "- Check the weather forecast.")

def weather_advice():
    print(Fore.CYAN + "TravelBot: Which type of place? (beach/mountain/city)")
    place = normalize_input(input(Fore.YELLOW + "You: "))

    if "beach" in place:
        print(Fore.GREEN + "TravelBot: Expect warm weather. Carry sunscreen, sunglasses, and light clothes.")
    elif "mountain" in place:
        print(Fore.GREEN + "TravelBot: It can be cold. Pack jackets, boots, and warm layers.")
    elif "city" in place:
        print(Fore.GREEN + "TravelBot: Moderate weather. Wear comfortable clothes and shoes.")
    else:
        print(Fore.RED + "TravelBot: Not sure, but always check forecast before traveling.")

def budget_tips():
    print(Fore.CYAN + "TravelBot: What's your budget? (low/medium/high)")
    budget = normalize_input(input(Fore.YELLOW + "You: "))

    if "low" in budget:
        print(Fore.GREEN + "TravelBot: Use public transport, book hostels, and eat local food.")
    elif "medium" in budget:
        print(Fore.GREEN + "TravelBot: Choose budget hotels and plan activities wisely.")
    elif "high" in budget:
        print(Fore.GREEN + "TravelBot: Enjoy luxury stays, guided tours, and premium experiences.")
    else:
        print(Fore.RED + "TravelBot: I couldn't understand your budget.")

def random_destination():
    category = random.choice(list(destinations.keys()))
    place = random.choice(destinations[category])
    print(Fore.CYAN + "TravelBot: Feeling adventurous?")
    print(Fore.GREEN + f"TravelBot: Try visiting {place} ({category})!")

def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommend')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Give weather advice (say 'weather')")
    print(Fore.GREEN + "- Give budget tips (say 'budget')")
    print(Fore.GREEN + "- Pick random destination (say 'random')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot ✈️")
    name = input(Fore.YELLOW + "Your name? ")

    print(Fore.GREEN + f"Nice to meet you, {name}!")
    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input:
            packing_tips()
        elif "weather" in user_input:
            weather_advice()
        elif "budget" in user_input:
            budget_tips()
        elif "random" in user_input:
            random_destination()
        elif "joke" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")

if __name__ == "__main__":
    chat()