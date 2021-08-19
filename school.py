class School:
    def __init__(self,rollnum,name,fname,mname,address,email,phone):
        
        self.rollnum = rollnum
        self.name    = name
        self.fname   = fname
        self.mname   = mname
        self.address = address
        self.email   = email
        self.phone   = phone
        

    #access method (get method)
    def getRollnum(self):
        return self.rollnum
   
    def getName(self):
        return self.name
    
    def getFname(self):
        return self.fname
    
    def getMname(self):
        return self.mname
        
    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email
        
    def getPhone(self):
        return self.phone


    #mutator method (set method) 
    def setRollnum(self,rollnum):
        self.rollnum = rollnum
        
    def setName(self,name):
        self.name = name
    
    def setFname(self,fname):
        self.fname = fname
    
    def setMname(self,mname):
        self.mname = mname
        
    def setAddress(self,address):
        self.address = address
        
    def setEmail(self,email):
        self.email = email
    
    def setPhone(self,phone):
        self.phone = phone
        
        
        