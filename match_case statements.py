#Match-case statements(switch)

def day_of_the_week(day):
    match day:
        case 1:
            return "It is Sunday."
        case 2:
            return "It is Monday."
        case 3:
            return "It is Tuesday."
        case 4:
            return "It is Wednesday."
        case 5:
            return "It is Thursday."
        case 6:
            return "It is Friday."
        case 7:
            return "It is Saturday."
        case _:
            return "Not a valid day"

def weekend_day(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return  False
        case _:
            return False

print(day_of_the_week(2))
print(weekend_day("Saturday"))





