# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 02:59:23 2020

@author: User
"""
print("Write the message You want to Hide >>")
text= input()
encoding='utf-8'
errors='surrogatepass'
bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
sequence = bits.zfill(8 * ((len(bits) + 7) // 8))


print(len(sequence))   
print("The string after binary conversion : " + sequence)

comp = ['100', '101', '110', '111', '1']
words = []
res =""
dicti = {'000':" ",'100':" ",'001':" ",'101':" ", '010':" ", '110':" ",'011':" ", '111':" ", '0':" ", '1':" "}

#Read the plain text file
f = open("G:/plainText.txt", "r", encoding="utf-8-sig")
if f.mode =="r":
    text = f.read()


words = text.split()
#print(words)

c1 = ['ড়', 'ঢ়', 'য়', 'র', 'গু', 'ো', 'ৌ', 'শু', 'হু', 'হৃ' ]
c2 = ['ড়', 'ঢ়', 'য়', 'ব়', 'গ‌ু', 'ো', 'ৌ', 'শ‌ু', 'হ‌ু', 'হ‌ৃ' ]

kc = 0

for i in range(len(words)):
    
    for j in range(len(c1)):
        flag =0
        
        if words[i].find(c1[j])>=0 and sequence[kc: kc+3] in comp and len(sequence) - kc >=3:
            #print("kcc: {}".format(sequence[kc: kc+3]))
            katara =words[i].replace(c1[j], c2[j])
            res = res + katara+dicti.get(sequence[kc:kc+3])
            #print("res: {}".format(res))
            kc = kc+3
            flag=1
            #print("rc1: {}".format(res))
            break
        elif words[i].find(c1[j])>=0 and sequence[kc: kc+3] not in comp and len(sequence) - kc >=3:
            #print("kc: {}".format(sequence[kc: kc+3]))
            res = res + words[i]+dicti.get(sequence[kc:kc+3])
            #print("res: {}".format(res))
            kc = kc+3
            flag=1
            #print("rc2: {}".format(res))
            break;
            
        elif words[i].find(c1[j])>=0 and sequence[kc: kc+1] in comp and len(sequence) - kc <3 and len(sequence) - kc >0:
            #print("ko",sequence[kc: kc+1])
            katara =words[i].replace(c1[j], c2[j])
            res = res + katara+dicti.get(sequence[kc:kc+1])
            kc = kc+1
            flag=1
            #print("rc2: {}".format(res))
            break;
            
        elif words[i].find(c1[j])>=0 and sequence[kc: kc+1] not in comp and len(sequence) - kc <3 and len(sequence) - kc >0:
            
            res = res + words[i]+dicti.get(sequence[kc:kc+1])
            #print(res)
            kc = kc+1
            flag=1
            #print("rc2: {}".format(res))
            break;
    if flag == 0:       
        res = res + words[i]+" "
            
    if kc >= len(sequence):
        break
    
if kc < len(sequence):
    print("Whole sequence is not been updated in result!")
print(res)

#Write data in the text file
text_file = open("G:/specialText.txt", "w", encoding="utf-8-sig")
n = text_file.write(res)
text_file.close()

        

        
            
    

    
