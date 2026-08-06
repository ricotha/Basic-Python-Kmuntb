#Exercise 3.1
#Input a word
#if you input "exit" or EXIT
#The program will stop and print words you input

word = input("Enter a word: ")
while True:
    if word.lower() == "exit":
        print("Program stopped")
        break
    print(word)
    word = input("Enter a word: ")