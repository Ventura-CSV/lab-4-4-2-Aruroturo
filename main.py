def main():
    while True:
        try:
            Person = int(input("Number: "))
            number = float(Person)
        except ValueError:
            print("Input must be numeric")
        else:
            print(number)
            break
    """
    ########################################
    Code Your Program here
    ########################################
    """
    
    
    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
