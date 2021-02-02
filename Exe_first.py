import sys

print( sys.argv ) 

string=sys.argv[1]

newstr=string[-1]

x=ord( newstr )

if(x<=90 and x>=65):
    print("true")
else :
    print("false")
