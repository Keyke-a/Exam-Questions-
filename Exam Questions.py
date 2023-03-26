#preparing exam questions for the ten students in the northern part of Europe
#Assignment
#preparing exam questions for the ten students in the northern part of Europe
student = int(input("Enter number "))#First verification stage
number = 10
exam = 0
limit = 1
if student <= number:
    print("kindly proceed")
    student_name = input("Enter name  ")#Second verification stage
    name = "kike"
    if student_name == name:
        print("Verification completed" "\n" "Kindly proceed")
        while exam < limit:
            Question = input ("What is the capital of Finland? " "\n" "(a) Moscow" "\n" "(b) Helsinki" "\n" "Enter option a or b "  )
            Answer = "b"
            if Question == Answer:
                exam += 1
            Question = input("What is the capital of Sweden? " "\n" "(a) Stockholm" "\n" "(b) Reykjavik" "\n" "Enter option a or b ")
            Answer = "a"
            if Question == Answer:
                exam +=1
            Question = input("What is the capital of Norway? " "\n" "(a) Oslo" "\n" "(b) Moss" "\n" "Enter option a or b ")
            Answer = "a"
            if Question == Answer:
                exam += 1
            Question = input("What is the capital of Denmark ? " "\n" "(a) Rome" "\n" "(b) Copenhagen" "\n" "Enter option a or b ")
            Answer = "b"
            if Question == Answer:
                exam += 1
            Question = input("What is the capital of Estonia? " "\n" "(a) Vilnius" "\n" "(b) Tallinn" "\n" "Enter option a or b ")
            Answer = "b"
            if Question == Answer:
                exam += 1
            Question = input(
                "What is the capital of United Kingdom? " "\n" "(a) London" "\n" "(b) Scotland" "\n" "Enter option a or b ")
            Answer = "a"
            if Question == Answer:
                exam += 1
            print("Dear " + name + "," "\n" "Examination completed" "\n""Your total score is " + str(exam) + "/" "6")
            break
    else:
        print("Incorrect name." "\n" "Kindly retry.")
else:
    print("Examination number is incorrect." "\n" "Kindly retry.")

