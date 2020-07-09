import os
import zappyprotocythan as zappy

g= open("test.txt","r")
d={}
for s in g:
    for i in range(len(s)):
        if(s[i:i+3]=="---"):
            a=s[0:i-1]
            b=s[i+4:(len(s)-1)]
            d[a]=b

    print(d)

d[""]="i didn't understand that sorry"
print("")
n = zappy.hear()
print("said: "+n)
while(n != "bye"):
    try:
        x=d[n]
    except:
        x=d[""]
    print("bot:"+x)
    zappy.say(x)
    print("")
    n = zappy.hear()
    print("said: "+n)

print("bye my friend!!!!!")
zappy.say("bye my friend!!!!!")
