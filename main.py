print 'Hello!'
name=raw_input('Enter your name') #name taken as input from user
if len(name) > 2: #checking for length of string
    print " welcome " + name + " \n Glad to have with us. " #concatenating strings
    salutation = raw_input('What should we call you(Mr. or Ms.) ')
    print salutation + " " + name
    if salutation == "Mr." or salutation == "Ms.":  # condition for checking input salutation
        spy_name=salutation+" "+name
        print " alright " + spy_name + " I\'d like to know little more about you......"
        age=input('what\'s your age')
        if 55<=age<=12: #nested if to check range of age
            print 'You are not eligible to be a spy'
        else:
            rating=input('enter your ratings ')
            if rating>5:
                print 'Great Spy!!!'
            elif rating>3.5: #elif is used for more than one condition
                print ' Average Spy '
            elif rating>2.5:
                print ' Need To Work Hard !!! '
            else:
                print ' Who Hired You...Get Out !!! '
            spy_is_online =True
            print 'Authentication complete. Welcome ' + spy_name + ' age: ' + str(age) + ' ratings: ' + str(rating)

    else:
        print ' Enter a valid salutation '
elif name.isspace(): #to check for space
    print ' Please enter a valid name. '

else:
    print "a spy need to have a valid name. Try again please "