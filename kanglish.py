
# Natural Language Toolkit: Kannada to KanGlish(kannada English)
# Copyright (C) 2019 NLTK Project NMAMIT 
# Author: Fedrick Royston Sequeira <sroystona13@gmail.com>
import re
def to_Kanglish(kannadaWords):
    kanEng=[]
    #checks whether arg is array type or string type
    #it is made so because to accept both sentence type and array...
    if isinstance(kannadaWords,list):
        #if true array will be array.
        kanWords=kannadaWords
    else:
        #if false it is made as array 
        kanWords=[kannadaWords]
    
    rule1={'ಕ':'k','ಅ':'a',
    'ಆ':'A',
    'ಇ':'i',
    'ಈ':'I',
    'ಉ':'u',
    'ಊ':'U',
    'ಋ':'Ru',
    'ೠ':'RU',
    'ಌ':'Li-',
    'ೡ':'LI-',
    'ಎ':'e',
    'ಏ':'E',
    'ಐ':'ai',
    'ಒ':'o',
    'ಃ':'H',       
    'ಓ':'O',
    'ಔ':'au',
    'ಖ': 'kh',
    'ಗ': 'g', 
    'ಘ': 'gh',
    'ಙ': 'NG',
    'ಚ': 'ch',
    'ಛ': 'Ch',
    'ಜ': 'j',
    'ಝ': 'jh',
    'ಞ': 'NY',
    'ಟ': 'T',
    'ಠ': 'Th',
    'ಡ': 'D',
    'ಢ': 'Dh',       
    'ಣ': 'N',
    'ತ': 't',
    'ಥ': 'th',
    'ದ': 'd',
    'ಧ':'dh',
    'ನ': 'n',
    'ಪ': 'p',
    'ಫ':' ph',
    'ಬ': 'b',
    'ಭ': 'bh',
    'ಮ': 'm',
    'ಯ': 'y',
    'ರ': 'r',
    'ಲ': 'l',
    'ವ': 'v',
    'ಶ': 'sh',
    'ಷ': 'Sh',
    'ಸ': 's',
    'ಹ': 'h',
    'ಳ': 'L',
    'ಱ': 'R',
    'ಕ್ಷ': 'kSh',
    'ಜ್ಞ': 'j`j'}
    rule2={ 'ಾ' :'A',
    '್':'',        
    'ಿ':'i',
    'ೀ':'I',
    'ೕ' :'e_',
    'ು' :'u',
    'ೂ' :'U',
    'ೃ' :'Ru',
    'ೄ' :'RU',
    'ೢ':'n\'',
    'ೣ':'n\'',
    'ೆ':'e',
    'ೇ':'E',
    'ೈ':'ai',
    'ೖ':'aI',
    'ೊ':'o',
    'ೋ':'O',
    'ೌ':'au',
    'ಃ':'H'}
    rule3={' ':' ','ಾ' :'A',
    '್':'',        
    'ಿ':'i',
    'ೀ':'I',
    'ೕ' :'e_',
    'ು' :'u',
    'ೂ' :'U',
    'ೃ' :'Ru',
    'ೄ' :'RU',
    'ೢ':'n\'',
    'ೣ':'n\'',
    'ೆ':'e',
    'ೇ':'E',
    'ೈ':'ai',
    'ೖ':'aI',
    'ೊ':'o',
    'ೋ':'O',
    'ೌ':'au',
    'ಂ':'M',
    'ಃ':'H',
    'ಅ':'a',
    'ಆ':'A',
    'ಇ':'i',
    'ಈ':'I',
    'ಉ':'u',
    'ಊ':'oo',
    'ಋ':'Ri',
    'ೠ':'RI',
    'ಌ':'Li-',
    'ೡ':'LI-',
    'ಎ':'e',
    'ಏ':'E',
    'ಐ':'ai',
    'ಒ':'o',
    'ಓ':'O',
    'ಔ':'au',
    'ಅಂ':'aM',
    'ಅಃ':'aH',
    'ಕ':'ka',
    'ಖ':'kha',
    'ಗ':'ga',
    'ಘ':'gha',
    'ಙ':'NGa', 
    'ಚ':'cha',
    'ಛ':'Cha',
    'ಜ':'ja',
    'ಝ':'jha',
    'ಞ':'NYa',
    'ಟ':'Ta',
    'ಠ':'Tha',
    'ಡ':'Da',
    'ಢ':'Dha',
    'ಣ':'Na', 
    'ತ':'ta',
    'ಥ':'tha',
    'ದ':'da',
    'ಧ':'dha',
    'ನ':'na', 
    'ಪ':'pa',
    'ಫ':'pha',
    'ಬ':'ba',
    'ಭ':'bha',
    'ಮ':'ma', 
    'ಯ':'ya',
    'ರ':'ra',
    'ಲ':'la',
    'ವ':'va',
    'ಶ':'sha',
    'ಷ':'Sha',
    'ಸ':'sa',
    'ಹ':'ha', 
    'ಳ':'La',
    'ಱ':'Ra',
    'ಕ್ಷ':'kSha',
    'ಜ್ಞ':'j`ja',
    '೦':'0',
    '೧':'1',
    '೨':'2',
    '೩':'3',
    '೪':'4',
    '೫':'5',
    '೬':'6',
    '೭':'7',
    '೮':'8',
    '೯':'9'}
    checkCh=''
    matchCh=''

    replacedWords=''
    #why array because we need to read word not character for cool performance...:)
    for kanWord in kanWords:
        countLen=0

    
        checkCh=''
        countLen=len(kanWord)
        kanWord += ' '
        count=0
        if countLen != 1:
             #checks for length, if length is greater than 1 
            while countLen >=2:
                #checks whether first character starts from (\u0C83)/(H)/(ಃ)
                if kanWord[count]=='\u0C83' and kanWord[count+1]==' ':
                    checkCh+='Ha'
                    count+=1
                    countLen-=1
                elif kanWord[count]=='\u0C83'and kanWord[count+1]!=' ':
                    checkCh+='H'
                    count+=1
                    countLen-=1
                #checks whether first character starts from (\u0C82)/(M)/(ಂ),,,if true it checks next character i.e _+ಂ+[ಕ-ನ]
                if kanWord[count]=='\u0C82':
                    #next it checks whether following character is between ಕ to ನ (\u0C95-\u0CA8).
                    matchChN=re.findall('[\u0C95-\u0CA8]+',kanWord[count+1])
                    if matchChN:
                        #if true. than ಂ is replaced by N
                        #because ಕಂಡ is spelled as kanda and ಕಂಬ as kamba
                        #so that means next character of ಂ(M) followed by any of the character ಕ to ನ (\u0C95-\u0CA8) should spelled as N
                        #and from ಪ to ಮ (\uCAA-\uCAE) should spelled as M
                        checkCh+='n'
                        count+=1
                        countLen-=1
                #here it checks character + 1 is between \u0CBA-\u0CE5 (rule2 values) like ೊ ೄ...     
                matchCh2=re.findall('[\u0CBA-\u0CE5]+',kanWord[count+1])
                if matchCh2:
                    #if true it will follow rule1 for character at position count and rule2 character at position count+1 
                    
                    if kanWord[count] in rule1 and kanWord[count+1] in rule2:
                        checkCh+=rule1[kanWord[count]]
                        checkCh+=rule2[kanWord[count+1]]
                        count +=2
                        countLen-=2
                    
                    else:
                        #if character is not mentioned in rules, it will place same character. like english charaters or other unicode characters
                        
                        checkCh+=kanWord[count]
                        checkCh+=kanWord[count+1]
                        count +=2
                        countLen-=2
                           
                else:
                    #else it follows rule 3 for position of count value only
                    #but in rule 3 ಕ is ka
                    if kanWord[count] in rule3:
                        checkCh+=rule3[kanWord[count]]
                        count +=1
                        countLen-=1
                          
                    else:
                        #if character is not mentioned in rules, it will place same character. like english charaters or other unicode characters
                        checkCh+=kanWord[count]
                        count +=1
                        countLen-=1
                        
        #if only 1 charater is found .             
        if countLen==1:
            if kanWord[count] in rule3:
                checkCh+=rule3[kanWord[count]]
                   
            else:
                #if character is not mentioned in rules, it will place same character. like english charaters or other unicode characters
                        
                checkCh+=kanWord[count]
        kanEng.append(checkCh.strip())       
        
    return kanEng

              

