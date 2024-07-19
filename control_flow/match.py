day = input("Enter the day: ").lower()

match day:
    case "monday":
        print("Smile for new work day")
    case "tuesday" | "wednsday" | "thursday" | "friday":
        print("Thank for having another working day")
    case "friday":
        print("Hang out ")
    case "sunday":
        print("Chill")
    case _:
        print("Invalid day")
