# function to convert decimal to binary
def decimaltobinary(response):
    binary = []
    i = 0
    while response//2 > 0:
        y = str(response%2)
        binary.insert(i, y)
        response = response//2
        i += 1
    i += 1
    response = str(response)
    binary.insert(i,response)
    cont = len(binary)
    if cont <= 4:
        x = 4 - cont
        while x > 0:
            i += 1
            binary.insert(i,"0")
            x -= 1
    binary = binary[::-1]
    text = "".join(binary)
    return text

# function to convert binary to decimal
def binarytodecimal(binary):

    decimal = 0
    length = len(binary)
    for i in range(length):
        decimal += int(binary[i]) * (2 ** (length - i - 1))
    return decimal

# funcition to convert binary to text
def binarytotext(binary):
    decimal = binarytodecimal(binary)
    text = chr(decimal)
    return text

print("\nHi, I'm bot and convert binary to text/decimal or text/decimal to bianary\n")
restart = 'Y'
while restart != 'N':
    op = input("\n1 - Decimal/Text -> Binary\n2 - Binary -> Decimal\n3 - Binary -> Text\n\nOption: ")
    if op == "1":
        response = input("\n\nWhat's the number or text you want to convert: ")
        if response.isdigit():
            response = int(response)
            result = decimaltobinary(response)
            print("\n" + result)
        else:
            final = ''
            if len(response) > 1:
                for x in response:
                    result = decimaltobinary(ord(x))
                    final += (result + " ")
                print('\nYour result is: ' + final)
            else:
                final = decimaltobinary(ord(response))
                print('\nYour result is: ' + final)
    elif op == "2":
        response = str(input("\n\nWhat's the binary you want to convert: "))
        response = binarytodecimal(response)
        print("\nYour number in decimal is: " + str(response))
    elif op == "3":
        response = str(input("\n\nWhat's the binary you want to convert: "))
        x = response.split()
        final = ''
        for x in x:
            response = binarytotext(x)
            final += response
        print("\nYour number in text is: " + str(final))
    else:
        print("\nThis isn't an option!\nChoose a valid option")
    restart = input("\nDo you want convert other number? Y/N: ")
    if restart.lower() not in ['y', 'yes', 'n', 'no']:
        restart = input("\nThis option does not exist, please enter an existing option, Y = yes or N = no\n\nDo you want convert other number? Y/N: ")
print('\nThanks for using the bot\n')