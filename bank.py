grt = input("Greeting: ")
grt = grt.lower().strip()
if grt.startswith("hello") == True:
    print("$0")
elif grt.startswith("h") == True:
    print("$20")
else:
    print("$100",end = "")
    