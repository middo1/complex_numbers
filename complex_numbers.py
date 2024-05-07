class ComplexNumber:
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
        if self.imag < 0:
            return str(self.real) + " - " + str(abs(self.imag)) + "i"
        return str(self.real) + " + " + str(self.imag) + "i"
    
    def __add__(self, other_complex_number):
        if type(other_complex_number) != ComplexNumber:
            raise Exception("You can not add an invalid complex number")
        return ComplexNumber(self.real + other_complex_number.real, self.imag + other_complex_number.imag)
    
    def __sub__(self, other_complex_number):
        if type(other_complex_number) != ComplexNumber:
            raise Exception("You can not subtract an invalid complex number")
        return ComplexNumber(self.real - other_complex_number.real, self.imag - other_complex_number.imag)
    
    def __mul__(self , other_complex_number):
        if type(other_complex_number) not in [int, ComplexNumber]:
            raise Exception("You can not muiltiply an invalid complex number")
        if type(other_complex_number) == int:
            return ComplexNumber(other_complex_number * self.real, other_complex_number * self.imag)
        return ComplexNumber(self.real * other_complex_number.real - other_complex_number.imag * self.imag, self.imag * other_complex_number.real + other_complex_number.imag * self.real)
    
    def conjugate(self):
        return ComplexNumber(self.real, -1 * self.imag)

    def abs(self):
        return (self * self.conjugate()).real**0.5
    
    def __div__(self, dividend):
        if type(dividend) not in [ComplexNumber]:
            raise Exception("You can not divide a complex number using anything other than an integer and a complex number")
        return self * dividend.conjugate() / dividend * dividend.conjugate()
    
    @staticmethod
    def divide_by(value1: 'int|ComplexNumber', value2: 'int|ComplexNumber') -> 'ComplexNumber':
        return value2.conjugate() * value1 / value2 * value2.conjugate

    
    def __pow__(self, power):
        if self.real == 0:
            pass