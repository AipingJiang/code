def translate_to_robot(value):
    if value < 512:
        return "Boop"
    elif value > 512:
        return "Beep"
    else:
        return None

robot_messages = []

while True:
    try:
        value = int(input(""))
        result = translate_to_robot(value)
        if result is None:
            break
        elif result == "Beep":
            robot_messages.append(result)
        elif result == "Boop":
            robot_messages.append(result)
        else:
            print(value)
            robot_messages.extend(robot_messages)  # Print collected "Beep" messages
            robot_messages = []  # Clear the collected "Beep" messages

    except ValueError:
        print("Not robot compliant!")

# Print any remaining "Beep" messages
for message in robot_messages:
    print(message)
