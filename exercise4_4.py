
print("Please enter a number")
num = int(input())
secret_number = 130
diff = abs(num - secret_number)

if num == secret_number:
    print("You win!")
elif diff == 1:
    print("So close!")
else:
    print("Try again")
