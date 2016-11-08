__author__ = 'student'
filename =open('input.txt')
n=int(input())
a=[]
words={}
s1='spisok'
for i in range(n):
    x=input()
    a.append[x]
for line in filename:
    s=line.split().split(' : ')
    words[s[0]]=s[1]
    s=s+s[0]
for i in range(n):
    for t in range(len(words)):
        s=s[t]
        if s.find(i)!=-1:
            print(s)