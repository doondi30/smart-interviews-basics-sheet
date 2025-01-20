def unique():
    morse=[ ".-","-...","-.-.","-..",".","..-.","--.","....",
    "..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
    "...","-","..-","...-",".--","-..-","-.--","--."]
    n=int(input())
    w=input().split()
    
    t={
        ''.join(morse[ord(char)-ord('a')] for char in word) for word in w
    }

    print(len(t))
unique()
