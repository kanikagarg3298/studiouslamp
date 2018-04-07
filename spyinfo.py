class friend:


    def _init_(self, name, salutation, age, ratings):
        self.spyname = salutation+" "+name
        self.spyage = age
        self.spyratings = ratings
        self.is_online = True
        self.chats = []
        self.current_status = None


    def read(self):
        self.spyname = raw_intput("Enter your name :")
        self.spyage =  input("Enter your age :")
        self.spyratings = input("Enter your ratings :")
        self.is_online = True

    def display(self):
        print "Name: ",self.spyname
        print "Age: ",self.spyage
        print "Ratings: ",self.spyratings
        print "Online status: ",self.is_online
c1 = Spy('',0,0.0,True,[])
c1.read()
c1.display()
