import os

print("Python Program started")
count = 0

def test():
    global count
    print("NOTE: Need to have proper path examples like C:/Users/Hafiz Jasmi/Desktop/testing/ ")
    folder = input("Please input the path of the folder : \n")
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
    count = 0  ##Reset back the count
    test()
    user_input1 = input("\n\nDo you want to continue on renaming? (y/n): ")
    if user_input1 == "y":
        count = 0  ##Reset back the count
        test()
    else:
        print("Program is exiting gracefully...")
        exit(0)
else:
    print("Program exited successfully.")
    exit()
