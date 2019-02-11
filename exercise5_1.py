distance = 0
print("Welcome to VirtEx, how much energy do you have today?- enter a number from 1-10")
energy = int(input())

while True:
    print("Would you like to walk or run?")
    ans = input()
    if ans == "walk":
        distance += 1
        energy += 1
    elif ans == "run":
        if energy == 0:
            print("Unfortunately you don't have the energy for this task")
            continue
        else:
            distance += 5
            energy = energy - 1
    elif ans == "go home":
        break
    else:
        print("Invalid input")
        continue
    print("You have travelled {}km".format(distance))

print("Thanks for playing!")
