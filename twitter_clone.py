import json

class Twitter:
    def __init__(self):
        self.filename = "twits.json"
    def send_twit(self):
        with open(self.filename) as file:
            data = json.load(file)
        user = input("Your name : ")
        twit = input("Your twit : ")
        a = {"user" : user, "twit" : twit}
        data.append(a)
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)
    def get_twits(self):
        with open(self.filename) as file:
            data = json.load(file)
        for twit in data:
            print("Name : {}\nTwit : {}\n--------------------".format(twit["user"], twit["twit"]))
    
twitter_clone = Twitter()

flag = True
while flag:
    option = input("1) Send twit\n2) Get twits\n3)Exit\nChoose one of these options : ")
    if option == "1":
        twitter_clone.send_twit()
    elif option == "2":
        twitter_clone.get_twits()
    elif option == "3":
        flag = False
    else:
        print("This option is not available")