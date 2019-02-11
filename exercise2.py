#Tip for a meal
print('Please enter a bill amount')
billtotal = float(input())
taxadd = float('%.2f'%(billtotal*0.18))
print("Recommended tip amount is ${}".format(taxadd))

#notes
# variable assignment is line by line, if two variables are equated, the second variable will adopt the value of the first forever regardless of changes to the first variable in the future. In this situation the only way to change the second variable would be to directly equate it to something else
