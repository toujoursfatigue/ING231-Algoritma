def fact(N):
    if N<2:
        return 1
    else:
        return N*fact(N-1)
