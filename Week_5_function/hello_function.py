def greeting(name):  # parameter is set in '()'
    message = f'Hello {name}!!!'  # variables like name will appear grey until set within function.
    return message  # output values by using return


# first function def set above

def main():  # main tells programmer where program starts
    username = 'Sally'
    hello_message = greeting(username)  # providing input to function, created new variable hello_message to give to
    # output
    print(hello_message.upper())


main()  # will call main function here - will 'order' - functions do not do anything unless you call them
