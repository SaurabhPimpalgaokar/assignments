class Dictionary:
    Dict={}
    def __init__(self):
        self.Index_list=[1,2,3,4,5,6,7,8,9,10,11,12]
        self.Name_list=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    
    def Add(self):
        for key in self.Index_list:                             #iterate through index list
            Dictionary.Dict[key] = self.Name_list[key-1]        # As Key points to list with index from 1 to 12 , key-1 ranges from 0 to 11.SO , using key-1 can avoid extrav variable 
        print(Dictionary.Dict)

D = Dictionary()
D.Add()



