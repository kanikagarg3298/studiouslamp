from spydetails import spy_rating, spy_age, spy_name  #  importing variables from spydetails.py
from spydetails import spy_rating, spy_age, spy_name, spy_isonline  #  importing variables from spydetails.py


def add_friend():
    frnd_name = raw_input(" What is your friend name : ")  #  taking friend details as input
    frnd_age = input(" what is the age : ")
    frnd_rating = input(" What is the rating : ")
    if len(frnd_name) > 2 and 12 < frnd_age < 50 and frnd_rating > spy_rating:  #  checking for details of spy
        friend_name.append(frnd_name)
        friend_age.append(frnd_age)
        friend_rating.append(frnd_rating)
        friend_isonline.append(True)
    else:
        print "The friend cannot be added "
    return len(friend_name)  #  retuning length of list friend_name


def add_status(c_status):  # function to add status
    if c_status != None:   #  cecking if the status is none
        print "Your current status is : "+c_status
    else:
        print "You don't have any status currently!! "
    existing_status = raw_input("You want to add from old status Y?N?")  #  taking new status from user
    if existing_status.upper() == 'N':
        new_status = raw_input(" enter your status : ")
        if len(new_status)>0:
            updated_status =new_status
            old_status.append(updated_status)  #  adding the new status in the status list
        else:
            print " Enter a valid status "
    elif existing_status.upper() == "Y":  #  checking if user want to add an old status
        serial_no = 1
        for status in old_status:  #  printing the old status
            print str(serial_no)+". "+status
            serial_no = serial_no+1
        status_choice = input(" enter your choice : ")
        updated_status = old_status[status_choice-1]  #  updating the status
    return updated_status  #  returning the new updated status


def spy_chat(spy_name, spy_age, spy_rating):  #  function spy_chat to display menu
    current_status = None
    choice=-1  #  choice variable set to -1
    print 'here are your options ' + spy_name
    while choice != 0:  #  while loop will run untill user chooose to exit
        print '  MENU  \n 1.Add a status \n 2.Add a friend \n 3.Send a message \n 4.Read a message \n 0.Exit'  #  printing menu
        choice = input("ENTER YOUR CHOICE:")  #  taking choice input
        if choice == 1:  #  choice 1
            current_status = add_status(current_status)
            print " Updated status is : "+current_status
        elif choice == 2:  #  choice 2
            friend = 1  #  counter to print number of friends
            no_of_friend = add_friend()  #  calling function add_friend to add friends
            print ' You have "+str(no_of_friend)+" number of friends '  #  printing number of friends
            for i in friend_name:
                print str(friend)+". "+i
                friend=friend+1
        elif choice == 0:  #  exit
            print 'EXIT'
        else:  #  for any invalid input
            print ' Invalid Input '


print 'Hello....!!!'  #  printing hello
print 'Let\'s get started...'
old_status = ["I spy","Watching Movies","battery about to die","Spy plots are hard,really hard"]  #  list of old status
#  lists to store friends details
friend_name = ["Ayush"]
friend_age = [22]
friend_rating = [2.9]
friend_isonline =[True]
spy_reply = raw_input('Are You A New User?? Y/N ')  #  taken as user is new or not
if spy_reply.upper() == 'N':
    print 'Welcome back!! '+spy_name+' . Your age is '+str(spy_age)+' and your rating is '+ str(spy_rating)
    spy_chat(spy_name, spy_age, spy_rating)   # calling function spy_chat
elif spy_reply.upper() == 'Y':
    name = raw_input('Enter your name')  #  name taken as input from user
    if name.isspace():  #  check for space input
        print ' Enter a valid name '
    elif name.isdigit():
        print ' Enter a valid name '
    elif len(name) > 2:  #  checking for length of string
        print " welcome " + name + " \n Glad to have with us. "   # concatenating strings
        salutation = raw_input('What should we call you(Mr. or Ms.) ')
        print salutation + " " + name
        if salutation == "Mr." or salutation == "Ms." or salutation == "Mrs.":  #  condition for checking input salutation
            spy_name = salutation+" "+name
            print " alright " + spy_name + " I\'d like to know little more about you......"
            age = input('what\'s your age')
            if 55 <= age <= 12:  #  nested if to check range of age
                print 'You are not eligible to be a spy'
            else:
                rating = input('enter your ratings ')
                if rating > 5:
                    print 'Great Spy!!!'
                elif rating > 3.5:   #  elif is used for more than one condition
                    print ' Average Spy '
                elif rating > 2.5:
                    print ' Need To Work Hard !!! '
                else:
                    print ' Who Hired You...Get Out !!! '
                spy_is_online = True
                print 'Authentication complete. Welcome ' + spy_name + ' age: ' + str(age) + ' and your rating is : ' + str(rating)  #  typecasting of integer to string

    else:
        print ' Enter a valid salutation '
        print ' Ooops!!  Please enter a valid name. '

