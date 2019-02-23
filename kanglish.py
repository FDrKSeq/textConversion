
# Natural Language Toolkit: Kannada to KanGlish(kannada English)
# Copyright (C) 2019 NLTK Project NMAMIT 
# Author: Fedrick Royston Sequeira <sroystona13@gmail.com>
import re
def to_Kanglish(kannadaWords):
    kanEng=[]
    if isinstance(kannadaWords,list):
        kanWords=kannadaWords
    else:
        kanWords=[kannadaWords]
    
    rule1={'ಕ':'k','ಅ':'a',
    'ಆ':'aa',
    'ಇ':'e',
    'ಈ':'E',
    'ಉ':'u',
    'ಊ':'oo',
    'ಋ':'Ri',
    'ೠ':'R^',
    'ಌ':'Li-',
    'ೡ':'LI-',
    'ಎ':'e',
    'ಏ':'E',
    'ಐ':'ai',
    'ಒ':'o',
    'ಃ':'H',       
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
    'ಣ': 'N',
    'ತ': 't',
    'ಥ': 'T',
    'ದ': 'd',
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
    '್':'',        
    'ಿ':'i',
    'ೀ':'I',
    'ೕ' :'e_',
    'ು' :'u',
    'ೂ' :'U',
    'ೃ' :'Ri',
    'ೄ' :'RI',
    'ೢ':'n\'',
    'ೣ':'n\'',
    'ೆ':'e',
    'ೇ':'E',
    'ೈ':'ai',
    'ೖ':'aI',
    'ೊ':'o',
    'ೋ':'oo',
    'ೌ':'au',
    'ಃ':'H'}
    rule3={' ':' ','ಾ' :'aa',
    '್':'',        
    'ಿ':'i',
    'ೀ':'I',
    'ೕ' :'e_',
    'ು' :'o',
    'ೂ' :'oo',
    'ೃ' :'Ri',
    'ೄ' :'RI',
    'ೢ':'n\'',
    'ೣ':'n\'',
    'ೆ':'e',
    'ೇ':'E',
    'ೈ':'ai',
    'ೖ':'aI',
    'ೊ':'O',
    'ೋ':'Oo',
    'ೌ':'au',
    'ಂ':'M',
    'ಃ':'H',
    'ಅ':'a',
    'ಆ':'AA',
    'ಇ':'e',
    'ಈ':'E',
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
    'ತ':'ta',
    'ಥ':'Ta',
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
    for kanWord in kanWords:
        countLen=0
        kanWord+=' '
    
        checkCh=''
        countLen=len(kanWord)
        count=0
        if countLen != 1:
            while countLen >=2:
                if kanWord[count]=='\u0C82':
                    matchChN=re.findall('[\u0C95-\u0CA8]+',kanWord[count+1])
                    if matchChN:
                        
                        checkCh+='N'
                        count+=1
                        countLen-=1
                        
                matchCh2=re.findall('[\u0CBA-\u0CE5]+',kanWord[count+1])
                  
                if matchCh2:
                    if kanWord[count] in rule1 and kanWord[count+1] in rule2:
                        checkCh+=rule1[kanWord[count]]
                        checkCh+=rule2[kanWord[count+1]]
                        count +=2
                        countLen-=2
                    
                    else:
                        checkCh+=kanWord[count]
                        checkCh+=kanWord[count+1]
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
        kanEng.append(checkCh.strip())       
        
    return kanEng

              

