
def BinarySearch(nums,target):
    left,right=0,len(nums)-1

    while left<right:
        mid=left+(right-left)//2

        if nums[mid]<target:
            left=mid+1
        else:
            right=mid
    print(left)
    return left

N=int(input())
arr=list(map(int,input().split()))
target=int(input())
a=BinarySearch(arr,target)
