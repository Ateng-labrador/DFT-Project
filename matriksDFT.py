import cmath

def dft_matriks(N):
    res = []
    # indeks baris
    for k in range(N):
        row = []
        # indeks kolom
        for n in range(N):
            W = cmath.exp(-1j * 2 * cmath.pi * k * n / N)
            row.append(W)
        res.append(row)
    return res


def dft(x):
    res = [0] * len(x)
    matriks = dft_matriks(len(x))
    for k in range(len(x)):
        for n in range(len(matriks[0])):
            res[k] += matriks[k][n] * x[n]
    return res

def fft(x):
    pass

if __name__ == "__main__":
    x = [1, 2 , 3, 4, 5, 6]
    y = dft(x)
    for i in y:
        print(i)
