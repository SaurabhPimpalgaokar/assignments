import os

class CollectFiles :
    
    def __init__(self):
        self.list=[]
        self.list1=[]
        
    def ReadCurrentDirectory(self):
        location = 'C:/CollectFiles'
        for root , directories , files  in os.walk(location):       # root-> points to folder . directories-> point to current directory  files-> point to files
             for name in files :                                    # travel through all files
                 self.list.append(name)                             # store each file in list
        print(self.list)


    def CheckCurrentFile(self):
        if 'Exe_third.py' in self.list :                            # check whether current file is present in list of collected files
            print("Current file found")
        else:
            print("current file not found")


    def ModifyReadDirectory(self,path,extension):
        self.path = path                                            # here path and file extension is taken from user
        self.extension = extension
        for root , directories , files in os.walk(self.path):       # root-> points to folder . directories-> point to current directory  files-> point to files
            for name in files :                                     # travel through each file
                if name.endswith(self.extension):                   # if file if of extension given by user
                    self.list1.append(name)                         # put only those files in a single list
        print("Modified list : ",self.list1)


c = CollectFiles()
c.ReadCurrentDirectory()
c.CheckCurrentFile()
path=input("Enter file path : ")                                
extension=input("Enter extension : ")
c.ModifyReadDirectory(path,extension)                           



