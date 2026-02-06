score = 0
print("""Weclome to a mental health quiz game. 
Answer the following questions to the best of your ability.
Lets distinguish the facts from the myth""")

question1 = input("True or False: Mental health is just as important as physical health. (True/False): ")
if question1 == "True":
    print("Correct")
    score += 1
else:
    print("Incorrect")
question2 = input("True or False: Mental health is only for people who are diagnosed with a mental illness. (True/False): ")  
if question2 == "False":
    print("Correct")
    score += 1
else:
    print("Incorrect")
question3 = input("True or False: Mental health can affect your physical health. (True/False): ")
if question3 == "True":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    
print(f"You got {score} out of 3 correct")