def zipString(iniString):
    nlen = len(iniString)
    rest =[]
    i = 0
    endflag = 0
    while i < (nlen-1):
        for j in range(i+1, nlen):
            if iniString[i] == iniString[j]:
                continue
            else:
                rest.append((iniString[i], i, j))
                endflag = j
                break
        i = j
    rest.append((iniString[endflag], endflag, nlen))
    resStr =""
    for i in range(0,len(rest)):
        item=rest[i]
        resStr += (item[0] + str(item[2]-item[1]))
    if(len(resStr) >= nlen):
        return iniString
    else:
        return resStr

print(zipString('aabcccccaaa'))
print(zipString('welcometonowcoderrrrr'))
