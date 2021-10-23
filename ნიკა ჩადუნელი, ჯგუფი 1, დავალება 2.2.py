
#in string invertes ones to zeros and vise versa
def invert(binary:str) -> str:
    trans = binary.maketrans('01','10')
    binary = binary.translate(trans)

    return binary  

#adds two binary number, returns error if given bits aren't enough to display the result
def binary_add(a,b) -> str:
    a_len = len(a)
    b_len = len(b)
    if a_len > b_len:
        b = '0'*(a_len-b_len)+b
    elif b_len > a_len:
        b = '0'*(b_len-a_len)+a    

    a, b = a[::-1], b[::-1]
    result = ''
    carry = 0
    for i in range(a_len):
        if a[i]=='1' and b[i] =='1' and carry== 1:
            result+='1'
            carry = 1
        if a[i]=='1' and b[i] =='1':
            result += '0'
            carry = 1
        elif (a[i]=='1' or b[i] =='1') and carry == 1:
            result+='0'
            carry = 1     
        elif a[i]=='1' or b[i] =='1':
            result+='1'
            carry = 0 
        elif carry ==1 :
            result+='1'
            carry = 0
        else:result+='0'

    return result[::-1] if len(result) == a_len else 'Overflow: not enough bits to display result'              

#converts decimal number into signed magnitude system
def decimal_to_sign_magn(num: int, bit_num: int=4) -> str:
    
    if abs(num) > 2**(bit_num-1):
        return 'not enough bits to display result'
    
    if num == 0:return '0'* bit_num, '1'+'0'*bit_num-1   
    result = ['0']* bit_num    
    result[-1] = '1' if num < 0 else '0'  #determine first bit of final result 
    num = abs(num)

    for i in range(len(result)-1):
        result[i] = str(num %2)
        num//=2

    return ''.join(result[::-1])

#converts decimal number into one's complement system
def decimal_to_ones_compl(num: str, bit_num: int=4) -> str:
    if abs(num) > 2**(bit_num-1):
        return 'not enough bits to display result'
    
    if num == 0:return '0'* bit_num, '1'+'0'*(bit_num-1)   
    result = ['0']* bit_num
    negative = True if num < 0 else False
    num = abs(num)

    for i in range(len(result)-1):
        result[i] = str(num %2)
        num//=2

    result = ''.join(result[::-1]) 
    if negative: 
        result = invert(result)

    return result

#converts decimal number into two's complement system
def decimal_to_twos_compl(num: int, bit_num: int=4) -> str:
     
    result = decimal_to_ones_compl(num, bit_num)
    if num > 0: result = binary_add(result, '1') #adds one bit to already inverted result if negative

    return result

#converts decimal number into excess system
def decimal_to_excess(num: int, bit_num: int = 4) -> str:
    result = decimal_to_twos_compl(num, bit_num)
    result = invert(result[0])+result[1:] #changes first bit

    return result

#converts signed magnitude into one's complement and vise versa
def sign_magn_and_ones_compl(num:str) -> str:
    if num[0] == '1':
        num = '0'+num[1:]
        return invert(num)

    return num    

#converts sign magitude into two's complement and vise versa
def sign_magn_and_twos_compl(num:str) -> str:
    
    if num[0]=='1':
        num = '0'+num[1:]
        num = invert(num)
        return binary_add(num,'1')
    else:
        return num    

#converts signed magnitude into excess
def sign_magn_to_excess(num:str) -> str:
    
    num = sign_magn_and_twos_compl(num)
    first_bit = invert(num[0])
    return first_bit + num[1:]

#converts one's complement into two's complement
def ones_compl_to_twos_compl(num:str) -> str:
    if num[0]=='1': 
        return binary_add(num,'1')   #adds 1 if number is negative
    return num

#converts one's complemet into excess
def ones_compl_to_excess(num:str) -> str:
    if num[0] == '1':
        return '0' + binary_add(num[1:],'1')   #adds 1 if number is negative
    return'1' + num[1:] 

#converts two's complemet into one's complement
def twos_compl_to_ones_compl(num:str) -> str:
    return sign_magn_and_ones_compl(sign_magn_and_twos_compl(num))

#converts twos'compelemt into excess and vise versa
def twos_compl_and_excess(num: str) -> str:

    return invert(num[0]) + num[1:]

