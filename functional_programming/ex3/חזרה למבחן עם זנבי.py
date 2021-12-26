from functional_programming.ex3.tailrecurse import *


def helper(Seq, d):
    return help1(Seq, [], d)


def help2(seqout):
    return [seqout[i].lower() for i in range(len(seqout))]


def impf(Seq):
    d = {'a': 'T', 't': 'A', 'g': 'C', 'c': 'G'}
    seqout = helper(Seq, d)
    seqout = help2(seqout)
    return "".join(seqout)

@tail_call_optimized
def help1(Seq, Acc, d):
    if len(Seq) == 0:
        return Acc
    elif not Seq[0] in d:
        return []
    else:
        return help1(Seq[1:], Acc + [d[Seq[0]]], d)





def main():
    seq = input("please insert a sequence\n")
    print(impf(seq))


if __name__ == "__main__":
    main()
