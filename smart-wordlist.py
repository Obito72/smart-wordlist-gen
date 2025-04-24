# smart-wordlist.py
from itertools import permutations

def collect_info():
    print("🔐 Enter target details (leave blank if not known):")
    name = input("Full Name: ")
    birth = input("Birth Year: ")
    pet = input("Pet Name: ")
    company = input("Company Name: ")
    fav = input("Favorite Word/Thing: ")

    base_words = [name, birth, pet, company, fav]
    base_words = [w.lower() for w in base_words if w.strip() != ""]

    return base_words

def generate_combinations(words):
    combos = set()

    # Add single words and common suffixes
    for word in words:
        combos.add(word)
        combos.add(word + "123")
        combos.add(word + "@123")
        combos.add(word + "2024")
        combos.add(word.capitalize())

    # Add 2-word permutations
    for a, b in permutations(words, 2):
        combos.add(a + b)
        combos.add(a + "@" + b)
        combos.add(a + "_" + b)
    
    return combos

def save_to_file(words, filename="wordlist.txt"):
    with open(filename, "w") as f:
        for word in sorted(words):
            f.write(word + "\n")
    print(f"✅ Wordlist saved as: {filename}")

if __name__ == "__main__":
    user_words = collect_info()
    wordlist = generate_combinations(user_words)
    save_to_file(wordlist)
