name = input('Enter your name: ') # asking the user for their name, variable may change

for letter in name:  # counting loops - repeat once for each letter in a string
    # this code is part of the loop and repeated
    print(letter.upper())  # print that letter, making it print in uppercase regardless

# print message to the user here
# any code here is after the loop and happens one time
print('That was your name vertically, ' + name + '. Thanks for using this program!')  # added + name + here, due to the
# variable being non-consistent/not set
