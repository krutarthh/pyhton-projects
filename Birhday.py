Birthday=input("give your birthday (dd/mm/yyyy) ")

k=Birthday[4:]
k=int (k)
if k<1000 :
    print("Common, How are you still even alive?")
elif k>2022:
    print("Common,You are not even in born!!?")
else:
 print("your birthyear is", Birthday[4:])

