filename = input("Input the Filename: ")
find = filename.rfind(".")
extension = filename[find + 1:]
print("The extension of the file is:", extension)