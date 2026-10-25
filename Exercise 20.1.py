
flashcards = {
    "Apple": "A fruit",
    "Computer": "An electronic machine",
    "Brave": "Showing courage",
    "Happy": "Feeling joy"
}

score = 0

for word, definition in flashcards.items():
    print("\nWord:", word)
    answer = input("Enter its definition: ")

    if answer.strip().lower() == definition.lower():
        print("Correct answer!")
        score += 1
    else:
        print("Wrong answer!")
        print("Correct definition:", definition)

print("\nFinal Score:", score, "/", len(flashcards))

accuracy = (score / len(flashcards)) * 100
print("Accuracy:", accuracy, "%")
