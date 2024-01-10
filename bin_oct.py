
def bin_to_oct(binary_string:str)->str:
    """

    """
    split_str = binary_string.split('.')

    if len(split_str)==1:
        l_dec = split_str[0]
        r_dec = None
        if len(l_dec) == 0:
            raise ValueError('The input is empty')
    elif len(split_str)== 2:
        l_dec = split_str[0]
        r_dec = split_str[1]
        if len(r_dec) == 0:
           r_dec = None
    else:
        raise ValueError(' There can only be one period(.) in the binary number')


    octal_dict = {'000':'0', '001':'1','010':'2',
                  "011": "3" ,"100": "4","101": "5",
                  "110": "6", "111": "7" }

    ## In case the number of bits isn't completely divisible by 3
    extra_zeros = ['0','00']

    l_oct = list()
    if len(l_dec)%3!=0:
        rem = len(l_dec)%3
        l_dec = ''.join([extra_zeros[rem-1],l_dec])

    for i in range(len(l_dec)//3):
        b = l_dec[3*i:3*(i+1)]
        if b not in octal_dict:
            print(b)
            raise ValueError("The String input isn't exactly a binary string")
        l_oct.append(octal_dict[b])

    left_octal = ''.join(l_oct)
    right_octal = None
    if r_dec is not None:

        r_oct = ['.']
        if len(r_dec)%3!=0:
            rem = len(r_dec)%3
            r_dec = ''.join([r_dec,extra_zeros[rem-1]])

        for i in range(len(r_dec)//3):
            b = r_dec[3*i:3*(i+1)]
            if b not in octal_dict:
                raise ValueError("The String input isn't exactly a binary string")
            r_oct.append(octal_dict[b])

        right_octal = ''.join(r_oct)



    if right_octal is None:
        return left_octal

    octstr = ''.join([left_octal,right_octal])
    return octstr

if __name__ == '__main__':
    binstr = input('Input a Binary String:')
    print(f'The octal representation of the binary number {binstr} is: {bin_to_oct(binstr)}')
