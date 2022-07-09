import time
from sympy.ntheory.factor_ import divisor_sigma
from itertools import count
initial = int(input("Enter two numbers p & q between which Amicable pairs need to be generated\n p = "))
final = int(input("\n q = "))
print("\n")
st = time.time()
def main():
  k=0
  j=1
  ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
  for u in count(initial):
    div_u=divisor_sigma(u)
    v=div_u-u
    if v>u and div_u==divisor_sigma(v):
      if initial<=220:
        print(ordinal(j) + " Amicable pair: (%s,%s)"%(u,v))
        k=1
        j=j+1
      else:
        print("(%s,%s) are amicable numbers "%(u,v))
        k=1
    if u>final:
      break;
  if k==0:
    print("There are no Amicable Numbers in the given range")
  else:
    print("The above numbers are the Amicable pairs generated between %s and %s"%(initial,final))
  et = time.time()
  print('\nExecution time:', et-st, 'seconds')

if __name__ == "__main__":
    main()