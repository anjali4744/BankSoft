import mymodule
import os
import bank

print('\n\n\t\t\t\t\t\t WELCOME \n\t\t\t\t\t\t TO \n\t\t\t\t BANK MANAGEMENT SYSTEM')
print('\n\t\t CREATED BY: \n\t\t\t ANJALI SINGH \n\t\t\t (XII-PCM)')
input()
os.system('CLS')

x = mymodule.password()
if x:
    mymodule.process()
    os.system('cls')
    bank.start()
else:
    print('\n\t SORRY!!! YOU ARE NOT AUTHORISED USER!!!')









