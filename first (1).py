class Member:
    def __init__(self, name, dob, status, num_children, date_hired, date_resigned,specialist, degree):
        self.name = name
        self.dob = dob
        self.status = status
        self.num_children = num_children
        self.date_hired = date_hired
        self.date_resigned=date_resigned
        self.specialist = specialist
        self.degree = degree
        self.salary = 0

    def update_name(self,new_name):
        self.name=new_name
        return self.name
    
    def update_dob(self,new_dob):
        self.dob=new_dob
        return self.dob

    def update_status(self,new_status):
        self.status=new_status
        return self.status

    def update_numofchildren(self,newnumofchildren):
        self.num_children=newnumofchildren
        return self.num_children

    def update_hiringdate(self,newhiringdate):
        self.date_hired=newhiringdate
        return self.date_hired
    
    def update_degree(self,newdegree):
        self.degree=newdegree
        return self.degree

class Employee(Member):
    def __init__(self, name, dob, status, num_children, date_hired,date_resigned, specialist,degree):
        super().__init__(name, dob, status, num_children, date_hired,date_resigned, specialist,degree)
    
    def compute_salary(self):
        base_salary = 220
        if self.degree == "Diploma":
            base_salary += 50
        elif self.degree == "BSc":
            base_salary += 100
        elif self.degree == "Master":
            base_salary += 120
        elif self.degree == "PhD":
            base_salary += 300
        if self.status == "Married":
            base_salary += 50
        base_salary += min(self.num_children, 3) * 20
        self.salary=base_salary*0.95
        return self.salary

    def update_basesalary(self,newbasesalary):
        base_salary=newbasesalary
        return base_salary
    
class Trainer(Member):
    def __init__(self, name, dob, status, num_children, date_hired,date_resigned, specialist, degree, institution):
        super().__init__(name, dob, status, num_children, date_hired,date_resigned, specialist, degree)
        self.institution = institution
        self.salary = 50
    
    def compute_salary(self):
        return self.salary
    
    def update_salary(self,new):
        self.salary=new
        return self.salary

class Worker(Member):
    def __init__(self, name, dob, status, num_children, date_hired, date_resigned,specialist,degree,hours_worked,rate):
        super().__init__(name, dob, status, num_children, date_hired, date_resigned,specialist,degree)
        self.hours_worked = hours_worked
        self.rate = rate
        
    def compute_salary(self):
        self.salary=self.hours_worked * self.rate
        return self.salary

def upload_data(filepath):
    members = []
    file = open(filepath, "r")
    for line in file:
        l=line.strip().split(",")
        if l[0] == "Employee":
            members.append(Employee(l[1], l[2], l[3], int(l[4]), l[5], l[6], l[7], l[8]))
        elif l[0] == "Worker":
            members.append(Worker(l[1], l[2], l[3], int(l[4]), l[5], l[6], l[7], l[8], int(l[9]), int(l[10])))
        elif l[0] == "Trainer":
            members.append(Trainer(l[1], l[2], l[3], int(l[4]), l[5], l[6], l[7], l[8], l[9]))
    return members
    
def write_data(members,filepath):
    file=open(filepath,'w')
    for member in members:
        if isinstance(member,Employee):
            file.write("Employee,"+member.name+','+member.dob+','+member.status+','+str(member.num_children)+','+member.date_hired+','+member.date_resigned+','+member.specialist+','+member.degree+"\n")
        elif isinstance(member,Worker):
            file.write("Worker,"+member.name+','+member.dob+','+member.status+','+str(member.num_children)+','+member.date_hired+','+member.date_resigned+','+member.specialist+','+member.degree+','+str(member.hours_worked)+','+str(member.rate)+"\n")
        elif isinstance(member,Trainer):
            file.write("Trainer,"+member.name+','+member.dob+','+member.status+','+str(member.num_children)+','+member.date_hired+','+member.date_resigned+','+member.specialist+','+member.degree+','+member.institution+"\n")

def Menu():
    print("1.Sending A Certificate To Trainer's Institution")
    print("2.Adding A Member")
    print("3.Deleting A Member")
    print("4.Searching For A Member")
    print("5.Printing The Employee Name With The Highest Salary")
    print("6.Printing A Financial Report For Members' Salaries")
    print("7.Printing A Categorical Report For All Members")
    print("8.Exit")

