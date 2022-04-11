
scores=input("Enter all the scores separated by space: ").split(" ")

high_score=0

for score in scores:
    if int(score) > high_score:
        high_score=int(score)

print("High score is "+ str(high_score))