#Assignment_8 Class

class Employee:
    def __init__(self, Name, Title, Department, Boss, Salary, Startdate):
        self.name = Name
        self.title = Title
        self.department = Department
        self.boss = Boss
        self.salary = Salary
        self.startdate = Startdate

    # Accessor Methods
    def getName(self):
        return self.name

    def getTitle(self):
        return self.title

    def getDepartment(self):
        return self.department

    def getBoss(self):
        return self.boss

    def getSalary(self):
        return self.salary

    def getStartdate(self):
        return self.startdate

#SuperClass
class CustomerBusiness:
    def __init__(self, Name, businessName, overSee):
        self.name = Name 
        self.businessname = businessName
        self.oversee = overSee

    def getName(self):
        return self.name

    def getbusinessName(self):
        return self.businessname

    def getoverSee(self):
        return self.oversee

class Customer(CustomerBusiness):
    def __init__(self, Name, businessName, overSee, acctNum, acctSize):
        self.acctNum = acctNum
        self.acctSize = acctSize
    
        #Can access the CustomerBusiness class
        CustomerBusiness.__init__(self, Name, businessName, overSee)

    def getacctNum(self):
        return self.acctNum

    def getacctSize(self):
        return self.acctSize

class BusinessPartner(CustomerBusiness):
    def __init__(self, Name, businessName, overSee, businessType):
           self.businesstype = businessType
           
           CustomerBusiness.__init__(self, Name, businessName, overSee)

    def getbusinessType(self):
        return self.businesstype


def makeEmployee(infoStr):

    #returns corresponding Employee object
    Name, Title, Department, Boss, Salary, Startdate = infoStr.split(",")
    return Employee(Name,Title, Department, Boss, Salary, Startdate)


def makeCustomer(infoStr):
    Name, businessName, overSee, acctNum, acctSize = infoStr.split(",")
    return Customer(Name, businessName, overSee, acctNum, acctSize)

def makeBusinessPartner(infoStr):
    Name, businessName, overSee, businessType = infoStr.split(",")
    return BusinessPartner(Name, businessName, overSee, businessType)



def main():

    # opens the input file for reading
    filename = input("Enter company file: ")
    infile = open(filename, 'r')

    # create objects from text file
    Employee_1 = makeEmployee(infile.readline())
    Employee_2 = makeEmployee(infile.readline())
    Customer = makeCustomer(infile.readline())
    BusinessPartner = makeBusinessPartner(infile.readline())



    infile.close()

    # prints the information
    print("Employee", Employee_1.getName(), Employee_1.getTitle(), Employee_1.getDepartment(), Employee_1.getBoss(), Employee_1.getSalary(), Employee_1.getStartdate())
    
    print("Employee", Employee_2.getName(), Employee_2.getTitle(), Employee_2.getDepartment(), Employee_2.getBoss(), Employee_2.getSalary(), Employee_2.getStartdate())

    print("Customer", Customer.getName(), Customer.getbusinessName(), Customer.getoverSee(), Customer.getacctNum(), Customer.getacctSize())

    print("BusinessPartner", BusinessPartner.getName(), BusinessPartner.getbusinessName(), BusinessPartner.getoverSee(), BusinessPartner.getbusinessType())


main()
