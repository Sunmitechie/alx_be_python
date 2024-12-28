task_desciption = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

message = ""
match priority:
    case "high":
        message = f"{task_desciption} is a high priority task"
    case "medium":
       message = f"{task_desciption} is a medium priority task"
    case "low":
        message = f"{task_desciption} is a low priority task"
    case _:
        print("Invalid priority level.")
        if time_bound == "yes":
            message += "Requires immediate attention today!"
        elif task_time == "no":
            message += "Consider completing it when you have free time."
        else:
            print("Invalid time-bound input.")
print(f"\nReminder:", message)
