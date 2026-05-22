import pandas as pd
import time
from textblob import TextBlob
from colorama import init, Fore
try: df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Error: The file 'imdb_top_1000.csv' was not found."); raise SystemExit
genre = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs})
def dots():
    for _ in range(3): print(Fore.YELLOW + ".", end="", flush=True); time.sleep(0.5)
def senti(p): return "Positive 😊" if p > 0 else "Negative 😞" if p < 0 else "Neutral 😐"
def recommend(genre=None , mood=None , rating=None , n=5):
    d = df
    if genre: d = d[d["Genre"].str.contains(genre, case=False, na=False)]
    if rating is not None: d = d[d["IMDB_Rating"] >= rating]
    if d.empty: return "No suitable movie recommendations found."
    d, need_nonneg, out = d.sample(frac=1).reset_index(drop=True), bool(mood), []
    for _, r in d.iterrows():
        ov = r.get("Overview")
        if pd.isna(ov): continue
        pol = TextBlob(ov).sentiment.polarity
        if (not need_nonneg) or pol >= 0:
            out.append((r["Series_Title"], pol))
            if len(out) == n: break
    return out if out else "No suitable movie recommendations found."
def show(recs , name):
    print(Fore.YELLOW + f"\n🍿 AI-Analyzed Movie Recommendations for {name}:")
    for i, (t, p) in enumerate(recs, 1):
        print(f"{Fore.CYAN}{i}. 🎥 {t} (Polarity: {p:.2f}, {senti(p)})")
def get_genre():
    print(Fore.GREEN + "Available Genres: ", end="")
    for i, g in enumerate(genre, 1): print(f"{Fore.CYAN}{i}. {g}")
    print()
    while True:
        x = input(Fore.YELLOW + "Enter genre number or name: ").strip()
        if x.isdigit() and 1 <= int(x) <= len(genre): return genre[int(x) - 1]
        x = x.title()
        if x in genre: return x
        print(Fore.RED + "Invalid input. Try again.\n")
def get_rating():
    while True:
        x = input(Fore.YELLOW + "Enter minimum IMDB rating (7.6-9.3) or 'skip': ").strip()
        if x.lower() == "skip": return None
        try:
            r = float(x)
            if 7.6 <= r <= 9.3: return r
            print(Fore.RED + "Rating out of range. Try again.\n")
        except ValueError:
            print(Fore.RED + "Invalid input. Try again.\n")
print(Fore.BLUE + "🎥 Welcome to your Personal Movie Recommendation Assistant! 🎥")
name = input(Fore.YELLOW + "What's your name? ").strip() or "Movie Lover"
print(Fore.GREEN + f"\nHi {name}! Let's find some great movies for you.")
dots()
g = get_genre()
r = get_rating()
mood = input(Fore.YELLOW + "Do you want only movies with a positive vibe? (yes/no): ").strip().lower() == "yes"
print(Fore.GREEN + "\nFinding the best movies for you", end="")
dots()
quick_recs = recommend(genre=g, mood=mood, rating=r)
if isinstance(quick_recs, str):
    print(Fore.red + "\n" + quick_recs)
else:
    show(quick_recs, name)
while True:
    more = input(Fore.YELLOW + "\nWould you like more recommendations? (yes/no): ").strip().lower()
    if more != "yes": break
    print(Fore.GREEN + "\nFinding more movies for you", end="")
    dots()
    recs = recommend(genre=g, mood=mood, rating=r)
    if isinstance(recs, str):
        print(Fore.RED + "\n" + recs)
        break
    show(recs, name)
print(Fore.BLUE + "\nThanks for using the Movie Recommendation Assistant! Enjoy your movies! 🎬🍿\n")