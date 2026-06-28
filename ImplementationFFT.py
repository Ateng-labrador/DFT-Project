import cmath


def myFFT(x):
    # rekrusi
    N = len(x)
    if N == 1:
        return x
    even = myFFT(x[::2])
    odd = myFFT(x[1::2])
    result = [0] * N

    for k in range(N//2):
        W = cmath.exp(-2j * cmath.pi * k / N)
        result[k] = even[k] + W * odd[k]
        result[k+N//2] = even[k] - W*odd[k]
    
    return result

