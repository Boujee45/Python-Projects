import wikipedia

topic = input("Enter keyword to search: ")
print("="*30)
print(f"Searching for: {topic}")
print("="*30)

res = wikipedia.summary(topic, sentences= 3)
print(res)
print("="*30)