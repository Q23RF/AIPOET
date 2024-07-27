from random import randint, choice


files = ['懷古.txt', '抒情.txt', '奇詭.txt']
notFirst = "個裏鞋貴…後人祐握外款處廠場之的得著嗎吧呢了、，。！？：」"
notLast = "最不只款，一"
ban = "；：,.●()（）」「—~"


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
  for b in ban:
    body.replace(b, '')
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


def write(n, fn):
  results = []
  wordDict = buildWordDict(files[fn])
  while len(results)<n:
    initialWord = choice(list(wordDict.keys()))
    text = []
    currentWord = initialWord
    line = []
    lineLen = 0
    while True:
      if currentWord not in wordDict:
        currentWord = initialWord
      currentWord = retrieveRandomWord(wordDict[currentWord])
      line.append(currentWord)
      lineLen += len(currentWord)
      if lineLen > 9:
        line.append('\n')
        lineLen += 1
        currentWord = '\n'
      if currentWord == '\n':
        while len(line)>1 and line[0][0] in notFirst:
          lineLen -= len(line[0])
          line = line[1:]
        while len(line)>1 and line[-2][-1] in notLast:
          lineLen -= len(line[-1])
          line = line[:-1]
        if len(line) > 1:
          str = ""
          for word in line:
            str += word
          text.append(str)
        if len(text) == 4:
          break
        line = []
        lineLen = 0
    results.append(text)
  return results
