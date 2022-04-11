
student_heights = input("Enter student's height separated by space: ").split(" ")

print(student_heights)

count=0
total_height=0

for height in student_heights:
    total_height+=int(height)
    count+=1

avg_height=round(total_height/count,2)

print("Average height of everyone is: "+str(avg_height))
