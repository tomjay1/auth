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
    
    print ('welcome to bankphp')
       
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

    init()

def login():
    print ('*******login********')
    accountnumberfromuser =int(input('insert your account number \n'))
    password = input('input your password \n')
    
    for accountnumber,userdetails in database.items():
        if(accountnumber == accountnumberfromuser):
            if(userdetails[3] == password):
                bankoperation(userdetails)
        
        print("invalid account number")
        login()

    

def register():
    print('***Register***')
    email = input('what is your email address? \n')
    first_name = input('what is your first name? \n')
    last_name = input('what is your last name? \n')
    password= input('create a password for yourself \n')

    accountnumber = generationaccountnumber()

    database[accountnumber] = [ first_name, last_name, email, password ]

    print('Your account has been created')
    print ('your account number is: %d' % accountnumber)
    print ('make sure to keep it safe')
    print ('======== ========= =========== ======')
    #return database
    login()

def bankoperation(user):
    print('welcome %s %s '% (user[0], user[1]))
    selectedoption = int(input('select an option (1)deposit (2)withdrawal (3) logout (4)exit \n'))
    if(selectedoption == 1):
        depositoperation()
    elif(selectedoption == 2):
        withdrawaloperation()
    elif(selectedoption ==3):
        logout()
    elif(selectedoption ==4):
        exit()
    else:
        print('invalid option selected')
    bankoperation(user)

def withdrawaloperation():
    print('withdrawal')

def depositoperation():
    print('deposit operation')

def generationaccountnumber():
    print('generating account number')
    
    return random.randrange(1111111111,9999999999)
    print(generationaccountnumber())

def logout():
    login()

### actual banking system ###


init()
