import CCcalc
import CCOld_CCNew


if __name__ == '__main__':
    Vibor = str(input())
    if Vibor == '1':
        num = str(input())
        from_base = int(input())
        to_base = int(input())
        CCOld_CCNew.Main(num, from_base, to_base)
    if Vibor == '2':
        a = str(input())
        a_ = int(input())
        b = str(input())
        b_ = int(input())
        c = str(input())
        CCcalc.Main(a, a_, b, b_, c)