correct_answers = ["A", "C", "B", "D"]

count = 0

for i in range(len(correct_answers)):
    
    ans = str(input(f"Answer for Question {i+1}: "))

    if ans == correct_answers[i]:
        print("Correct!")
        count = count + 1
    else:
        print("Wrong.")
        

print(f"You got {count} out of 4")