def adding_member(members):
    type=input("Please Enter The Type Of Member:")
    n=input("Please Enter The Name:")
    d=input("Plaese Enter The Date Of Birth:")
    s=input("Please Enter The Status:")
    nm=int(input("Please Enter The Number Of Children:"))
    dh=input("Please Enter The Date Of Hire:")
    dr=input("Please Enter The Date Of Resignation In The Form (dd//mm/yyyy)(If Exists):")
    sp=input("Please Enter The Specialist:")
    dg=input("Please Enter The Last Degree:")
    if type=="Employee":
        members.append(Employee(n,d,s,nm,dh,dr,sp,dg))
    elif type=="Worker":
        ho=input("Please Enter Hours Worked:")
        r=input("Please Enter The Hourly Rate:")
        members.append(Worker(n,d,s,nm,dh,dr,sp,dg,ho,r))
    elif type=="Trainer":
        ins=input("Please Enter The Institution Name:")
        members.append(Trainer(n,d,s,nm,dh,dr,sp,dg,ins))

def Deleting_member(members):   
    name=input("Please Enter The Name Of Member That You Want To Delete:")
    for member in members:
        if member.name==name:
            members.remove(member)
            break

def Searching(members):
    name=input("Please Enter The Name Of The Member You Want To Search For(With The First Letter Of The First And Last Name Capitalized):")
    for member in members:
        if name==member.name:
            print("Name:",member.name)
            print("Date Of Birth:",member.dob)
            print("Status:",member.status)
            print("Number Of Children:",member.num_children)
            print("Date Of Hire:",member.date_hired)
            print("Date Of Resignation:",member.date_resigned)
            print("Specilaist:",member.specialist)
            print("Degree:",member.degree)
            if isinstance(member, Worker):
                print("Hours Worked:",member.hours_worked)
                print("Hour Rate:",member.rate)
            elif isinstance(member, Trainer):
                print("Institution:",member.institution)
            break

def Highest_Salary(members):
    highest=0
    for member in members:
        member.compute_salary()
        if member.salary > highest:
            highest=member.salary
            highest_name=member.name
    print("\nThe Employee With The Highest Salry Is :",highest_name,"With Salary=",highest,"JOD\n")

def Financial_Report(members):
    print("Name\t\t\tSalary")
    for member in members:
        member.compute_salary()
        print(member.name,"\t\t",member.salary)

def Categorical_Report(members):
    category=input("Please Enter The Category (Employee,Worker,Trainer):")
    for member in members:
        if isinstance(member, Employee) and category == "Employee":
            print("Name:",member.name,",Date Of Birth:",member.dob,",Status:",member.status,",Number Of Children:",member.num_children,",Date Of Hire:",member.date_hired,",Date Of Resignation:",member.date_resigned,",Specialist:",member.specialist,",Degree:",member.degree)
        elif isinstance(member, Worker) and category == "Worker":
            print("Name:",member.name,",Date Of Birth:",member.dob,",Status:",member.status,",Number Of Children:",member.num_children,",Date Of Hire:",member.date_hired,",Date Of Resignation:",member.date_resigned,",Specialist:",member.specialist,",Degree:",member.degree,",Hours Worked:",member.hours_worked,",Rate:",member.rate)
        elif isinstance(member, Trainer) and category == "Trainer":
            print("Name:",member.name,",Date Of Birth:",member.dob,",Status:",member.status,",Number Of Children:",member.num_children,",Date Of Hire:",member.date_hired,",Date Of Resignation:",member.date_resigned,",Specialist:",member.specialist,",Degree:",member.degree,",institution:",member.institution)
            
def main():
    filepath=input("Please Enter File Path:")
    members = upload_data(filepath)
    choice = ""
    print("\n**Note:Any Word The User Enters Should have its First Letter Capitalized**\n ")
    while choice != "8":
        Menu()
        choice = input("\nPlease Enter Your Choice:")
        if choice == "1":
            print("\nA Certificate Will Be Sent To Trainer's Institute.\n")
        elif choice == "2":
            adding_member(members)
        elif choice == "3":
            Deleting_member(members)
        elif choice == "4":
            Searching(members)
        elif choice == "5":
            Highest_Salary(members)
        elif choice == "6":
            Financial_Report(members)
        elif choice == "7":
            Categorical_Report(members)
        elif choice == "8":
            write_data(members,filepath)
            print("Thank You For Using Our Program!")
        else:
            print("Invalid!\n")
main()


m=Trainer()