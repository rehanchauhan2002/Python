class gets:
    name = ""
    emid = ""
    designation = ""
    date = ""
    salary = 0
    ta = 0
    da = 0
    hra = 0
    pf = 0

    def inputs(self,n,e,d,de,s):
        name=n
        emid=e
        designation=d
        date=de
        salary=s
        print("Name : ",name,"\nEmployeeId : ",emid,"\nDesignation : ",designation,"\nDate : ",date,"\nSalary : ",salary)

    def calcy(self,salary):
        ta=salary*0.02
        da=salary*0.05
        hra=salary*0.2
        pf=salary*0.18
        total=salary+ta+da+hra-pf
        print("TA : ",ta,"\nDA : ",da,"\nHRA : ",hra,"\nPF : ",pf,"\nTotal Salary : ",total)

class display(gets):
    def show(self,salary):
        self.calcy(salary)
note=int(input("Enter No. Of Input : "))
for i in range(note):
    name=input("Enter Name : ")
    emid=int(input("Enter EmployeeId : "))
    designation=input("Enter Designation : ")
    date=(input("Enter Date: "))
    salary=int(input("Enter Salary : "))
    op1=display()
    op1.inputs(name,emid,designation,date,salary)
    op1.show(salary)