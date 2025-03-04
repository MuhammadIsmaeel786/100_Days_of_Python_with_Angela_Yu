def calculate_love_score(name1,name2):
    word_true = "true"
    love = 'love'
    totalOne = 0
    totalTwo = 0
    combine_name = name1 + name2
    for letter in combine_name.lower():
        if letter in word_true:
            totalOne +=1
    for letter in combine_name.lower():
        if letter in love:
            totalTwo +=1
    print(f"{totalOne}{totalTwo}")
    
calculate_love_score(input("Your Name : "), input("Your Loved one Name : "))