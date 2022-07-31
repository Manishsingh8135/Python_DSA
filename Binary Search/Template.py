
def BinarySearch(nums,target):
    left,right=0,len(nums)-1

    while left<right:
        mid=left+(right-left)//2

        if nums[mid]<target:
            left=mid+1
        else:
            right=mid
    return left

arr=[2,3,4,5,6,7,,8,9]
target=3
a=BinarySearch(arr,target)
print(a)