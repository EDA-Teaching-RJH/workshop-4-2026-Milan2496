def main():
    
    student_count = int(input("How many students to enter? "))
    
    names = []
    scores = []

    
    for i in range(student_count):
        
        print(f"Student {i + 1}")
        
        
        name_input = str(input("Name: "))
        name_input = name_input.title()
        name_input = name_input.strip()
        names.append(name_input)

        
        while True:
            score_input = int(input("Score: "))
            
            
            if score_input < 0 or score_input > 100:
                print("Invalid score. Must be 0-100.")
                continue
            else:
                break
        
        scores.append(score_input)

    
    print("--- Class Summary ---")
    
   
    for i in range(len(names)):
        if scores[i] < 40:
            result = "Fail"
        else:
            result = "Pass"
        
        print(f"{i + 1}: {names[i]} - {scores[i]} ({result})")


main()
