word=str(input("enter a word: "))
reverse=""   
for i in word:
        reverse = i + reverse
 
print("The original word is: ", word)
 
print("Reverse of the word is: ", reverse)