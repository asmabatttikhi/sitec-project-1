days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
mood = [input(x) for x in days]

count={}
for emotion in mood:
    sum = count.get(emotion ,0)
    count[emotion]= sum+1

percentage={}
total_days= len(days)
for x in count:
    percentage= int(count[x]/total_days*100)
    print(f"{x}:{percentage}%")
