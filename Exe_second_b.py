import csv
class ListOfTuple:
    list=[]

    def __init__(self):
        self.Index_list = [1,2,3,4,5,6,7,8,9,10,11,12]
        self.Name_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    
    def Convert(self):
        for travel in self.Index_list :
            x = travel                                                         # storing each element of Index list in 0th index of tuple
            y = self.Name_list[travel-1]                                       #storing each element of Name list in first index of tuple
            tup = (x,y)
            ListOfTuple.list.append(tup)                                       # append values in tuple


    def Show(self):
        print(ListOfTuple.list)


    def StoreInCsv(self):
            # separates ListOfTuple in two different lists
            self.newlist = [ x[0] for x in ListOfTuple.list ]                   # from ListOfTuple , put 0th value of each index in newlist 
            self.newlist1 = [ x[1] for x in ListOfTuple.list ]                  # from ListOfTuple , put 1st value of each index in newlist1 

            self.csv_rowlist=[]                                                 #list taken to insert multiple values in CSV file simultaeously

            for i in range(12):
                self.csv_rowlist.append([i,self.newlist[i],self.newlist1[i]])   # put all the id , month number ,month name in csv_rowlist

        
            with open ('month_names.csv','w',newline='') as file :              # open month_csv file in write mode
                writer=csv.writer(file)                                 
                writer.writerow(['id','month_num','month_name'])                # insert first row in CSV file
                for row in self.csv_rowlist:                                    #iterate through csv_rowlist and insert value at  each index , in each row of csv file respectively 
                    writer.writerow(row)    
            
            with open ('month_names.csv','r') as file :                         # open csv file in read mode
                reader=csv.reader(file)
                for row in reader :                                             # read complete csv file
                    print(row)

obj = ListOfTuple()
obj.Convert()
obj.Show()
obj.StoreInCsv()
