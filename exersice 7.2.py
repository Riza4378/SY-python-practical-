def count_python(paragraph):
    count = paragraph.lower().split().count("python")
    print(f"The word 'Python' appears {count} time(s).")


paragraph = input("Enter a paragraph: ")

count_python(paragraph)