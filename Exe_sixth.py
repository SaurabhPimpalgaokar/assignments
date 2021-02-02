import os
listFiles = []
cmplist=["INFO","ERROR","WARNING"]
infoCnt = 0
errorCnt = 0
warningCnt = 0
totalLines = 0
# If we extract zip file in code , the file is extracted each time we run the code
# hence we extracted the zip file manually and through the code
#...........Code to extract zip file...............................
'''
from zipfile import ZipFile
with ZipFile('C:\\Users\\saura\\Documents\\log_files.zip','r') as zip :
zip.extractall('C:\\CollectFiles\\zipfolder')
'''

location = 'C:\\Users\\saura\\Documents\\zipfolder'
for travel in os.walk(location):                                 # Go to desired location              
    listFiles.append(travel)                                     # append all files of folder in a list
    for root, subdir, files in listFiles :                       # root->points to folder , subdir->points to directory , files->points to files
        for file in files :                                      # read each file in files using for loop
            print(file)
            fullFilePath = os.path.join(root, file)              # join folder name and file name to pass complete path of file 
            f = open(fullFilePath,'r')                           # open file in read mode
            for line in f:
                if ( line.startswith('[') and ']' in line ) :    # Check whether the line contains [ and ] symbol to avoid reading of NULL value
                     text = line.split(']')                      # split the line on ']' because that will be the result we will work on
                     text2 = text[0].split(':')                  # now we will work on only first index becasue we get all info , error , warning in first index
                     index = cmplist.index(text2[-1])            # text2[-1] will give info or error or warning . now find its index in cmplist and increment its accordingly
                     if (index == 0):
                            infoCnt = infoCnt + 1
                     elif (index == 1):
                            errorCnt = errorCnt + 1
                     elif (index == 2):
                            warningCnt = warningCnt + 1

                     totalLines = totalLines + 1                # this counter is incremented for each iteration of loop

            
print("-num_of_errors = ",errorCnt)
print("-num_of_warnings = ",warningCnt)
print("-num_of_info = ",infoCnt)
print("-num_of_log_lines",totalLines)
                    
                    
                
                    
            
            
    







   
