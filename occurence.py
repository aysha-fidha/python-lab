line=input("Enter a line of text:")
words=line.split()
freq={}
for w in words:
    freq[w]=freq.get(w,0)+1
print(freq)