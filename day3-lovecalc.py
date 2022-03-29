
name1 = input("Enter your name1: ").lower()

name2 = input("Enter your name2: ").lower()

t_count=name1.count('t')
t_count+=name2.count('t')

r_count=name1.count('r')
r_count+=name2.count('r')

u_count=name1.count('u')
u_count+=name2.count('u')

e_count=name1.count('e')
e_count+=name2.count('e')


l_count=name1.count('l')
l_count+=name2.count('l')

o_count=name1.count('o')
o_count+=name2.count('o')

v_count=name1.count('v')
v_count+=name2.count('v')

E_count=name1.count('e')
E_count+=name2.count('e')

true_count=str(t_count+r_count+u_count+e_count)

love_count=str(l_count+o_count+v_count+E_count)

love_percent=int(true_count+love_count)

if love_percent<10 and love_percent>90:
    print("you go together like coke and mentos")
elif love_percent>=40 and love_percent<=50:
    print("you go alright together")
else:
    print(f"your score is {love_percent}%")


