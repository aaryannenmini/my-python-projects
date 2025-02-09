nums = [34,5,6,5,3,24,8,5,3,675,2,3,53,5]
nams=["Aaryan","Is","The","Best"]
list=[24,5,5.6,True,"Aa"]

#acessing

print(nums[-4])
print(nams[1])
print(list[-2])
list[3]=False
print(list)

#appending item in a list

nams.append("bingo")
print(nams)
print(nams[-1])
  
# inserting items on a listlist.insert(4,True)
print(list)

#extending a list

list.extend([2,4,7,69,"random.randint"])
print(list)

#removing an item from a list

list.remove(False)
print(list)

print(nums)
nums.remove(5)#value
print(nums)

nams.pop(0)#index
print(nams)

del nums[6:]
print(nums)

#inbuilt function
print(min(nums))
print(max(nums))
print(sum(nums))
print(nums.count(5))
nams_copy=nams.copy()
print(nams_copy)
combined=nams+nums
print(combined)
#sorting the list
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nams.sort()
print(nams)
#Looping
fruits=["Applebees","Hi-Chews","Pinapple","orange","python","lists","data strucutre"]

for i in fruits:
    print(i)
