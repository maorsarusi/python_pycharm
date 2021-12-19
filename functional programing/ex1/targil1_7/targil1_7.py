def enterOneWord(word,dictionary):
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
    return dictionary
#
#תכנית ראשית
dictionary={}
with open('./shakespeare.txt','r',) as f:
    for line in f:
        words = line.split()
        for i in words:
            if i[len(i)-1]=="." or i[len(i)-1]=="," or i[len(i)-1]=="?" or i[len(i)-1]=="!"  or i[len(i)-1]=="(" or i[len(i)-1]==")" or i[len(i)-1]=="[" or i[len(i)-1]=="]" or i[len(i)-1]=="{":
          
                word =i[0:len(i)-1]
                enterOneWord(word,dictionary)
            else:
                 enterOneWord(i,dictionary)

   
for keys,values in dictionary.items():
       print("the word: "+ "'"+keys+"'"+" appears "+str(values)+" times")

          

   
                         
                         
    
                        
    
