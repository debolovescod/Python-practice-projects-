class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__mood_history = []  # private list

    def add_mood(self, mood):
        self.__mood_history.append(mood)

    def get_report(self):
        print(f"Patient: {self.name}, Age: {self.age}")
        print("Mood History:")
        for i, mood in enumerate(self.__mood_history, start=1):
            print(f"{i}. {mood}")

# Create patient object
amina = Patient("Amina", 30)

# While loop to collect moods
while True:
    mood = input("Enter Amina's mood (or type 'quit' to stop): ")
    if mood.lower() == "quit":
        break
    amina.add_mood(mood)

# Print report
amina.get_report()
