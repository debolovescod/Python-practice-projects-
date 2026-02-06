mood_log = []
mood = None
added_score = 0
meaning = None

while mood != "done":
    mood = input("Enter your mood on a scale of 1 - 10: ")
    if mood == "done":
        break 
    mood_log.append(mood)
x = len(mood_log)
for moods in mood_log:
   moods = int(moods) 
   added_score += moods
average_score = added_score/x

mood_meaning = {1: "Struggling", 5: "Neutral", 10: "Excellent"}
if average_score >= 1 and average_score < 5:
    meaning = "struggling"
elif average_score >= 5 and average_score < 10:
    meaning = "neutral"
elif average_score == 10:
    meaning = "excellent"

print(f"Over  {x} days, your average mood was {average_score}. Currently, you are {meaning}."
)
