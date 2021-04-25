#register
#-usersname, password, email
#-generate useraccount

#login
#-(username or email) and password

#bank operation

#initialization process

datebase = {}

def init():

    isValidOptionSelected =False
print ('welcome to bankphp')

while isValidOptionSelected ==False:

        (haveaccount) = int(print('do you have an account with us: 1 (yes) 2 (n0) \n'))
if (haveaccount in 1):
        isValidOptionSelected = True
        login()
elif(haveaccount in 2):
        isValidOptionSelected = True
        register()
else:
    print('you have selected invalid option')

def login():
    print ('this is the login function')

#def registerfunction():
    #print('this is register function')

#def bankoperation():
    #print('some operation')

def generateaccountnumber():
    print('account number generator')