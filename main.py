# here will be my python program
import time
import string
text = "Hello world, help me with Czech Literatura!!!"
temp = ""
for ch in text:
    for i in string.printable:
        if i == ch or ch == temp:
            time.sleep(0.02)
            print(temp+i)
            temp +=ch
            break
        else:
            time.sleep(0.02)
            print(temp+i)

