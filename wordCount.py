import re
def countWord(words):
    try:
        wordList={}
        if not isinstance(words,list):
            wd=''
            count=0
            for wds in words+' ':
                if wds!='\u000A' and wds!=' ':
                    wd=wd+wds
                else:
                    if wd !='':
                        if not wd in wordList:
                            wordList[wd] = 1
                        else:
                            count=wordList[wd]
                            wordList.update({wd: count+1})
                        wd=''
        else:
            for wds in words:
                if not wds.strip() in wordList:
                    wordList[wds.strip()] = 1
                else:
                    count=wordList[wds.strip()]
                    wordList.update({wds.strip(): count+1})
                
        
    except:
        print('error')

    return wordList

