import datetime

ages = 0
set_num = 100
year_death = 0
year = 0
user_name = ""

def main():
    name_please()
    age_please()
    whats_date()
    age_sum()

def name_please():
    global user_name
    user_name = input("Please tell me your name: ")

def age_please():
    global ages 
    while True:
        try:
            ages = int(input("Please tell me your age: "))
        except ValueError:
            print("This is not a number. Please enter a valid number")
            continue
        if ages >= 100:
            print("Damn, you old as hell")
            exit()
        else:
#successful input 
            break

def whats_date():
    global year
    date = datetime.date.today()
    year = date.year

def age_sum():
    global ages, set_num, year_death, year, user_name
    year_death = int(set_num) - int(ages) + int(year)

    print("Ok " + user_name, "your age is",ages,"and you will be 100 in the year",year_death)
    
main()
