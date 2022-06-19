import os

print("Python Program started")
count = 1

def test():
    global count
    folder = input("\nPlease enter your path to your folder... [Must have \ on the last path parameter, Example : C:\Users\Hafiz Jasmi\Desktop\John_Cena\] : \n")
    naming_scheme = input("Please enter naming scheme here... [Example John, it will be John_1, John_2 and so on]  : \n")
    print("Files found in the folder are :\n\n")
    for file_name in os.listdir(folder):
        #Construct old file name
        source = str(folder) + str(file_name)
        print(source)
        count = count + 1
        extension = os.path.splitext(file_name)[1]
    
        #Adding the count to the new file name and extension
        destination = folder + str(naming_scheme) + "_" + str(count) + str(extension)
        
        
        #Renaming the file
        os.rename(source, destination)
    print('All Files have been renamed successfully...')
    print("New filenames are :\n\n")
    # verify the result
    res = os.listdir(folder)
    print(str(folder) + str(res))
    user_input = input("\n\nDo you want to continue on renaming? (y/n): ")
    while user_input == "y":
        print("Loop restarted again...")
        test()
    else:
        print("Program exited successfully.")
        exit()
        
test()
exit()