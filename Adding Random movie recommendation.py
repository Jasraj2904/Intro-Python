import pandas as pd
import random
import time
from textblob import TextBlob
from colorama import init, Fore
init(autoreset=True)
try:
    df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Error: imdb_top_1000.csv file not found.")
    raise SystemExit
genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs})
def loading():
    for _ in range(3):
        print(Fore.YELLOW + "🤖 AI is analyzing movies...", end="\r")
        time.sleep(0.8)
def sentiment(p):
    if p > 0:
        return "Positive 😊"
    elif p < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"
def ai_recommend(genre=None, rating=None, mood=None, n=5):
    data = df
    if genre:
        data = data[data["Genre"].str.contains(genre, case=False, na=False)]
    if rating:
        data = data[data["IMDB_Rating"] >= rating]
    if data.empty:
        return []
    data = data.sample(frac=1).reset_index(drop=True)
    recs = []
    for _, row in data.iterrows():
        overview = str(row["Overview"])
        polarity = TextBlob(overview).sentiment.polarity
        if mood == "happy" and polarity < 0:
            continue
        if mood == "dark" and polarity > 0:
            continue
        ai_score = round((row["IMDB_Rating"] * 10) + (polarity * 10), 2)
        recs.append({
            "title": row["Series_Title"],
            "genre": row["Genre"],
            "rating": row["IMDB_Rating"],
            "overview": overview,
            "polarity": polarity,
            "ai_score": ai_score
        })
        if len(recs) == n:
            break
    return recs
def random_recommend(n=5):
    data = df.sample(n)
    recs = []
    for _, row in data.iterrows():
        overview = str(row["Overview"])
        polarity = TextBlob(overview).sentiment.polarity
        recs.append({
            "title": row["Series_Title"],
            "genre": row["Genre"],
            "rating": row["IMDB_Rating"],
            "overview": overview,
            "polarity": polarity
        })
    return recs
def display(recs):
    print(Fore.CYAN + "\n🎬 Recommended Movies:\n")
    for i, movie in enumerate(recs, 1):
        print(Fore.YELLOW + f"{i}. 🎥 {movie['title']}")
        print(Fore.GREEN + f"   🎭 Genre : {movie['genre']}")
        print(Fore.MAGENTA + f"   ⭐ IMDB Rating : {movie['rating']}")
        print(Fore.WHITE + f"   📝 Overview : {movie['overview']}")
        print(Fore.BLUE + f"   📊 Sentiment : {sentiment(movie['polarity'])}")
        if "ai_score" in movie:
            print(Fore.RED + f"   🤖 AI Match Score : {movie['ai_score']}%")
        print()
print(Fore.BLUE + "🎬 Welcome to AI Movie Recommendation System 🎬")
name = input(Fore.YELLOW + "\nEnter your name: ").strip()
if name == "":
    name = "Movie Lover"
print(Fore.GREEN + f"\nHello {name}! Choose Recommendation Mode:\n")
print(Fore.CYAN + "1. 🤖 AI Smart Recommendation")
print(Fore.CYAN + "2. 🎲 Random Movie Recommendation")
mode = input(Fore.YELLOW + "\nEnter choice (1/2): ").strip()
loading()
if mode == "1":
    print(Fore.GREEN + "\nAvailable Genres:\n")
    for i, g in enumerate(genres, 1):
        print(Fore.CYAN + f"{i}. {g}")
    genre_input = input(Fore.YELLOW + "\nEnter genre name or skip: ").strip()
    if genre_input.lower() == "skip":
        genre_input = None
    rating_input = input(Fore.YELLOW + "Enter minimum IMDB rating or skip: ").strip()
    if rating_input.lower() == "skip":
        rating_input = None
    else:
        rating_input = float(rating_input)
    mood_input = input(Fore.YELLOW + "Choose mood (happy/dark/skip): ").strip().lower()
    if mood_input == "skip":
        mood_input = None
    print(Fore.GREEN + "\n🤖 AI is finding perfect movies for you...\n")
    loading()
    movies = ai_recommend(
        genre=genre_input,
        rating=rating_input,
        mood=mood_input
    )
    if len(movies) == 0:
        print(Fore.RED + "No matching movies found.")
    else:
        display(movies)
elif mode == "2":
    print(Fore.GREEN + "\n🎲 Finding random blockbuster movies...\n")
    loading()
    movies = random_recommend()
    display(movies)
else:
    print(Fore.RED + "Invalid Choice.")
print(Fore.BLUE + "\n🍿 Thank you for using the AI Movie Recommendation System 🍿")