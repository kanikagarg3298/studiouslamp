from spydetails import spy_rating,spy_age,spy_name  #  importing variables from spydetails.py
def spy_chat(spy_name,spy_age,spy_rating):
    choice=-1  #  choice variable set to -1
    print 'here are your options ' + spy_name
    while choice!=0:  #  while loop will run untill user chooose to exit
        print '  MENU  \n 1.Add a status \n 2.Add a friend \n 0.Exit'  #  printing menu
        choice=input("ENTER YOUR CHOICE:")  #  taking choice input
        if choice==1:  #  choice 1
            print ' will add status '
        elif choice==2:  #  choice 2
            print ' will add a spy_friend! '
        elif choice==0:  #  exit
            print 'EXIT'
        else:  #  for any invalid input
            print ' Invalid Input '

print 'Hello....!!!'  #  printing hello
print 'Let\'s get started...'
spy_reply=raw_input('Are You A New User?? Y/N ')  #  taken as user is new or not
if spy_reply.upper()=='N':
    print 'Welcome back!! '+spy_name+' . Your age is '+str(spy_age)+' and your rating is '+ str(spy_rating)
    spy_chat(spy_name,spy_age,spy_rating)   # calling function spy_chat
elif spy_reply.upper()=='Y':
    name=raw_input('Enter your name')  #  name taken as input from user
    if name.isspace():  #  check for space input
        print ' Enter a valid name '
    elif name.isdigit():
        print ' Enter a valid name '
    elif len(name) > 2:  #  checking for length of string
        print " welcome " + name + " \n Glad to have with us. "   # concatenating strings
        salutation = raw_input('What should we call you(Mr. or Ms.) ')
        print salutation + " " + name
        if salutation == "Mr." or salutation == "Ms." or salutation == "Mrs." :  # condition for checking input salutation
            spy_name=salutation+" "+name
            print " alright " + spy_name + " I\'d like to know little more about you......"
            age=input('what\'s your age')
            if 55<=age<=12: #nested if to check range of age
                print 'You are not eligible to be a spy'
            else:
                rating=input('enter your ratings ')
                if rating>5:
                    print 'Great Spy!!!'
                elif rating>3.5:   #elif is used for more than one condition
                    print ' Average Spy '
                elif rating>2.5:
                    print ' Need To Work Hard !!! '
                else:
                    print ' Who Hired You...Get Out !!! '
                spy_is_online =True
                print 'Authentication complete. Welcome ' + spy_name + ' age: ' + str(age) + ' and your rating is : ' + str(rating)  #typecasting of integer to string

    else:
        print ' Enter a valid salutation '
        print ' Ooops!!  Please enter a valid name. '

