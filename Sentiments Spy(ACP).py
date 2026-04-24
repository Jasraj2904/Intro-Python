import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}🤖 Smart Sentiment Chatbot 🤖{Style.RESET_ALL}")

user = input(f"{Fore.MAGENTA}Enter your name: {Style.RESET_ALL}").strip()
if not user:
    user = "Guest"

# Store data
history = []
stats = {"Positive": 0, "Negative": 0, "Neutral": 0}

print(f"\n{Fore.CYAN}Hello {user}! Start typing your sentences.")
print(f"Commands: {Fore.YELLOW}history, stats, reset, exit{Style.RESET_ALL}\n")

while True:
    text = input(f"{Fore.GREEN}>>> {Style.RESET_ALL}").strip()

    if not text:
        print(f"{Fore.RED}Please enter something!{Style.RESET_ALL}")
        continue

    # EXIT + FINAL REPORT
    if text.lower() == "exit":
        print(f"\n{Fore.BLUE}Generating Final Report...{Style.RESET_ALL}")

        total = len(history)
        print(f"\n{Fore.CYAN}--- Final Sentiment Report ---{Style.RESET_ALL}")
        print(f"Total Inputs: {total}")

        for key in stats:
            print(f"{key}: {stats[key]}")

        if total > 0:
            print("\nPercentage:")
            for key in stats:
                percent = (stats[key] / total) * 100
                print(f"{key}: {percent:.2f}%")

        print(f"\n{Fore.BLUE}Goodbye {user}! 👋{Style.RESET_ALL}")
        break

    # RESET
    elif text.lower() == "reset":
        history.clear()
        stats = {"Positive": 0, "Negative": 0, "Neutral": 0}
        print(f"{Fore.CYAN}All data reset successfully!{Style.RESET_ALL}")
        continue

    # HISTORY
    elif text.lower() == "history":
        if not history:
            print(f"{Fore.YELLOW}No history available.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}--- Conversation History ---{Style.RESET_ALL}")
            for i, (msg, pol, sent) in enumerate(history, start=1):
                print(f"{i}. {msg} ({sent}, {pol:.2f})")
        continue

    # STATS COMMAND
    elif text.lower() == "stats":
        print(f"{Fore.CYAN}--- Sentiment Stats ---{Style.RESET_ALL}")
        for key in stats:
            print(f"{key}: {stats[key]}")
        continue

    # SENTIMENT ANALYSIS
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.25:
        sentiment = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment = "Negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    # Store results
    history.append((text, polarity, sentiment))
    stats[sentiment] += 1

    # Output
    print(f"{color}{emoji} {sentiment} sentiment (Score: {polarity:.2f}){Style.RESET_ALL}")