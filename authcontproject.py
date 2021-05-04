#register
#-first name, last name, password, email
#-generate useraccount

#login
#-account number and password

#bank operation

#initialization process
import random

database = {} #dictonary

def init():
    isValidOptionSelected =False
    print ('welcome to bankphp')
    
    while isValidOptionSelected ==False:
        
        haveaccount = int(input('do you have an account with us: 1 (yes) 2 (no) \n'))
        
        if (haveaccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveaccount == 2):
            isValidOptionSelected = True
            #register()
            print(register())
        else:
            print('you have selected invalid option')

def login():
    print ('login to your account')
    accountnumber =input('insert your account number \n')
    password = input('input your password \n')
    


    bankoperation()

def register():
    print('***Register***')
    email = input('what is your email address? \n')
    first_name = input('what is your first name? \n')
    last_name = input('what is your last name? \n')
    password= input('create a password for yourself \n')

    accountnumber = generationaccountnumber()

    database[accountnumber] = [ first_name, last_name, email, password ]

    print('Your account has been created')

    return database
    login()

def bankoperation():
    print('1. withdrawal')
    print('2. deposit')
    print('3. transfers')
    print('4. careers')

def generationaccountnumber():
    
    print('generating account number')
    return random.randrange(1111111111,9999999999)
    print(generationaccountnumber())

### actual banking system ###


init()
