success = True

for i in range(5):
    print("Attempt")
    if success:
        print("Success")
        break
else:
    print("Failed")    