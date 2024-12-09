days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
mood_data = {}


print("Enter your mood for each day of the week:")
for day in days:
    while True:
        mood = input(day + ": ").strip().lower()  
        if mood:
            mood_data[day] = mood
            break
        print("Mood cannot be empty. Please try again.")

mood_count={}
emotions_list=mood_data.values()
for emotion in emotions_list:
    # Get previous counts if there's no value in mood_count means its the first time im getting this value so its default is 0 and will always increase it
    sum_previous=mood_count.get(emotion,0)
    mood_count[emotion]=sum_previous+1


# percentage
total_days = len( mood_data)
for mood in mood_count.keys():
    avg=mood_count.get(mood)/total_days
    by_perc=int((avg)*100)
    mood_count[mood]=f'{by_perc}%'
print (mood_count)

