def solution(nums):
    if nums == (None):
        return([])
    else:
        nums.sort()
        return(nums)

#def solution(nums):
    #return sorted(nums or [])