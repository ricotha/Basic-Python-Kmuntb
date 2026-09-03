# Create a program to get a keyword from user.
# When user input a keyword != Exit, store the keyword to "keywords.txt" file.
#If not reading and printing keywords

file = open("keywords.txt", "w")
file.close()
 
while True:
    keyword = input("Enter a keyword (type 'Exit' to stop): ")
 
    if keyword == "Exit":
        break
 
    file = open("keywords.txt", "a")
    file.write(keyword + "\n")
    file.close()
 
print("\nKeywords stored in keywords.txt:")
file = open("keywords.txt", "r")
for line in file:
    print(line.strip())
file.close()
