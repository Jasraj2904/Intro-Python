import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Start color support
colorama.init()

print(f"{Fore.CYAN}🔎 Sentiment Analyzer Started 🔎{Style.RESET_ALL}")

name = input(f"{Fore.MAGENTA}Enter your name: {Style.RESET_ALL}").strip()
if name == "":
    name = "Agent X"

# List to store user inputs and results
history_data = []

print(f"\n{Fore.CYAN}Welcome, {name}!")
print("Type anything and I will detect its sentiment.")
print(f"Commands: {Fore.YELLOW}reset{Fore.CYAN}, {Fore.YELLOW}history{Fore.CYAN}, {Fore.YELLOW}exit{Style.RESET_ALL}\n")

while True:
    text = input(f"{Fore.GREEN}>>> {Style.RESET_ALL}").strip()

    if text == "":
        print(f"{Fore.RED}Input cannot be empty!{Style.RESET_ALL}")
        continue

    # Commands handling
    if text.lower() == "exit":
        print(f"{Fore.BLUE}Goodbye {name}! 👋{Style.RESET_ALL}")
        break

    elif text.lower() == "reset":
        history_data = []
        print(f"{Fore.CYAN}History has been cleared!{Style.RESET_ALL}")
        continue

    elif text.lower() == "history":
        if len(history_data) == 0:
            print(f"{Fore.YELLOW}No records yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}--- Previous Analysis ---{Style.RESET_ALL}")
            for i, (msg, pol, senti) in enumerate(history_data, start=1):

                if senti == "Positive":
                    clr = Fore.GREEN
                    emo = "🙂"
                elif senti == "Negative":
                    clr = Fore.RED
                    emo = "🙁"
                else:
                    clr = Fore.YELLOW
                    emo = "😐"

                print(f"{i}. {clr}{emo} {msg} | Score: {pol:.2f} | {senti}{Style.RESET_ALL}")
        continue

    # Sentiment calculation
    score = TextBlob(text).sentiment.polarity

    if score > 0.25:
        senti_type = "Positive"
        clr = Fore.GREEN
        emo = "🙂"
    elif score < -0.25:
        senti_type = "Negative"
        clr = Fore.RED
        emo = "🙁"
    else:
        senti_type = "Neutral"
        clr = Fore.YELLOW
        emo = "😐"

    # Save result
    history_data.append((text, score, senti_type))

    # Output result
    print(f"{clr}{emo} {senti_type} detected (Score: {score:.2f}){Style.RESET_ALL}")