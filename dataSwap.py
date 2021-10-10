def dataSwap():

    file1 = input("Enter the first file name that you would like to swap: ")
    file2 = input("Enter the second file name you would like to swap: ")

    with open(file1, 'r') as a:
        data_a = a.read()
        #data from file1 is stored in a
    
    with open(file2, 'r') as c:
        data_c = c.read()
        #data from file2 is stored in c

    with open(file1, 'w+') as a:
        a.write(data_c)
        #data from c is writen in file1
    
    with open(file2, 'w+') as b:
        b.write(data_a)
        #data from a is stored in file2

dataSwap()