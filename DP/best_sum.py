def BestSum(target,array):  
    dp={}
    def helper(target,array):       
        if(target==0):
            return []
        if(target in dp):
            return dp[target]
        #keep track of best_sum
        shortestCombination=None 
        for num in array:
            if(num>target):
                continue 
            ans=helper(target-num,array)
            if(ans!=None):
                ans=ans+[num]
                #for very first answer and when len is smaller
                if(shortestCombination==None or len(ans)<len(shortestCombination)):
                    shortestCombination=ans
        dp[target]=shortestCombination
        return shortestCombination
    return helper(target,array)

print(BestSum(8,[2,3,5]))
print(BestSum(7,[2,3,5,7]))
#print(BestSum(8,[1,4,5]))
print(BestSum(100,[1,2,5,25]))