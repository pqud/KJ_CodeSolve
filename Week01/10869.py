
def Plus(a,b):
  return a+b

def Minus(a,b):
  return a-b

def Mul(a,b):
  return a*b

def Sub(a,b):
  return a/b

def Remain(a,b):
  return a%b

if __name__=='__main__':
  a, b= input().split()
  print(Plus(a,b))
  print(Minus(a,b))
  print(Mul(a,b))
  print(Sub(a,b))
  print(Remain(a,b))
    
