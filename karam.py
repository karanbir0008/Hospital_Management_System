import sys

class Conversion:

    def _init_(self,number,initial_base,target_base):
        self.number  = number
        self.initial_base  = initial_base
        self.target_base  = target_base

        self.binary_numbers_four_digit = ["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]
        self.binary_numbers_three_digit = ["000","001","010","011","100","101","110","111"]
        self.binary_numbers_two_digit = ["00","01","10","11"]

        self.octal_equivalent_four_digit = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        self.octal_equivalent_three_digit = ["0","1","2","3","4","5","6","7"]
        self.octal_equivalent_two_digit = ["0","1","2","3"]

        self.hexa_alpha_after_nine = ['A','B','C','D','E','F']
        self.hexa_num_after_nine = ["10","11","12","13","14","15"]

    
    def int_split_list(self):
        if '.' in self.number:
        else:
            int_part_str = self.number
            frac_part_str = ''  

        self.int_part_list = [int(d) for d in int_part_str]
        self.frac_part_list = [int(d) for d in frac_part_str]
    
    def str_split_list(self):
        if '.' in self.number:
            int_part_str, frac_part_str = self.number.split('.')
        else:
            int_part_str = self.number
            frac_part_str = ''  

        self.int_part_in_str_list = [str(d) for d in int_part_str]
        self.frac_part_in_str_list = [str(d) for d in frac_part_str]

        self.len_int_part_in_str_list = len(self.int_part_in_str_list)
        self.len_frac_part_in_str_list = len(self.frac_part_in_str_list)

    
    def direct_split(self):
        
        self.number = float(self.number)
        self.int_part = int(self.number) 
        self.quotient = int(self.int_part)
        frac_part = float(self.number-self.int_part)
        self.frac_part = round(frac_part,4)
        self.temp_frac_part = frac_part
    

    def decimal_to_binary_and_octal(self):

        self.direct_split()

        remainder=str()

        while self.target_base<=self.quotient:
            remainder += str(self.quotient % self.target_base)
            self.quotient = int(self.quotient/self.target_base)

        remainder = remainder+str(self.quotient)
        binary_int_part = "".join(reversed(remainder))


        binary_frac_part=str()


        i=0
        while i<3:
            sub_temp_frac_part = self.temp_frac_part*self.target_base
            sub_int_part = int(sub_temp_frac_part)
            sub_frac_part = float(sub_temp_frac_part-sub_int_part) 
            sub_frac_part = round(sub_frac_part,2) 
   
            binary_frac_part += str(sub_int_part)
            sub_frac_part = float(sub_frac_part)
            self.temp_frac_part = sub_frac_part
            i+=1

        decimal_to_binary_or_octal_equivalent = binary_int_part+"."+binary_frac_part
        print(decimal_to_binary_or_octal_equivalent)


    def binary_to_decimal(self):
    
            
            int_result = 0
            int_exponent=0
            frac_result = 0
            frac_exponent=-1
            
            self.int_split_list()
            for val in reversed(self.int_part_list):
                
                if val!=0 and val!=1:
                    print("Entered number is not of base 2 (binary number).... ")
                    sys.exit()
                
                else:
                    int_result += pow(self.initial_base,int_exponent)*val
                    int_exponent+=1

            for val in (self.frac_part_list):
                
                if val!=0 and val!=1:
                    print("Entered number is not of base 2 (binary number).... ")
                    sys.exit()
                
                else:    
                    frac_result += pow(self.initial_base,frac_exponent)*val
                    frac_exponent-=1
        
            binary_to_decimal_equivalent = int_result+frac_result
            print(binary_to_decimal_equivalent)


    def binary_to_hexadecimal(self):
        self.str_split_list()
        
        int_part_result=0

        remainder_int_part = int(self.len_int_part_in_str_list%4)
        groups_int_part  = int(self.len_int_part_in_str_list/4)      # Calculating groups
        hexa_int_part = str()

        remainder_frac_part = int(self.len_frac_part_in_str_list%4)
        groups_frac_part  = int(self.len_frac_part_in_str_list/4)    # Calculating groups
        hexa_frac_part = str()

        k=0
        while k!=groups_int_part:
            i=0
            while i < 16:
                j=0
                if self.len_int_part_in_str_list>remainder_int_part:
                    if self.int_part_in_str_list[self.len_int_part_in_str_list-4]==self.binary_numbers_four_digit[i][j] and self.int_part_in_str_list[self.len_int_part_in_str_list-3]==self.binary_numbers_four_digit[i][j+1] and self.int_part_in_str_list[self.len_int_part_in_str_list-2]==self.binary_numbers_four_digit[i][j+2] and self.int_part_in_str_list[self.len_int_part_in_str_list-1]==self.binary_numbers_four_digit[i][j+3]:
                        hexa_int_part += self.octal_equivalent_four_digit[i]
                        del self.int_part_in_str_list[-4:]
                    self.len_int_part_in_str_list = len(self.int_part_in_str_list)
                i+=1
            k+=1




        if self.len_int_part_in_str_list == 1:
            hexa_int_part += self.int_part_in_str_list[0]



        elif self.len_int_part_in_str_list==2:
            i=0
            while i<4:
                j=0
                if self.int_part_in_str_list[0]==self.binary_numbers_two_digit[i][j] and self.int_part_in_str_list[1]==self.binary_numbers_two_digit[i][j+1]:
                    hexa_int_part+=self.octal_equivalent_two_digit[i]
                    break
                i+=1


        elif self.len_int_part_in_str_list==3:
            i=0
            while i<8:
                j=0   
                if self.int_part_in_str_list[0]==self.binary_numbers_three_digit[i][j] and self.int_part_in_str_list[1]==self.binary_numbers_three_digit[i][j+1] and self.int_part_in_str_list[2]==self.binary_numbers_three_digit[i][j+2]:
                    hexa_int_part+=self.octal_equivalent_three_digit[i]
                    break
                i+=1

        int_part_result = hexa_int_part[::-1]





        k=0
        while k!=groups_frac_part:
            i=0
            while i < 16:
                j=0
                if self.len_frac_part_in_str_list>remainder_frac_part:
                    if self.frac_part_in_str_list[0]==self.binary_numbers_four_digit[i][j] and self.frac_part_in_str_list[1]==self.binary_numbers_four_digit[i][j+1] and self.frac_part_in_str_list[2]==self.binary_numbers_four_digit[i][j+2] and self.frac_part_in_str_list[3]==self.binary_numbers_four_digit[i][j+3]:
                        hexa_frac_part += self.octal_equivalent_four_digit[i]
                        del self.frac_part_in_str_list[:4]
                self.len_frac_part_in_str_list = len(self.frac_part_in_str_list)
                i+=1
            k+=1



# Calculating Fractional Part If one Element is present
        if self.len_frac_part_in_str_list==1:
            self.frac_part_in_str_list.extend(["0"]*3)
            i=0
            while i<16:
                j=0
                if self.frac_part_in_str_list[0]==self.binary_numbers_four_digit[i][j] and self.frac_part_in_str_list[1]==self.binary_numbers_four_digit[i][j+1] and self.frac_part_in_str_list[2]==self.binary_numbers_four_digit[i][j+2] and self.frac_part_in_str_list[3]==self.binary_numbers_four_digit[i][j+3]:
                    hexa_frac_part+=self.octal_equivalent_four_digit[i]
                i+=1

# Calculating Int Part If two Elements are present
        elif self.len_frac_part_in_str_list==2:
            self.frac_part_in_str_list.extend(["0"]*2)
            i=0
            while i<16:
                j=0
                if self.frac_part_in_str_list[0]==self.binary_numbers_four_digit[i][j] and self.frac_part_in_str_list[1]==self.binary_numbers_four_digit[i][j+1] and self.frac_part_in_str_list[2]==self.binary_numbers_four_digit[i][j+2] and self.frac_part_in_str_list[3]==self.binary_numbers_four_digit[i][j+3]:
                    hexa_frac_part+=self.octal_equivalent_four_digit[i]
                i+=1

# Calculating Int Part If Three Elements are present
        elif self.len_frac_part_in_str_list==3:
            self.frac_part_in_str_list.append("0")
            i=0
            while i<16:
                j=0
                if self.frac_part_in_str_list[0]==self.binary_numbers_four_digit[i][j] and self.frac_part_in_str_list[1]==self.binary_numbers_four_digit[i][j+1] and self.frac_part_in_str_list[2]==self.binary_numbers_four_digit[i][j+2] and self.frac_part_in_str_list[3]==self.binary_numbers_four_digit[i][j+3]:
                    hexa_frac_part+=self.octal_equivalent_four_digit[i]
                i+=1

        if self.len_frac_part_in_str_list==0:
            result = int_part_result
        elif self.len_int_part_in_str_list==0:
            result = "0."+hexa_frac_part
        else:
            result = int_part_result+"."+hexa_frac_part


        print("Ewuivalent hexadecimal number is : ",result)

    

    def decimal_to_hexadecimal(self):

        self.direct_split()
        remainder=str()
        temp_remainder=str()
        
        while self.target_base<=self.quotient:
            temp_remainder = str(self.quotient % self.target_base)
            i=0
            while i<6:
                if temp_remainder == self.hexa_num_after_nine[i]:
                    temp_remainder = self.hexa_alpha_after_nine[i]
                i+=1
            remainder += temp_remainder
            self.quotient = int(self.quotient/self.target_base)


        self.quotient  = str(self.quotient)

        i=0
        while i<6:
            if self.quotient == self.hexa_num_after_nine[i]:
                self.quotient = self.hexa_alpha_after_nine[i]
            i+=1


        remainder = remainder+self.quotient
        hexa_int_part = "".join(reversed(remainder))


        hexa_frac_part=str()
        temp_hexa_frac_part=str()
        i=0
        while i<3:
    
            sub_temp_frac_part = self.frac_part*self.target_base
            sub_int_part = int(sub_temp_frac_part)
            sub_frac_part = float(sub_temp_frac_part-sub_int_part) 
            sub_frac_part = round(sub_frac_part,2) 
            temp_hexa_frac_part = str(sub_int_part)
   
            j=0
            while j<6:
                if temp_hexa_frac_part == self.hexa_num_after_nine[j]:
                    temp_hexa_frac_part = self.hexa_alpha_after_nine[j]
                j= j+1
  
            hexa_frac_part += temp_hexa_frac_part
            sub_frac_part = float(sub_frac_part)
            self.frac_part = sub_frac_part
            i+=1

        print("Binary equivalent is : ",hexa_int_part + "." + hexa_frac_part)

  
    def hexadecimal_to_binary(self):
        self.str_split_list()
        
        bianry_int_part = str()

        i=0
        while i <self.len_int_part_in_str_list:
            j=0
            while j<16:
                if self.int_part_in_str_list[i]==self.octal_equivalent_four_digit[j]:
                    bianry_int_part += self.binary_numbers_four_digit[j]
                j+=1
            i+=1

        binary_frac_part = str()

        i=0
        while i <self.len_frac_part_in_str_list:
            j=0
            while j<16:
                if self.frac_part_in_str_list[i]==self.octal_equivalent_four_digit[j]:
                    binary_frac_part += self.binary_numbers_four_digit[j]
                j+=1
            i+=1

        if self.len_frac_part_in_str_list==0:
            result = bianry_int_part
        elif self.len_int_part_in_str_list==0:
            result = "0."+binary_frac_part
        else:
            result = bianry_int_part+"."+binary_frac_part

        print(result)


    def hexadecimal_to_decimal(self):
        self.str_split_list()
        int_exponent = 0
        frac_exponent = -1
        int_result = 0
        frac_result = 0
        i=0
        while i<self.len_int_part_in_str_list:
            j=0
            while j<6:
                if self.int_part_in_str_list[i]==self.hexa_alpha_after_nine[j]:
                    self.int_part_in_str_list[i]=self.hexa_num_after_nine[j]
                j=j+1
            i=i+1    

        i=0
        while i<self.len_frac_part_in_str_list:
            j=0
            while j<6:
                if self.frac_part_in_str_list[i]==self.hexa_alpha_after_nine[j]:
                    self.frac_part_in_str_list[i]=self.hexa_num_after_nine[j]
                j=j+1
            i=i+1    
 
        int_part = [int(d) for d in self.int_part_in_str_list]
        frac_part = [int(d) for d in self.frac_part_in_str_list]
    
        for val in reversed(int_part):
            int_result += pow(self.initial_base,int_exponent)*val
            int_exponent+=1

        for val in (frac_part):
            frac_result += pow(self.initial_base,frac_exponent)*val
            frac_exponent-=1

        decimal = int_result+frac_result
        print("Decimal equivalent is : ",decimal)


    def octal_to_binary(self):
        self.str_split_list()
        
        bianry_int_part = str()

        i=0
        while i <self.len_int_part_in_str_list:
            j=0
            while j<8:
                if self.int_part_in_str_list[i]==self.octal_equivalent_three_digit[j]:
                    bianry_int_part += self.binary_numbers_three_digit[j]
                j+=1
            i+=1


        binary_frac_part = str()

        i=0
        while i <self.len_frac_part_in_str_list:
            j=0
            while j<8:
                if self.frac_part_in_str_list[i]==self.octal_equivalent_three_digit[j]:
                    binary_frac_part += self.binary_numbers_three_digit[j]
                j+=1
            i+=1

        if self.len_frac_part_in_str_list==0:
            result = bianry_int_part
        elif self.len_int_part_in_str_list==0:
            result = "0."+binary_frac_part
        else:
            result = bianry_int_part+"."+binary_frac_part

        print(result)

    
    def octal_to_decimal(self):
        self.int_split_list()
        
        int_exponent = 0
        frac_exponent = -1
        int_result = 0
        frac_result = 0

        for val in reversed(self.int_part_list):
            int_result += pow(self.initial_base,int_exponent)*val
            int_exponent+=1

        for val in (self.frac_part_list):
            frac_result += pow(self.initial_base,frac_exponent)*val
            frac_exponent-=1

        decimal = int_result+frac_result
        print("Decimal equivalent is : ",decimal)


number = input("Enter the number : ")
initial_base = int(input("Enter the initial base : "))
target_base = int(input("Enter the taeget base : "))
obj = Conversion(number,initial_base,target_base)

if initial_base == 2 and target_base == 10:
    obj.binary_to_decimal()

elif initial_base == 10 and (target_base == 2 or target_base==8):
    obj.decimal_to_binary_and_octal()

elif initial_base == 10 and target_base == 16:
    obj.decimal_to_hexadecimal()

elif initial_base == 16 and target_base == 2:
    obj.hexadecimal_to_binary()

elif initial_base == 16 and target_base == 10:
    obj.hexadecimal_to_decimal()

elif initial_base == 8 and target_base == 2:
    obj.octal_to_binary()

elif initial_base == 8 and target_base == 10:
    obj.octal_to_decimal()

elif initial_base == 2 and target_base == 16:
    obj.binary_to_hexadecimal()