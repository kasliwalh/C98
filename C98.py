file = open("test.txt")
fileRead = file.readlines()
for eachLine in fileRead:
  print(eachLine)

introString = "My name is Hitasha, I am 12 years old"
words = introString.split()
print(words)

introString = "My name is Hitasha, I am 12 years old"
partition = introString.split(",")
print(partition)

introString = "My name is Hitasha, I am 12 years old"
sentence = introString.split(":")
print(sentence)

def greet(name):
  print("Hello " + name + ". How are you?")
greet("Hitasha")



def countWords():
    fileName = input("Enter the file: ")
    numberOfWords = 0
    file = open(fileName, 'r')
    for eachLine in file:
        words = eachLine.split()
        numberOfWords = numberOfWords + len(words)
    print("The number of words inside the file are ")
    print(numberOfWords)

countWords()