from spydetails import spy, Spy, Chats  #  importing class from spydetails.py
from steganography.steganography import Steganography  #  importing Steganography library
from datetime import datetime  #  importing datetime library
import csv  #  importing csv
from colorama import Fore  #  importing Fore from colorama for color
friends = []  #  list to load friends
messages = []  #list to load chats
old_status = ["I spy","Watching Movies","battery about to die","Spy plots are hard,really hard"]  #  list of old status


def load_frnds():  #  Function to load friends
    with open("friends.csv", "rb") as friend_data:  #opening file friends.csv
        reader = list(csv.reader(friend_data))  #  reading from file
        for row in reader[1:]:
            frnd = Spy(name=row[0], salutation=row[1], age =row[2], ratings =[3])
            friends.append(frnd)  #  appending in the friend list


def load_chats():
    with open("chats.csv", "rb") as chats:  #opening file chats.csv
        reader = list(csv.reader(chats))  #  reading from file
        for row in reader[1:]:
            chat = Chats(time=row[0], sender=row[1], message=row[2], receiver=[3])
            messages.append(chat)  #  Appending the chats in the list messages

load_frnds()  #  loading friends automatically by calling load_frnds()
load_chats()  #  loading chats automatically by calling load_chats()


def login():
    username =raw_input("Enter your username: ")  #  taking username as input
    password = raw_input("Enter your password: ")  #  taking password as input
    with open ("login.csv","rb") as login:  #  opening login.csv file
        reader = csv.reader(login)  #  Reading from file
        for row in reader:
            row = list(reader)  #  typecasting to list
            c = 0
            for i in range(0, len(row)):  #  travelling the list
                name = row[i][0]
                pswd = row[i][1]
                sal = row[i][2]
                age = row[i][3]
                rating = row[i][4]
                if name == username:  #  #  checking for correct username
                    if password == pswd:  #  checking for correct password
                        spy_name = sal+" "+name
                        print  'Welcome !! ' + name + "Your age is " + str(age) + ' and your rating is ' + str(rating)
                        spy_chat(name, age, rating)  #  calling spy_chat
                        break
                    else:
                        c=1  # if username is incorrect c=1
                else:
                     c=2   # if username is incorrect c=2
                i=i+1
            if c == 1:
                print "Invalid username"
            elif c == 2:
                print "Invaild password"


def show_frnds():  #  function to show list of friends
    serial_no = 1
    for frnd in friends:
        print str(serial_no)+". "+frnd.name
        serial_no = serial_no+1


def select_frnd():  #  function to select a friend
    show_frnds()  #  calling show_frnds()
    print "Select your friend"
    user_selected_frnd = input("Enter your choice: ")  #  user selecting friend
    user_selected_frnd_index = user_selected_frnd-1
    return user_selected_frnd_index  #  to return the selected friend index


def send_message(spy):  #  function for sending message
        selected_friend = select_frnd()  #  calling the select_friend function
        receiver = friends[selected_friend].name
        original_image = raw_input("What is the name of original image : ")  #  take name of original image as input
        secret_text = raw_input("Enter your secret message : ")  #  entering the secret message
        output_path = "output.jpg"  #  name of image after encoding the message
        Steganography.encode(original_image, output_path, secret_text)  #  calling encode() function to encode message in image
        print "Message Encoded"
        special_msg = ["kaise ho dost","lol", "Mrinali here","hello", "Save"]
        message= secret_text.upper()
        sp = message.spilt(" ")
        for word in sp:
            for i in special_msg:
                if word.upper()  == i:
                    print Fore.RED + "You have send an emergency message \n"
                    print Fore.BLACK
        time = datetime.now()
        with open('chats.csv', 'ab')as chats:
            writer = csv.writer(chats)
            writer.writerow([time, spy,secret_text, receiver])
        print "Your secret message is ready"

def read_message():  #  function for reading message
    selected_friend = select_frnd()  #  calling select_friend function
    output_path = raw_input("Which image you want to decode? ")  #  the name of image to be decoded
    secret_text = Steganography.decode(output_path)  #  calling decode() function to decode
    print "The decoded message is "+secret_text  #  printing the secret text
    #  class to store details of message
    new_chat = Chats(secret_text,False)
    friends[selected_friend]['chats'],append(new_chat)


def chat_history():
    selected_friend = select_frnd()
    choice = friends[selected_friend].name
    for i in messages:
                if choice == i.receiver:
                    print Fore.BLUE + "Time: " + i.time
                    print Fore.RED + "Receiver: " + i.receiver
                    print Fore.BLUE + "Message: " + i.msg


