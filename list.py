#(a)Positive numbers from a list
nums=[3,-5,2,-8,9,0,-1]
positives=[n for n in nums if n>0]
print("Positives: ",positives)

#(b)Squares of N numbers
n=int(input("Enter N:"))
squares=[i ** 2 for i in range(1,n+1)]
print("Squares:",squares)

#(c)Vowels in a word
word=input("Enter word:")
vowels=[ch for ch in word if ch.lower() in 'aeiou']
print("vowels:",vowels)

#(d)Ordinal value of each character
ordinals=[ord(ch)for ch in word]
print("Ordinal values:",ordinals)