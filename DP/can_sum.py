def CanSumB(targetsum,array):
    if(targetsum==0):
        return True 
    for num in array:
        if(num>targetsum):
            continue 
        elif(CanSumB(targetsum-num,array)):
            return True 
    return False 

def HowSumB(targetsum,array):
    if(targetsum==0):
        return []
    for num in array:
        if(num>targetsum):
            continue 
        ans=HowSumB(targetsum-num,array)
        if(ans!=None):
            ans.append(num)
            return ans
    return None 

def HowSumTable(target,array):
    ans=[None]*(target+1)
    ans[0]=[]
    for i in range(target+1):
        if(ans[i]!=None):
            for j in array:
                if(i+j<=target):
                    short=ans[i]+[j] 
                    if(ans[i+j]==None or len(short)<len(ans[i+j])):
                        ans[i+j]=ans[i]+[j]
    return ans[target]
    
def CanSumM(targetsum,array):
    dp={}
    def helper(targetsum,array):
        if(targetsum==0):
            return True 
        if(targetsum in dp):
            return dp[targetsum]
        for num in array:
            if(num>targetsum):
                continue 
            elif(helper(targetsum-num,array)):
                dp[targetsum]=True  
                return True
        dp[targetsum]=False 
        return False 
    present= helper(targetsum,array)
    return present
   
print(CanSumM(8,[2,3,5]))
print(HowSumB(8,[2,3,5]))
print(HowSumTable(8,[2,3,5]))
print(HowSumTable(7,[2,3,5]))
print(HowSumTable(300,[6,14]))