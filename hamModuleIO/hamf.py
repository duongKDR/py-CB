def phep_chia(a, b):
   return a / b
c = 300
d = 100
print("Kết quả của phép chia là:",phep_chia(c, d))



def vidu():
    "vi du cong"
    print("cong 3+4" ,3+4)

vidu()
print(vidu.__doc__)

def giathua (n):
  giathua = 1
  for i in range( 1,n+1,1):
    giathua *= i
  return giathua
  
# x= int(input("x = " ))
  
# e_nu = 0
# for i in range(30):
#   e_nu +=  x**i/giathua(i)
# res=e_nu/(1+e_nu)
# print("Sigmoid({0})= {1}".format(x,res))
length = len(string)
print(length)  # In ra 13