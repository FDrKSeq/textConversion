
# Natural Language Toolkit: Kannada to KanGlish(kannada English)
# Copyright (C) 2019 NLTK Project
# Author: Fedrick Royston Sequeira <sroystona13@gmail.com>


import re
def to_Kanglish(kanWord):
    if isinstance(kanWord,list):
        kanWord=kanWord
    else:
        kanWord=[kanWord]
    
    rule1={ 'ಕ':' k','ಅ':'a',
    'ಆ':'aa',
    'ಇ':'i',
    'ಈ':'ee',
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
    'ಂ':'M',
    'ಃ':'/H',
    'ಓ':'O',
    'ಔ':'au[ou]',
    'ಖ': 'kh',
    'ಗ': 'g', 
    'ಘ': 'gh',
    'ಙ': 'g',
    'ಚ': 'ch',
    'ಛ': 'Ch',
    'ಜ': 'j',
    'ಝ': 'jh',
    'ಞ': 'j',
    'ಟ': 't',
    'ಠ': 'T',
    'ಡ': 'd',
    'ಢ': 'D',
    'ಫೆ':'Fe',
    'ಡ್ರಿ':'dri',
    'ಕ್':'ck',        
    'ಣ': 'N',
    'ತ': 'th',
    'ಥ': 'Th',
    'ದ': 'dh',
    'ಧ':'Dh',
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
    'ಕ್ಷ': 'ksh',
    'ಜ್ಞ': 'j`j'}
    rule2={ 'ಾ' :'aa',
    '್':'\'',        
    'ಿ':'i',
    'ೀ':'ee',
    'ೕ' :'e_',
    'ು' :'u',
    'ೂ' :'U',
    'ೃ' :'Ri',
    'ೄ' :'RI',
    'ೢ':'Li-',
    'ೣ':'LI-',
    'ೆ':'e',
    'ೇ':'E',
    'ೈ':'ai',
    'ೖ':'aI',
    'ೊ':'o',
    'ೋ':'oo',
    'ೌ':'au',
    'ಂ':'M/',
    'ಃ':'/H'}
    rule3={' ':' ','ಅ':'a',
    'ಆ':'aa',
    'ಇ':'i',
    'ಈ':'ee',
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
    'ಂ':'M',
    'ಃ':'/H',
    'ಔ':'au[ou]',
    'ಅಂ':'aM',
    'ಅಃ':'aH',
    'ಕ':'ka',
    'ಖ':'kha',
    'ಗ':'ga',
    'ಘ':'gha',
    'ಙ':'`ga', 
    'ಚ':'cha',
    'ಛ':'Cha',
    'ಜ':'ja',
    'ಝ':'jha',
    'ಞ':'`ja',
    'ಟ':'ta',
    'ಠ':'Ta',
    'ಡ':'da',
    'ಢ':'Da',
    'ಣ':'Na', 
    'ತ':'tha',
    'ಥ':'Tha',
    'ದ':'dha',
    'ಧ':'Dha',
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
    'ಕ್ಷ':'ksha',
    'ಜ್ಞ':'j`ja'} 

    checkCh=''
    matchCh=''

    replacedWords=''
    for kanWord in kanWord:
        countLen=0
        checkCh=''
        countLen=len(kanWord)
        count=0
        if countLen != 1:
            while countLen >=2:
                
                matchCh=re.findall('[\u0CBB-\u0CDD]+',kanWord[count+1])
                if matchCh:
                    checkCh+=rule1[kanWord[count]]
                    checkCh+=rule2[kanWord[count+1]]
                    count +=2
                    countLen-=2
                else:
                    if kanWord[count] in rule3:
                        checkCh+=rule3[kanWord[count]]
                        count +=1
                        countLen-=1
                    else:
                        checkCh+=kanWord[count]
                        count +=1
                        countLen-=1
                        
        if countLen==1:
            if kanWord[count] in rule3:
                checkCh+=rule3[kanWord[count]]
            else:
                checkCh+=kanWord[count]
        
    return checkCh






