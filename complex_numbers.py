class complex_number:
    def __init__(self, real, imag):
        if self.is_valid(real, imag):
            self.real = real
            self.imag = imag
        else:
            raise Exception("Put a valid number")

    def is_valid(self, real_num, imag_num):
        if type(real_num) not in [int, float]:
            return False
        if type(imag_num) not in [int, float]:
            return False
        return True

    def __str__(self) -> str:
        if self.real == 0:
            return str(self.imag) + 'i'
        if self.imag == 0:
            return str(self.real)
        return str(self.real) + " + " + str(self.imag) + "i"
    
    def __add__(self, other_complex_number):
        if type(other_complex_number) != complex_number:
            raise Exception("You can not add an invalid complex number")
        return complex_number(self.real + other_complex_number.real, self.imag + other_complex_number.imag)
    
    def __sub__(self, other_complex_number):
        if type(other_complex_number) != complex_number:
            raise Exception("You can not subtract an invalid complex number")
        return complex_number(self.real - other_complex_number.real, self.imag - other_complex_number.imag)
    
    def __mul__(self , other_complex_number):
        if type(other_complex_number) != complex_number:
            raise Exception("You can not muiltiply an invalid complex number")
        return complex_number(self.real * other_complex_number.imag - other_complex_number.real * self.imag, self.imag * other_complex_number.real + other_complex_number.imag * self.real)