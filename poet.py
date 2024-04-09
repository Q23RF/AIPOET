from random import randint, choice


def wordListSum(wordList):
    sum = 0
    for value in wordList.values():
        sum += value
    return sum


def retrieveRandomWord(wordList):

    randIndex = randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word


def buildWordDict(fn):
    d = {}
    infile = open(fn, "r", encoding='utf-8')
    body = infile.read()
    infile.close()
    addWord(body, d)
    return d


def addWord(words, wordDict):
    import jieba
    words = words.replace("？", "")
    words = jieba.lcut(words)
    for i in range(1, len(words)):
        if words[i - 1] not in wordDict:
            wordDict[words[i - 1]] = {}
        if words[i] not in wordDict[words[i - 1]]:
            wordDict[words[i - 1]][words[i]] = 0
        wordDict[words[i - 1]][words[i]] += 1


files = ['懷古.txt', '抒情.txt', '奇詭.txt']

notfirst = "個裏鞋貴…後人祐握外款處廠場之的得著嗎吧呢了、，。！？：」"
notlast = "最不只款，一"
no = "；：,.●()（）」「—~"


def write(n, fn):
    re = []
    wordDict = buildWordDict(files[fn])

    while len(re) < n:
        passed = True
        initialWord = choice(list(wordDict.keys()))
        text = []
        currentWord = initialWord
        line = ""
        while True:
            if currentWord not in wordDict:
                currentWord = initialWord
            currentWord = retrieveRandomWord(wordDict[currentWord])

            line += currentWord
            if len(line) > 7:
                line += '\n'
                currentWord = '\n'
            if currentWord == '\n':
                for c in line:
                    if c in no:
                        passed = False
                while line[0] in notfirst:
                    line = line[1:]
                else:
                    text.append(line)
                    if len(text) > 4 and len(text) < 6:
                        while text[0][0] == '\n':
                            del text[0]
                        while text[-1][0] == '\n':
                            del text[-1]
                        while len(line) > 2 and line[-2] in notlast:
                            text[-1] = line[:-2] + '\n'
                        break
                    line = ""

        if passed:
            re.append(text)
    return re
