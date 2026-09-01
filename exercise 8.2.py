feedback = input("Enter your feedback: ")

target_words = ["bad", "stupid", "hate"]

for word in target_words:
    feedback = feedback.replace(word, "****")

print("Moderated feedback:", feedback)