#converts excess into signed magnitude
def excees_to_sign_magn(num: str) -> str:
    if num[0] == '0':
        return binary_add(invert(num),'1')   #adds 1 if number is negative

    return invert(num[0])+num[1:] #inverts first bit 

#converts xcess into one's complement
def excess_to_ones_compl(num: str) -> str:
    return sign_magn_and_ones_compl(excees_to_sign_magn(num))

def main():

    while True:
        
        print('\n')
        choices = ["Decimal.","Signed magnitude.", "One's complement.","Two's complement.","Excess." ]
        
        for i,j in enumerate(choices,1):
            print(f'{i}. {j}')
        
        choice = input('\nChoose from above: ')

        if choice == '1':

            num = int(input('\nEnter decimal number: '))
            bit_num = int(input('Enter number of bits: '))
            choices.pop(0)
            
            for i,j in enumerate(choices,1):
                print(f'{i}. {j}')

            choice = input('\nChoose system to convert decimal into: ')    
            
            if choice == '1':
                print(f'Decimal to signed magnitude -> {decimal_to_sign_magn(num, bit_num)}')
            elif choice =='2':
                print(f"Decimal to Ones'complement -> {decimal_to_ones_compl(num, bit_num)}")
            elif choice =='3':
                print(f"Decimal to Two's complement -> {decimal_to_twos_compl(num, bit_num)}")
            elif choice =='4':
                print(f'Decimal to Excess -> {decimal_to_excess(num, bit_num)}')
            else: print('--------------wrong number--------------')  


        elif choice == '2':

            num = input('Enter number in Signed Magnitude system: ')
            choices.pop(0)
            choices.pop(0)
            
            for i,j in enumerate(choices,1):
                print(f'{i}. {j}')

            choice = input('\nChoose system to convert Signed Magnitude into: ')    
            
            if choice == '1':
                print(f"signed magnitude to One's complement -> {sign_magn_and_ones_compl(num)}")
            elif choice =='2':
                print(f"Signed Magnitude to Two's complement-> {sign_magn_and_twos_compl(num)}")
            elif choice =='3':
                print(f'Signed Magnitude to Excess -> {sign_magn_to_excess(num)}')
            else: print('--------------wrong number--------------') 

        elif choice == '3':

            num = input("\nEnter number in One's complement system: ")
            choices.pop(0)
            choices.pop(1)
            
            for i,j in enumerate(choices,1):
                print(f'{i}. {j}')

            choice = input("\nChoose system to convert Ones's Comlement  into:")    
            
            if choice == '1':
                print(f"One's complement to Signed Magnitude  -> {sign_magn_and_ones_compl(num)}")
            elif choice =='2':
                print(f"One's complement to Two's complement-> {ones_compl_to_twos_compl(num)}")
            elif choice =='3':
                print(f"One's complement to Excess -> {ones_compl_to_excess(num)}")
            else: print('--------------wrong number--------------')

        elif choice == '4':

            num = input("\nEnter number in Two's complement system: ")
            choices.pop(0)
            choices.pop(2)

            for i,j in enumerate(choices,1):
                print(f'{i}. {j}')

            choice = input("\nChoose system to convert Two's Comlement  into:") 

            if choice == '1':
                print(f"Two's complement to Signed Magnitude  -> {sign_magn_and_twos_compl(num)}")
            elif choice =='2':
                print(f"Two's complement to One's complement -> {twos_compl_to_ones_compl(num)}")
            elif choice =='3':
                print(f"Two's complement to Excess -> {twos_compl_and_excess(num)}")
            else: print('--------------wrong number--------------')

        elif choice == '5':
            num = input("\nEnter number in Excess system: ")
            choices.pop(0)
            choices.pop(3)

            for i,j in enumerate(choices,1):
                print(f'{i}. {j}')
            
            choice = input("\nChoose system to convert Excess  into:")  

            if choice == '1':
                print(f"Excess to Signed Magnitude  -> {excees_to_sign_magn(num)}")
            elif choice =='2':
                print(f"Excess to One's complement -> {excess_to_ones_compl(num)}")
            elif choice =='3':
                print(f"Excess to Two's complement -> {twos_compl_and_excess(num)}")
            else: print('--------------wrong number--------------')

        else: print('-------wrong number-------')   


if __name__ == "__main__":
    main()