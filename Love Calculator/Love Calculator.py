def calculate_love_score(name1, name2):
    combined = (name1 + name2).lower()

    true_count = 0
    for letters in "true":
        true_count += combined.count(letters)

    love_count = 0
    for letters in "love":
        love_count += combined.count(letters)

    love_score = int(str(true_count) + str(love_count))
    print(love_score)


calculate_love_score(name1="Miguel Gonzales", name2="Manny Pacquiao")
