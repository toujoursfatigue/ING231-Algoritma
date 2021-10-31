def toplam(N):
    if N<2:
        return 1
    else:
        return N+toplam(N-1)
