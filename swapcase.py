def swap_case(s):
    a=''
    for letter in s:
        if letter.isupper()== True:
            a+=letter.lower()
        elif letter.islower()== True:
            a+=letter.upper()
        else:
            a+=letter
    return a
            

    return

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
