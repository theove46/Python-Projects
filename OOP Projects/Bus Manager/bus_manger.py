from distutils.log import info
from lib2to3.pgen2 import driver


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Bus:
    def __init__(self, coach, driver, arrival, departure, from_des, to_des):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to_des = to_des 
        self.seat = ["Empty" for i in range (20)]

class Company:
    total_bus = 5
    total_bus_list = []
    def install(self):
        bus_no = int(input("Enter Bus no: "))
        flag = 1
        for bus in self.total_bus_list:
            if bus_no == bus['coach']:
                print("Bus already installed")
        if flag:
            bus_driver = input("Enter driver name: ")
            bus_arrival = input("Enter arrival time: ")
            bus_departure = input("Enter depurture time: ")
            bus_from_des = input("Enter from destination: ")
            bus_to_des = input("Enter to destination: ")
            self.new_bus = Bus(bus_no, bus_driver, bus_arrival,  bus_departure,  bus_from_des, bus_to_des)
            self.total_bus_list.append(vars(self.new_bus))
            print("Bus installed successfully")



class BusCounter(Company):
    user_list = []
    bus_seat = 20
    def reservation(self):
        bus_no = int(input("Enter bus no: "))
        for bus in self.total_bus_list:
            if bus_no == bus['coach']:
                passenger = input("Enter passenger name: ")
                seat_no = int(input("Enter seat no: "))
                if(seat_no-1>self.bus_seat):
                    print("Only 20 seats are available")
                elif bus['seat'][seat_no-1] != "Empty":
                    print("Seat already booked")
                else:
                    bus['seat'][seat_no-1] = passenger
            else:
                print("No bus has available")
                break
        # for bus in self.total_bus_list:
        #     print(bus['seat'])

    def showBusInfo(self):
        bus_no = int(input("Enter bus no: "))
        for bus in self.total_bus_list:
            if bus['coach'] == bus_no:
                print("*"*50)
                print()
                print(f"{' '*10} {'#'*10}10 BUS INFO{'#'*10}")
                print(f"Bus no: {bus_no} \t\tDriver: {bus['driver']}")
                print(f"Arrival: {bus['arrival']} \t\tDeparture: {bus['departure']}")
                print(f"From: {bus['from_des']} \t\tTo: {bus['to_des']}")
                print()
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}.{bus['seat'][a-1]}", end="\t\t")
                        a+=1
                    print("\t", end="")
                    for j in range(2):
                        print(f"{a}.{bus['seat'][a-1]}", end="\t\t")
                        a+=1
                    print()

    def get_user(self):
        return self.user_list

    def create_account(self):
        name = input("Enter your name: ")
        flag = 0
        for user in self.get_user():
            if user.username == name:
                print("Username already exists")
                flag = 1
                break
        if flag == 0:
            password = input("Enter your password: ")
            self.new_user = User(name, password)
            self.user_list.append(vars(self.new_user))

    def available_busses(self):
        if len(self.total_bus_list) == 0:
            print("No busses available")
        else:
            for bus in self.total_bus_list:
                print("*"*50)
                print()
                print(f"{' '*10} {'#'*10}10 BUS INFO{'#'*10}")
                print(f"Bus no: {bus['coach']} \t\tDriver: {bus['driver']}")
                print(f"Arrival: {bus['arrival']} \t\tDeparture: {bus['departure']}")
                print(f"From: {bus['from_des']} \t\tTo: {bus['to_des']}")
                print()
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}.{bus['seat'][a-1]}", end="\t\t")
                        a+=1
                    print("\t", end="")
                    for j in range(2):
                        print(f"{a}.{bus['seat'][a-1]}", end="\t\t")
                        a+=1
                    print()

while True:
    counter =  BusCounter()
    print("1. Create an account. \n2. Login in your account. \n3. Exit. ")
    user_input = int(input("Enter your choice: "))
    if user_input == 3:
        break
    elif user_input == 1:
        counter.create_account()
    elif user_input == 2:
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        isAdmin = False
        flag = 0
        if name == "Admin" and password == "1234":
            isAdmin = True
        if isAdmin == False:
            for user in counter.get_user():
                if user['username'] == name and user['password'] == password:
                    flag = 1
                    break
            if flag:
                while True:
                    print("1. Available busses. \n2. Reservation. \n3. Show Busses info. \n4. Exit")
                    a = int(input("Enter your choice: "))
                    if a == 4:
                        break
                    elif a == 1:
                        counter.available_busses()
                    elif a == 2:
                        counter.reservation()
                    elif a == 3:
                        counter.showBusInfo()
            else:
                print("Invalid user")
        else:
            while True:
                print("1. Install bus. \n2. See available busses. \n3. Show bus. \n4. See total user list. \n5. Exit")
                a = int(input("Enter your choice: "))
                if a == 5:
                    break
                elif a == 1:
                    counter.install()
                elif a == 2:
                    counter.available_busses()
                elif a == 3:
                    counter.showBusInfo()
                elif a == 4:
                    counter.reservation()






# 1. create account -> create_new_account()
# 2. log in account -> user:
#                     1. available busses
#                     2. reservation
#                     3. show bus info

#                     admin:
#                     1. install Bus
#                     2. see available busses
#                     3. see total user list 
# 3. exit 
