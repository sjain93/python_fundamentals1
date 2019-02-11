
print("Please enter your age")
age = int(input())
my_age = 25
diff = abs(age - my_age)

if age >= 105:
    print("I'm not sure I believe you")
elif diff == 1:
    print("We are {} year apart".format(diff))
else:
    print("We are {} years apart".format(diff))
