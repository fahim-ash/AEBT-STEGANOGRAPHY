
import itertools
# =============================================================================
# Read The data from the file
# =============================================================================
f = open("G:/specialText.txt", "r", encoding="utf-8")
if f.mode =="r":
    data = f.read()
# Special Character Dataset
# =============================================================================
# Output Result Array Defination
# =============================================================================
c1 = ['ড়', 'ঢ়', 'য়', 'র', 'গু', 'ো', 'ৌ', 'শু', 'হু', 'হৃ']
c2 = ['ড়', 'ঢ়', 'য়', 'ব়', 'গ‌ু', 'ো', 'ৌ', 'শ‌ু', 'হ‌ু', 'হ‌ৃ']

result = []

# =============================================================================
# Data traversing Loop
# =============================================================================
for i in range(len(data)):
    spn = '0'
    if ord(data[i]) == 8196 or ord(data[i]) == 8201 or ord(data[i]) == 8200 or ord(data[i]) == 8287 or ord(data[i]) == 8239:
        if ord(data[i]) == 8196:
            spn = '1'
        if ord(data[i]) == 8201:
            spn = '2'
        if ord(data[i]) == 8200:
            spn = '3'
        if ord(data[i]) == 8287:
            spn = '4'
        if ord(data[i]) == 8239:
            spn = '5'
        backind = data[0 : i]
        extract=backind.split()[-1]
        #print(extract)
        fl=0
        for item in range(len(c2)):
            #print(spn)
            if extract.find(c2[item])>=0:
                #print(c2[item])
                fl = 1
                if spn == '2':
                    result.append('101')
                if spn == '3':
                    result.append('110')
                if spn == '4':
                    result.append('111')
                if spn == '5':
                    result.append('1')
                if spn == '1':
                    result.append('100')
                break
        if fl == 0:
            for item in range(len(c1)):
                #print(spn)
                #print(c1[item])
                if extract.find(c1[item]) >= 0:
                    if spn == '1':
                        result.append('000')
                    if spn == '2':
                        result.append('001')
                    if spn == '3':
                        result.append('010')
                    if spn == '4':
                        result.append('011')
                    if spn == '5':
                        result.append('0')
                    break
        
    
# =============================================================================
# Result Representation Part:
# =============================================================================
print("Result in List Form : ")
print(result)
str1 = ''.join(str(e) for e in result)

#Result length:
print("Result Length: ")
print(len(str1))
# =============================================================================
#print every 8 bits:
print("Every 8 bits: ")
chopper =0
for item in range(len(str1)):
    chopper = chopper+1
    print(str1[item], end=" ")
    if chopper == 8:
        print('\n')
        chopper =0

#==============================================================================

n = int(str1, 2)
tres =n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
#Print decoded data
print("Result in decoded form: ")
print(tres)
    
    
