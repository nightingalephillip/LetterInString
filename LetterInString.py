string_is = "The string is"
aString = "      The purpose of this program assignment is to practice how to use for loop and if-else statement."

print(string_is)
print(aString)

target_o = "o"
target_s = "s"
o = 0   #setting this variable to 0 so I can add 1 every time "o" occurs
s = 0   #setting this variable to 0 so I can add 1 every time "o" occurs

for i in range(len(aString)):                                   # for each index
    if aString[i] == target_o.lower():                          # check if the target is found
        print("'o' character occurs in index: ", i)             # prints index where 'o' occurs
        o += 1                                                  # adding 1 to variable o every time aString[i] == target_o
print("There are {} 'o' characters.".format(str(o)))            # formatting {} with the value of o variable
print("*****************************************\n")            # print new line to make space

for i in range(len(aString)):                                   # for each index
    if aString[i] == target_s.lower():                          # check if the target is found                                                 #
        print("'s' character occurs in index: ", i)             # prints index where 's' occurs
        s += 1                                                  # adding 1 to variable s every time aString[i] == target_s
print("There are {} 's' characters.".format(str(s)))            # formatting {} with the value of s variable
print("*****************************************")              # print ***
print("There are {} characters in the string".format(str(len(aString))))   # print format how many characters in string
