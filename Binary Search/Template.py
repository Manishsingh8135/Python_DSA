
# This template is for general Binary Search , where you get a target to search
#Note that this template doesn't tell whether, the target element exists or not.
    #For this an extra check if required
def BinarySearch(nums,target):
    left,right=0,len(nums)-1

    while left<right:
        mid=left+(right-left)//2

        if nums[mid]<target:
            left=mid+1
        else:
            right=mid
    #To check whether the target exists in the given array
    if target==nums[left]:
        return left
    else:
        return -1

N=int(input())
arr=list(map(int,input().split()))
target=int(input())
a=BinarySearch(arr,target)
