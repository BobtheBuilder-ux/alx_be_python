# daily_reminder.py

def daily_reminder():
    # Get user input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process task using match case and conditionals
    if time_bound == 'yes':
        print(f"\nReminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    else:
        match priority:
            case 'high':
                print(f"\nNote: '{task}' is a high priority task. Although not time-bound, it is important to complete it soon.")
            case 'medium':
                print(f"\nNote: '{task}' is a medium priority task. Consider completing it in the next few days.")
            case 'low':
                print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
            case _:
                print("\nInvalid priority level entered. Please use high, medium, or low.")

if __name__ == "__main__":
    daily_reminder()
