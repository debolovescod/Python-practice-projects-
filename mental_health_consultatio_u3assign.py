def get_user_feeling():
    user_input = input("Describe how you are feeling in one secente")
    return user_input.lower()
def provide_advice(feeling):
    if "sad" in feeling or "lonely" in feeling:
        return "Reach out to a friend"
    elif "stressed" in feeling or "anxious" in feeling:
        return "Try a 5 minute prayer session"
    else:
        return "Thank you for reaching out "

def get_stress_level():
    try:
        level = int(input("On a scale of 1-10 how stressed are you: "))
        return level
    except ValueError: 
        print("Warning, this is not a number. setting stress level to 0")
        return 0

while True: 
    feeling_input = get_user_feeling()
    if feeling_input == "exit":
        print("Goodbye take care of yourself")
        break
    else: 
        advice = provide_advice(feeling_input)
        print(f"Advice: {advice}")

    stress = get_stress_level()
    print(f"recorded stress level: {stress}")
    if stress >= 5:
        print("Pleas take a rest")
    print("Thanks for reaching out. re run the program to test more")
    break
    