def add_friend():  #  function to add friend
    #  taking friend detail as input
    frnd = Spy("","",0,0.0)  #  class for details of friend
    frnd.name = raw_input("What is your friend's name :")
    frnd.sal = raw_input("What is your friends salutation")
    frnd.age = input("What is the age :")
    frnd.rating = input("What are the rating :")
    frnd.is_online = True
    if len(frnd.name)>0 and 12<frnd.age<50 and frnd.rating > spy.rating:
        #  adding the details in the respective lists
        with open('friend.csv','ab')as friend_data:
        writer = csv.writer(friend_data)
        writer.writerow([frnd.sal,frnd.age,frnd.rating,frnd.is_online])
        print "Your frnd is added"
        friends.append(frnd)  #  appending friend details in friend list
    else:
        print "The friend cannot be added "
    return len(friends)  #  retuning length of list friend_name


def add_status(c_status):  # function to add status
    if c_status is not None:  #  checking if the status is none
        print "Your current status is : "+c_status  #  printing the current status
    else:
        print 'You don\'t have any status currently!!'
    existing_status = raw_input("You want to add from old status Y?N?")  #  taking new status from user
    if existing_status.upper() == 'N':
        new_status = raw_input(" Enter your status : ")  #  taking new status as input
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


def spy_chat(name, spy_age, spy_rating):  #  function spy_chat to display menu
    current_status = None
    choice=-1  #  choice variable set to -1
    print 'here are your options ' + name
    while choice != 0:  #  while loop will run until user choose to exit
        print '  MENU  \n 1.Add a status \n 2.Add a friend \n 3.Send a message \n 4.Read a message \n 5.Read chats from a user \n 6. Logout \n 0.Exit'  #  printing menu
        choice = input("ENTER YOUR CHOICE:")  #  taking choice input
        if choice == 1:  #  choice 1
            current_status = add_status(current_status)
            print " Updated status is : "+current_status
        elif choice == 2:  #  choice 2
            friend_no = 1  #  counter to print number of friends
            no_of_friend = add_friend()  #  calling function add_friend to add friends
            print " You have "+str(no_of_friend)+" number of friends "  #  printing number of friends
            for i in friends:  #  printing name of friends
                print str(friend_no)+". "+i.name
                friend_no = friend_no+1
        elif choice == 3:
            send_message()  #  calling send_message() function
        elif choice == 4:
            read_message()  # calling read_message() function
        elif choice == 5:
            print "Will read a user's message!!!...."
        elif choice == 0:  #  exit
            print 'EXIT'
        else:  #  for any invalid input
            print ' Invalid Input '



def signup():
    spy = Spy("","",0,0.0)  #class for spy details
    spy.name = raw_input("Enter your name ")  #  name taken as input from user
    if spy.name.isspace():  #  check for space input
        print ' Enter a valid name '
    elif spy.name.isdigit():
        print ' Enter a valid name '
    elif len(spy.name) > 2:  #  checking for length of string
        print " welcome " + spy.name+" "+" Glad to have with us. "   # concatenating strings
        spy.sal = raw_input("What do we call you (Mr. or Ms. or Mrs.)")
        if spy.sal == "Mr." or spy.sal == "Ms." or spy.sal == "Mrs.":  #  condition for checking input salutation
            spy_name = spy.sal+" "+spy.name
            print " Alright " + spy_name + " I\'d like to know little more about you......"
            spy.age = input('what\'s your age')
            if 55 <= spy.age <= 12:  #  nested if to check range of age
                print 'You are not eligible to be a spy'
            else:
                rating = input('enter your ratings ')
                if spy.rating > 5:
                    print 'Great Spy!!!'
                elif spy.rating > 4:
                    print 'Good Spy...!'
                elif spy.rating > 3.5:   #  elif is used for more than one condition
                    print ' Average Spy '
                elif spy.rating > 2.5:
                    print ' Need To Work Hard !!! '
                else:
                    print ' Who Hired You...Get Out !!! '
                spy_is_online = True
                print 'Authentication complete. Welcome ' + spy.name + ' age: ' + str(spy.age) + ' and your rating is : ' + str(spy.rating)  #  typecasting of integer to string
                spy_chat(spy.name, spy.age, spy.rating)   #  calling function spy_chat

        else:
            print ' Enter a valid salutation '
    else:
        print ' Ooops!!  Please enter a valid name. '


def welcome():
    f = datetime.now()  #  calling function now() from datetime library
    print f.strftime("%b %d %Y %H:%M:%S")
    print "Hello...!!! Welcome to spy chat.."
    print 'Let\'s get started'
    spy_reply = raw_input('Are you a new user? Y/N ')
    if spy_reply.upper()  == 'N':
        login()
    elif spy_reply.upper() =='Y':
                signup()
    else:
        print "Invalid input"

welcome()
