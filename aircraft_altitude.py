from aircraft import Aircraft
model = input("Enter aircraft model:\n")
aircraft = Aircraft(model)

while True:
    command = input("Enter command (A for ascent, D for descent, X to exit):\n")
    
    if command == "X":
        break
    action, feet = command.split()
    feet = int(feet)

    if action == "A":
        aircraft.ascent(feet)

    elif action == "D":
        aircraft.descent(feet)

print(f"Final altitude: {aircraft.altitude} feet")