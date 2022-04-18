def parse(str):
    if str == "I":
        return 1
    elif str == "II":
        return 2
    elif str == "III":
        return 3
    elif str == "IV":
        return 4
    elif str == "V":
        return 5
    elif str == "VI":
        return 6
    elif str == "VII":
        return 7
    elif str == "VIII":
        return 8
    elif str == "IX":
        return 9
    elif str == "X":
        return 10
    elif str == "XI":
        return 11
    # if str == 'I':
    #     return 1
    # elif str == 'V':
    #     return 5
    # elif str == 'X':
    #     return 10
    elif str == 'L':
        return 50
    elif str == 'C':
        return 100
    elif str == 'D':
        return 500
    # new_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    # total = 0

    # for i in range(len(str)):
    #     print(str[i])
    #    total += new_dict[i]
    # return total


print(parse("XII"))
print(parse("IX"))   
