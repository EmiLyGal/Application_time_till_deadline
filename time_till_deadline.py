from datetime import datetime

user_input= input("Hey user, enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":") #creating list with strngs from users input


goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y") #class datetime with method strptime - string to time

# calculate how many days from now till deadline
today_date = datetime.today()

time_left = deadline_date - today_date
hours_left = int(time_left.total_seconds()/60/60)

# control flow with if-statements
if time_left.days >1:
    print(f"Dear user! Time remaining for your goal: {goal} are {time_left.days} days.")
elif hours_left <24:
    print(f"Dear user! Time remaining for your goal: {goal} are {hours_left} hours.")
else:
    print(f"Dear user! Deadline for your goal: {goal} past.")
    result =input("""Please state your achieved result by entering\n
    Y (Yes,I have completed my goal) or \n
    N (No,I haven't completed my goal):\n""")
    if result == "Y":
        print("Congratulation for achieving your goals")
    elif result == "N":
        new_goal = print("Maybe next time. Would you like to set up the new goal with time? Y/N?\n")
        if new_goal == "Y":
            new_input= input("Hey user, enter your goal with a deadline separated by colon\n")
            input_list = new_input.split(":") #creating list with strngs from users input
            goal = input_list[0]
            deadline = input_list[1]
            deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
            today_date = datetime.today()
            time_left = deadline_date - today_date
            hours_left = int(time_left.total_seconds()/60/60)
        elif new_goal =="N":
            print("Thank you for using the application")
        else:
            print("Error")
            new_goal = print("Maybe next time. Would you like to set up the new goal with time? Y/N?\n")
    else:
        print("Error")