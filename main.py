question = input("Enter solved question name:")
difficulty = input("Enter difficulty(Easy/Medium/Hard):")
topic = input("Enter topic:")
file= open("progress.txt", "a")
file.write(question + " - " + difficulty + " - " + topic + "\n")
file.close()
print("Question Saved Successfully!")
print("\nYour Saved Progress:\n")
file = open("progress.txt", "r")
data = file.read()
print(data)
file.close()
search = input("Enter question to search:")
file = open("progress.txt", "r")
data = file.read()
if search in  data:
    print("Question Found!")
else:
    print("Question Not Found!")
file.close()


