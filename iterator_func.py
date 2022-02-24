
import itertools
list1=[1,2,3,4]

list2=list(itertools.starmap(pow,list(zip(list1,itertools.repeat(2,times=4)))))
print(list2)
