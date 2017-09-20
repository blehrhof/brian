import math 
class complex:
    'this class simulates conplex numbers'
    def __init__(self, real=0 , imag=0):
        if(type(real) not in (int,float)) or type(imag) not in (int,float):
            raise Exception('Args are not numbers!')
        self.__real = real
        self.__imag = imag
    
    def GetReal(self):
        return self.__real
    
    def GetImag(self):
        return self.__imag
    
    def GetModulus(self):
        return math.sqrt(self.GetReal() * self.GetReal() + self.GetImag() * self.GetImag())
    
    def GetPhi(self):
        return math.atan2(self.GetImag(), self.GetReal())
    
    
    def SetReal(self,val):
        if type(val) not in (int,float):
            raise Exception('real part must be a number')
        self.__real=val
    def SetImag(self,val):
        if type(val) not in (int,float):
            raise Exception('imag part must be a number')
        self.__imag=val
    def __str__(self):
        return str(self.GetReal()) + '+' + str(self.GetImag()) + 'i'
    def __add__(self,other):
        return complex(self.GetReal() + other.GetReal(), self.GetImag() + other.GetImag())
    def __mul__(self, other):
        if type(other) in (int,float):
            return complex(self.GetReal() * other, self.GetImag() * other)
        else:
            return complex(self.GetReal() * other.GetReal() - self.GetImag() * other.GetImag(),
            self.GetImag()* other.GetImag() + self.GetReal() * other.GetReal())

a = complex(5,0.3)
b = complex(-3,4)
print(a+b)
print(a*b)


try:
#c = complex(2.5,5.2)
    c=complex(-3,4)
#   c.SetImag(1)
#   c.SetReal((1,2,3))


    print(c.GetModulus(), c.GetPhi())
except Exception as e:
    print(e)

#c=complex((1,2,3),[1,2,3])
#c=complex(2)
#print(c.__real, c.__imag)

