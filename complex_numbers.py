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
        return str(self.real) + ' + ' + str(self.imag) + "i"
     