def CanConstruct(target,wordbank):
    dp={}
    def helper(target,wordbank):
        if(target==""):
            return True
        if(target in dp):
            return dp[target]
        for i in range(len(wordbank)):
            word=wordbank[i]
            check=True 
            for j in range(len(word)):
                if(len(word)>len(target) or word[j]!=target[j]):
                    check=False 
                    break
            if(check):
                #slicing -creates a new string 
                if(CanConstruct(target[len(word):],wordbank)):
                    dp[target]=True
                    return True 
        dp[target]=False
        return False
    return helper(target,wordbank) 
        
def CountConstruct(target,wordbank):
    dp={}
    def helper(target,wordbank):
        if(target==""):
            return 1
        if(target in dp):
            return dp[target]
        count=0
        for i in range(len(wordbank)):
            word=wordbank[i]
            check=True 
            for j in range(len(word)):
                if(len(word)>len(target) or word[j]!=target[j]):
                    check=False 
                    break
            if(check):
                #slicing -create a new string 
                count+=CanConstruct(target[len(word):],wordbank)
        dp[target]=count 
        return dp[target]
    return helper(target,wordbank) 
def AllConstruct(target,wordbank):
    dp={}
    def helper(target,wordbank):
        if(target==""):
            return [[]]
        allans=[]
        for i in range(len(wordbank)):
            word=wordbank[i]
            check=True 
            for j in range(len(word)):
                if(len(word)>len(target) or word[j]!=target[j]):
                    check=False 
                    break
            if(check):
                #slicing -creates a new string O(n)
                ans=AllConstruct(target[len(word):],wordbank)
                ways=[[word]+each_combination for each_combination in ans]
                if ways:
                    #extend appends elements from the iterable
                    allans.extend(ways)
        return allans
    return helper(target,wordbank) 
       
print(CanConstruct("abcdef",["ab","abc","cd","def","abcd"]))
print(CountConstruct("abcdef",["ab","abc","cd","def","abcd","ef","c"]))
print(CanConstruct("abcdef",["ab","bc","cd","def","abcd"]))
print(CanConstruct("cchirag",["c","hi","aa","ag","r"]))
print(CountConstruct("purple",["purp","p","ur","le","purpl"]))
print(AllConstruct("purple",["purp","p","ur","le","purpl"]))
print(AllConstruct("abcdef",["ab","abc","cd","def","abcd","ef","c"]))
print(AllConstruct("abcdef",["ab"]))