print("===== DSA Progress Tracker=====")
while True:
    name =  input("Enter Solved question name (or type exist): ")
    if name.lower() == "exit":
        print("Progress saved. Existinng...")
        break  
    print("Question Saved:", name)
