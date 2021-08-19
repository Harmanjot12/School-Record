from school import School
import pickle


#creating list of for records
record = []


#writing record in binary file
def writedata():
   
    while(True):
        
        print("\t\t\t \t\t *Welcome to Delhi Public School* \n Here you can add record of new student")
        
        #input data from user        
        rollnum  = int(input("Roll Number   : "))
        name    = input("Enter Student  Name : ")
        fname    = input("Enter Father's Name : ")
        mname    = input("Enter Mother's Name : ")
        address  = input("Residencial Address : ")
        email    = input("Email Address : ")
        phone    = int(input("Phone Number : "))
        
        obj = School(rollnum,name,fname,mname,address,email,phone)
        
        record.append(obj)
        
        
        
        #asking user weather they want to enter more values or not
        more = input("Want to enter more : ")
        more = more.lower()
        if (more=='n'):
            print("\t\t\t\t\t\tThankyou ! ")
            break
        

    with open("student.bin" , "wb") as f:
        pickle.dump(record,f)
           
    f.close()



#reading record from binary file
def readdata():
    with open("student.bin" , "rb") as f:
        global record
        record = pickle.load(f)

    f.close()



#to print all the data from file
def printdata():
    print("\n\n")
    print("Here is Record of all students")
    for s in record:
        print("----------------------")
        print("Roll Num    - " + str(s.getRollnum()))
        print("Name        - " + s.getName())
        print("Father Name - " + s.getFname())
        print("Mother Name - " + s.getMname())
        print("Address     - " + s.getAddress())
        print("Email       - " + s.getEmail())
        print("Phone       - " + str(s.getPhone())   + "\n")
        

#calling main function
def main():
    readdata()
    writedata()
    printdata()

if __name__ == "__main__":
    main()