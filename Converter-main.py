import converter

user_input=input("(1) Decimal\n(2) Binary\n(3) Hexadecimal\n(q) quit\n")

while user_input!="q":
    if user_input=="1":
        print()
        dec_input=input("Enter a decimal number (Enter q to quit): ")
        while dec_input!="q":
            print("Binary: "+converter.decimal.binary(dec_input))
            print("Hexadecimal: "+converter.decimal.hexadecimal(dec_input))
            print()
            dec_input=input("Enter a decimal number (Enter q to quit): ")
    elif user_input=="2":
        print()
        bin_input=input("Enter a binary number (Enter q to quit): ")
        while bin_input!="q":
            print("Decimal: "+converter.binary.decimal(bin_input))
            print("Hexadecimal: "+converter.binary.hexadecimal(bin_input))
            print()
            bin_input=input("Enter a binary number (Enter q to quit): ")
    elif user_input=="3":
        print()
        hex_input=input("Enter a hexadecimal number (Enter q to quit): ")
        while hex_input!="q":
            print("Binary: "+converter.hexadecimal.binary(hex_input))
            print("Decimal: "+converter.hexadecimal.decimal(hex_input))
            print()
            hex_input=input("Enter a hexadecimal number (Enter q to quit): ")
    user_input=input("(1) Decimal\n(2) Binary\n(3) Hexadecimal\n(q) quit\n")
    print()
