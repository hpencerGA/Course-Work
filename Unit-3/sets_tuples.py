#set key thing we can do is build it from a list
#common use case is to conver a list to a set to get unique numbers in a set
nums = [1, 2, 3, 4, 4, 5, 5, 6, 1]
unique_nums = set(nums)

print(unique_nums) #can grab an element from a set by

unique_nums.remove(3)
print(unique_nums) 

unique_nums.add(10)
print(unique_nums) 

#tuple similar to a list but not mutuable cant change elements in a list
#to create use round bracket

colors = ('red', 'blue', 'green')
#can index to grab elements in list
#use for geospatial coordinates or if dont want to change anything


