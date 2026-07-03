# Linear Search

def spam_detector(blacklist, sender):
    for i in range(len(blacklist)):
        if blacklist[i] == sender:
            return i
    return -1


blacklist = [101, 205, 309, 412, 587]
sender = int(input("Enter sender ID: "))

result = spam_detector(blacklist, sender)

if result != -1:
    print("Spam sender found at index", result)
else:
    print("Sender is not in blacklist")
