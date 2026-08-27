def scan_email(text):
    characters = ['@', '.', '!']

    print("\n--- Email Scanner Results ---")

    total = 0

    for char in characters:
        count = text.count(char)
        print(f"'{char}' occurred {count} time(s)")
        total += count

    print(f"\nTotal special characters: {total}")


email_text = input("Enter your email/text:\n")

scan_email(email_text)
