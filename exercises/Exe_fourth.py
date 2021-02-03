def Fun(count):
    cnt = count                                       # cnt = size of list 
    if(cnt<9): 
        print("Number of items : ",cnt)
    else:
        print("Number of items : many")

x=list( map( int,input("Enter numbers: ").split() ) )   # take multiple input of integer type from user and store them in single list
count=len(x)                                            # size of list
Fun(count)
