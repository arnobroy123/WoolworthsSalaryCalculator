time = float(input("Enter Hours: "))

def WeekDays(hours):
        rate1 = hours * 23.7592
        rate2 = hours * 5.9398
        rate3 = hours * 5.9398
        global total1
        total1 = rate1 + rate2 + rate3
        print("This WeekDay salary is: " + str(round(total1, 3)));

def WeekEnds(hours):
        rate1 = hours * 23.7592
        rate2 = hours * 5.9398
        rate3 = hours * 11.8796
        global total2
        total2 = rate1 + rate2 + rate3
        print("This WeekEnd salary is: " + str(round(total2, 3)));

def TotalSalary():
    subtotalSal = total1 + total2
    print("Your Total Salary is: " + str(round(subtotalSal, 3)))

while time is not None:
    if time >= 0 and time <=168:
        Day = input("Please enter W for weekdays and WD for weekend: ").lower()
        if Day == "w":
            WeekDays(time)
            hrs = float(input("Enter weekends hours: "))
            WeekEnds(hrs)
            TotalSalary()
        elif Day == "wd":
            WeekEnds(time)
            hrs = float(input("Enter weekdays hours: "))
            WeekDays(hrs)
            TotalSalary()
        else:
            print("Please enter a valid day")
            continue;
        break;
    else:
        print("Please enter a valid time!!!")
        time = float(input("Enter Hours: "))
        continue;