#Tip for a meal
print('Please enter a bill amount')
billtotal = float(input())
taxadd = float('%.2f'%(billtotal*0.18))
print("Recommended tip amount is ${}".format(taxadd))
