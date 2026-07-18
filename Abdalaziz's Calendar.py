import calendar, datetime
print("Welcone To Abdalaziz's Calendar".center(70, "*"),"\n")
current = datetime.datetime.now().date()
current_year = int(current.strftime("%Y")) # current.year
current_month = int(current.strftime("%m")) # current.month

print(f"Today's date is : {current.strftime('%A')}, {current} \n")
print(calendar.month(current_year, current_month))
print("Jump To Date".center(70, "*"),"\n")

while True : 
    try : 
        given_year = int(input("Enter The Year, Month and Day In Order : "))
        given_month = int(input("The Month : "))
        given_day = int(input("The Day : "))
        given = datetime.datetime(given_year, given_month, given_day).date()
        break

    except ValueError : 
        print("Invalid Date, Try Again")

if given == datetime.datetime(2001, 11, 24).date() : 
    print("\nIt's Abdalaziz's Birthday Himself")

if current > given : 
    print(f"\n{(current - given).days} Days Have Passed Since That Day \n")
elif current < given : 
    print(f"\n{(given - current).days} Days Remain Until That Day\n")
else : 
    print("\nYou Have Already Entered The Date Of Today\n")

print(calendar.month(given_year, given_month))
