import getpass
import random
import time
import os
def menu():
    print('1.ADD ACOOUNT HOLDER \n2.DISPLAY RECORD AS PER ACCOUNT NUMBER \n3.DISPLAY RECORD AS PER COSTUMER NAME \n 4.DELETE RECORD OF ACCOUNT HOLDER \n5.UPdATE RECORD \n 6.SEARCH RECORD AS PER ACCOUNT NO. \n7.SEARCH RECORD AS PER COSTUMER NAME \n8.WITHDRAW FROM ACCOUNT \n9.CREDIT INTO ACCOUNT \n10.LOCK SYSTEM \n11.EXIT SYSTEM')



def password():
    print("\n\n\n\n\t\t", end=" ")
    p=getpass.getpass()

    os.system('CLS')

    if p == '123':
        print("\n\n\t\t WELCOME TO THE SYSTEM")

        return True
    else:
        return False

def process():
    x=random.randint(1,2)
    for i in range (0,x):

        print('\n\n\n\n\t\tprocessing.')
        time.sleep(0.25)
        os.system('CLS')
        print('\n\n\n\n\t\tprocessing..')
        time.sleep(0.25)
        os.system('CLS')
        print('\n\n\n\n\t\tprocessing...')
        time.sleep(0.25)
        os.system('CLS')
        print('\n\n\n\n\t\tprocessing...')
        time.sleep(0.25)
        os.system('CLS')
        print('\n\n\n\n\t\tprocessing....')
        time.sleep(0.25)
        os.system('CLS')











