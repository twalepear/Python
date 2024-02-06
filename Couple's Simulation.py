print("This is a couple's simulation. Type 'help' for question options available.")
input_command = ""
question_mode = False

while True:
    input_command = input(">").lower()
    if input_command == "help":
        print("""
work -
eat -
sleep - 
done - no more questions""")
    elif input_command == "work":

    elif input_command == "eat":

    elif input_command == "sleep":

    elif input_command == "done":
        print("Thank you for running this couple's simulation.")
        break
    else:
        print("We don't have a solution for that yet, please type help to find the available options.")