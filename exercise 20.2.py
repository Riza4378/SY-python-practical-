
questions = [
    ("\nIs data privacy important?", True),
    ("\nCan we share passwords with others?", False),
    ("\nShould companies follow regulations?", True),
    ("\nIs fraud allowed in business?", False),
    ("\nShould customer data be protected?", True)
]

score = 0

print("Compliance Screening Portal")
print("Enter True or False for each question.\n")

for question, correct_answer in questions:
    print(question)
    answer = input("Your answer (True/False): ").strip().lower()

    if answer == str(correct_answer).lower():
        score += 1

accuracy = (score / len(questions)) * 100

print("\nFinal Score:", score, "/", len(questions))
print("Accuracy:", accuracy, "%")

if accuracy >= 80:
    print("Result: PASS")
else:
    print("Result: FAIL")
