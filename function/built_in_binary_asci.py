#Receive number from user and print equivalent binary
def numbers():              
    number = int(input("Enter number to be converted in to binary: "))
    binary = format(number, 'b')
    print(binary)
    next()

#Receive string, output binary equevalent of each characters on the string separated by double space
def strings():              

    string = input("Enter string to be converted in to binary: ")
    for char in string:
        asci = ord(char)
        binary = format(asci, 'b')
        print(binary, end="  ")
    print()
    next()


#Select if you want to proceed or exit
def next():
    nex = input("'Y' continue 'X' exit: " ).lower()
    
    if nex == "y":
        main()
    else:
        exit()

#The main function where code beginnes
def main():
    choice = input("Data type you want to convert in to binary? 'I' for num 'S' string: ").lower()
    match choice:
        case "i":
            numbers()
        case "s":
            strings()
        case _:
            print("Wrong choice")
main()