from datetime import datetime
import uuid

class Task():
    def __init__(self, name):
        self.name = name
        self.created_time = datetime.now()
        self.updated_time = None
        self.completed_time = None
        self.task_done = False
        self.id = uuid.uuid1()

    def update_task(self, up_name):
        self.name = up_name
        self.updated_time = datetime.now()

    def complete_task(self):
        self.task_done = True
        self.completed_time = datetime.now()

    
TaskList = []

while True:
    print("1. Add new task\n2. Show all tasks\n3. Show incompleted tasks\n4. Show completed tasks\n5. Update task\n6. Mark a task completed")
    choice = input("Enter option: ")

    if choice == '1':           # 1. Add new task
        name = input("Enter New Task: ")
        new_obj = Task(name)
        TaskList.append(new_obj)
        print("\nTask Created Successfully\n")


    elif choice == '2':         # 2. Show all tasks
        for i in TaskList:
            print("\n")
            print("ID - ", i.id)
            print("Task - ", i.name)
            print("Created Time - ", i.created_time.strftime("%m/%d/%Y %H:%M:%S"))
            if(i.updated_time==None):
                print("Updated time - NA")
            else:
                print("Updated time - ", i.updated_time.strftime("%m/%d/%Y %H:%M:%S"))
            print("Completed - ", i.task_done)
            if(i.completed_time==None):
                print("Completed time - NA")
            else:
                print("Completed time - ", i.completed_time.strftime("%m/%d/%Y %H:%M:%S"))
        print("\n")


    elif choice== '3':          # 3. Show incompleted tasks
        x = 0
        for i in TaskList:
            if(i.task_done==False):
                x += 1
                print("\n")
                print("ID - ", i.id)
                print("Task - ", i.name)
                print("Created Time - ", i.created_time.strftime("%m/%d/%Y %H:%M:%S"))
                if(i.updated_time==None):
                    print("Updated time - NA")
                else:
                    print("Updated time - ", i.updated_time.strftime("%m/%d/%Y %H:%M:%S"))
                print("Completed - ", i.task_done)
                print("Completed time - NA")
        if(x==0):
            print("\nNo Incompleted Task")
        print("\n")
    

    elif choice == '4':         # 4. Show completed tasks
        x = 0
        for i in TaskList:
            if(i.task_done==True):
                x += 1
                print("\n")
                print("ID - ", i.id)
                print("Task - ", i.name)
                print("Created Time - ", i.created_time.strftime("%m/%d/%Y %H:%M:%S"))
                if(i.updated_time==None):
                    print("Updated time - NA")
                else:
                    print("Updated time - ", i.updated_time.strftime("%m/%d/%Y %H:%M:%S"))
                print("Completed - ", i.task_done)
                print("Completed time - ", i.completed_time.strftime("%m/%d/%Y %H:%M:%S"))
        if(x==0):
            print("\nNo Completed Task")
        print("\n")


    elif choice == '5':         # 5. Update task
        print("\nSelect Which Task To Update")
        x = 0
        for i in TaskList:
            print("\n")
            print("Task No - ", x+1)
            x+=1
            print("ID - ", i.id)
            print("Task - ", i.name)
            print("Created Time - ", i.created_time.strftime("%m/%d/%Y %H:%M:%S"))
            if(i.updated_time==None):
                print("Updated time - NA")
            else:
                print("Updated time - ", i.updated_time.strftime("%m/%d/%Y %H:%M:%S"))
            print("Completed - ", i.task_done)
            if(i.completed_time==None):
                print("Completed time - NA")
            else:
                print("Completed time - ", i.completed_time.strftime("%m/%d/%Y %H:%M:%S"))
        print("\n")
        ch = int(input("Enter Task No: "))
        x = 1
        for i in TaskList:
            if(x==ch):
                name = input("Enter New Task: ")
                i.update_task(name)
                print("\nTask Updated Successfully\n")
                break
            else:
                x+=1


    elif choice == '6':         # 6. Mark a task completed
        print("\nSelect Which Task To Complete")
        x = 0
        for i in TaskList:
            if(i.task_done==False):
                print("\n")
                print("Task No - ", x+1)
                x+=1
                print("ID - ", i.id)
                print("Task - ", i.name)
                print("Created Time - ", i.created_time.strftime("%m/%d/%Y %H:%M:%S"))
                if(i.updated_time==None):
                    print("Updated time - NA")
                else:
                    print("Updated time - ", i.updated_time.strftime("%m/%d/%Y %H:%M:%S"))
                print("Completed - ", i.task_done)
                if(i.completed_time==None):
                    print("Completed time - NA")
                else:
                    print("Completed time - ", i.completed_time.strftime("%m/%d/%Y %H:%M:%S"))
        print("\n")
        ch = int(input("Enter Task No: "))
        x = 1
        for i in TaskList:
            if(i.task_done==False):
                if(x==ch):
                    i.complete_task()
                    print(x)
                    print("\nTask Completed Successfully\n")
                    break
                else:
                    x+=1
