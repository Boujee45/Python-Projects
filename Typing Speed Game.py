import time

target_text = "Python is the best language"

print("Type this fast: ")
print(target_text)

input("\nPress enter to start...")
start_time = time.time()

user_input = input("\nStart Typing: ")
end_time = time.time()

if user_input == target_text:
    '''time_taken = (end_time - start_time) / 60 'words per minute'
    wpm = round(len(target_text.split()) / time_taken, 2)'''
    time_taken = end_time - start_time
    print(f"{time_taken = :.2f} sec")
else:
    print("Try Again!")