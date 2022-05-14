
f_name_title_case=""
l_name_title_case=""

def convert_name_title_case(f_name, l_name):
    f_name_title_case=f_name.title()
    l_name_title_case = l_name.title()
    return f_name_title_case, l_name_title_case;

first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")

f_name_title_case, l_name_title_case = convert_name_title_case(f_name=first_name, l_name=last_name)
print("Provided name is: "+ f_name_title_case +" "+ l_name_title_case)