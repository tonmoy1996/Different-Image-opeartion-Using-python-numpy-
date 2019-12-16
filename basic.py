num2=12

name="tonmoy"

print("My name is {} and age is {}".format(name,num2))

#list
my_list=[1,2,3,4,5,6]

my_list.append([7,8,9,10])
print(my_list[6][0])

# Dictionary

my_dict={'num1':3,'num2':2,'num3':4}

my_dict
print(my_dict['num1'])

# tuple is immutable


my_tuple=(1,2,3,4,4)

print(my_tuple)



#set is always store distinct value

my_set={1,2,3,4,1,2,3,4,5,6,2,3}

print(my_set)

##List Comprehension


num_list=[1,2,3,4,5,6,7]

out=[]

print("My List {}".format(num_list))

for num in num_list:
    out.append(num**2)


print(out)


### Now List Comprehension

print("Comprehension List")
com=[num**2 for num in num_list]

print(com)


print("##############################################")


#function
def makeSquare(value):

    return value**3


#print(makeSquare(3))


seed=[1,2,3,4,5,6]


shlist=list(map(makeSquare,seed))

print(shlist)

## Lamda expression

makecube= lambda num:num**2


#print(makecube(9))


#lamda with mapping

print(list(map(makecube,seed)))


#filter


filterValue=filter((lambda num:num%2==0),seed)

print(list(filterValue))




