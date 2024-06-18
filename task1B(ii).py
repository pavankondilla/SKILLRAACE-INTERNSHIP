def flames_count(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    total_chars = len(name1) + len(name2)

    common_chars = 0
    for char in name1:
        if char in name2:
            common_chars += 1

    remaining_chars = total_chars - (2 * common_chars)

    relationships = ["Friends", "Love", "Affection", "Marriage", "Enemies", "Siblings"]
    flames_index = remaining_chars % len(relationships) - 1

    return relationships[flames_index]

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
relationship = flames_count(name1, name2)
print(f"The relationship between {name1} and {name2} is: {relationship}")
