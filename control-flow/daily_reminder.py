# daily_reminder.py

def daily_reminder():
    # Get user input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    print()  # Add spacing for better readability
    
    # Customized reminder logic
    if time_bound == 'yes':
        print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    else:
        match priority:
            case 'high':
                print(f"Note: '{task}' is a high priority task. Complete it as soon as possible.")
            case 'medium':
                print(f"Note: '{task}' is a medium priority task. Should be completed this week.")
            case 'low':
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
            case _:
                print("Invalid priority level entered. Please use high, medium, or low.")

if __name__ == "__main__":
    daily_reminder()