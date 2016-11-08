__author__ = 'student'
import string
words = {}
strip =string.punctuation
filename =open('/usr/share/licenses/python/LICENSE')
filename=filename.read().lower()
for i in strip:
    filename=filename.replace(i,' ')
wordss=filename.split()
for i in wordss:
    x=wordss.count(i)
    words[i]=x
max1=0
s='stroka'
for c in range(10):
    for i in words:
        value =words.get(i)
        if value>max1:
            max1=value
            s=i

    print(s,max1)
    words.pop(s)
    max1=0




