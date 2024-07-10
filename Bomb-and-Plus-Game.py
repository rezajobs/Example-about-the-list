bomb_plus_list = ["Bomb", "+", "+", "Bomb", "+", "+", "Bomb", "+"]

print("Initial list:", bomb_plus_list)

while True:
    try:
        position = int(input("Enter a position (0 to " + str(len(bomb_plus_list) - 1) + "): "))

        if position < 0 or position >= len(bomb_plus_list):
            print("Invalid position. Try again.")
            continue
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if bomb_plus_list[position] == "+":
        bomb_plus_list[position] = None  # Remove the "+"
        print("Updated list:", bomb_plus_list)
    elif bomb_plus_list[position] == "Bomb":
        print("Bomb! You lose.")
        break

    if "+" not in bomb_plus_list:
        print("Congratulations! You win.")
        break
