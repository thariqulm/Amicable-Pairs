import time
from sympy.ntheory.factor_ import divisor_sigma

initial = int(
    input(
        "Enter two numbers p & q between which Amicable pairs need to be generated\n p = "
    ))
final = int(input("\n q = "))
d = 0
div_u = 0
print(" ")
st = time.time()

def v_temp(h):
    global d, div_u
    div_u = divisor_sigma(h)
    d = div_u - h
    return d


def main():
    global d, div_u
    ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(n // 10 % 10 != 1) *
                                                (n % 10 < 4) * n % 10::4])
    Amicable = list((w, d) for w in range(initial, final + 1)
                    if v_temp(w) > w and div_u == divisor_sigma(d))
    if len(Amicable) == 0:
        print("There are no Amicable Numbers in the given range")
    elif 220 in Amicable[0]:
        k = 1
        for i in iter(Amicable):
            print(ordinal(k) + " Amicable pair: " + str(i))
            k = k + 1
        print(
            "The above numbers are the Amicable pairs generated between %s and %s"
            % (initial, final))
    elif 220 not in Amicable[0]:
        for i in iter(Amicable):
            print(" Amicable pair: " + str(i))
        print(
            "The above numbers are the Amicable pairs generated between %s and %s"
            % (initial, final))
    et = time.time()
    print('\nExecution time:', et - st, 'seconds')


if __name__ == "__main__":
    main()
