print("What is your name")
name = input()
print("Hello {}, nice to meet you!".format(name))

secret_pw = "please"
print("What is the password?")
pw_attempt = input()
veracity = (pw_attempt == secret_pw)
print("Thats {}!".format(veracity))

print("How old are you?")
age = int(input())
yearborn = 2019-age
print("You were born in {}".format(yearborn))
