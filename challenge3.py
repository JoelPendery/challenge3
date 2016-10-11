import string
import codecs
import numpy as np

f = codecs.open("textChallenge3.txt",'r',encoding='utf-8')
text = f.read()
f.close

newText = list(text.encode('utf-8'))

uniqStr, uniqInd, uniqCounts = np.unique(newText,return_index=True,return_counts=True)

goodInd = np.where(uniqCounts - 1 == 0)[0]
sortInds = uniqInd[goodInd]
newArr = uniqStr[goodInd]


ts=np.array2string(newArr)
print string.join(ts)
#==============================================================================
# newText = ts.encode('utf-8')
# print newText
#==============================================================================

# print newText

# the answer is 'equality'