import pymysql
class employee:
    def __init__(self):
        self.con=pymysql.connect(
        host="localhost",
        user="root",
        password="Arun@2002",
        database="testdb"
)
    def Add(self,eid,ename,edept,esalary):
        q="INSERT INTO employee(id,name,dept,salary)values(%s,%s,%s,%s)"
        c=self.con.cursor()
        res=c.execute(q, (eid,ename,edept,esalary))
        self.con.commit()
        print("Added" if res>=1 else "Not Added")
    def View(self):
        q="SELECT * FROM employee"
        c=self.con.cursor()
        c.execute(q)
        data=c.fetchall()
        for i in data:
            print(i)
    def Update(self,eid,salary):
        q="UPDATE employee SET salary=%s where id=%s"
        c=self.con.cursor()
        res=c.execute(q, (salary,eid))
        self.con.commit()
        print("Updated" if res>=1 else "Not Updated")
    def Remove(self,eid):
        q="DELETE FROM employee WHERE id=%s"
        c=self.con.cursor()
        res=c.execute(q,(eid,))
        self.con.commit()
        print("Removed" if res>=1 else "Not Removed")
    def Search(self,eid):
        q="SEARCH * FROM employee WHERE id=%s"
        c=self.con.cursor()
        res=c.execute(q,(eid,))
        data=c.fetchone()
        if data:
            print(data)
        else:
            print("Employee Not found")
    def SortSalary(self):
        q=SELECT * FROM employee ORDER BY salary DESC;  
        c=self.con.cursor()
        c.execute(q)
        data=fetchall()
        for i in data:
            print(i)
    def DeptFilter(self,dept):
        q="SELECT * FROM employee WHERE dept=%s"
        c=self.con.cursor()
        c.execute(q,(dept,))
        data=fetchall()
        if data:
            for i in data:
                print(i)
        else:
            print("No Employees found")                          


while True:
    option=int(input("1-Add 2-View 3-Update 4-Remove 5-Search 6-SortSalary 7-DeptFilter 8-Exit: "))
    if option==1:
        id=int(input("Enter ID: "))
        un=input("Enter name: ")
        dept=input("Enter dept: ")
        sal=int(input("Enter Salary: "))
        emp=employee()
        emp.Add(id,un,dept,sal)
    elif option==2:
        emp=employee()
        emp.View()
    elif option==3:
        id=int(input("Enter Employee ID: "))
        sal=int(input("Enter new salary: "))
        emp=employee()
        emp.Update(id,sal)
    elif option==4:
        id=int(input("Enter Employee ID: "))
        emp=employee()
        emp.Remove(id)
    elif option==5:
        id=int(input("Enter Employee ID: "))
        emp=employee()
        emp.Search(id)
    elif option==6:
        emp=employee()
        emp.SortSalary()
    elif option==7:
        dept=input("Enter Department: ")
        emp.DeptFilter(dept) 
    elif option==8:      
         print("Thank you...!")   
    else:
        print("Invalid login")                                

