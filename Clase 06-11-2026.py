et = float(input("Total space (GB): "))
eo = float(input("Used space (GB): "))

if et > eo:
    print("Saving the document")
elif et == eo:
    print("No space available")
else:
    print("Error")