vowel= 0
word= input("Enter your Name: ")
for char in word:
    if char.lower() in "aeiou":
        vowel = vowel+1
        print(vowel)
    