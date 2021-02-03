import math1 as m                   # math1 is user dedined module
import sys

x=sys.argv                          # all the arguments from command iibe are stored in list sys.argv
a = int ( x[1] )                    # as 0th index holds name of file , we start from first index
b = int ( x[2] )
print( "sum : ", m.Sum(a,b) )       # function for addition
print( "Diff : ", m.Diff(a,b) )     # function for division
print( "Mul : ", m.Mul(a,b) )       # function for multipliction


