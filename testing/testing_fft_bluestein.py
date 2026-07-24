import numpy as np
import fftModule as fM
import unittest

class testingbluestein(unittest.TestCase):
    N = np.linspace(0, 2 * np.pi, 1000)
    a = np.mgrid[:5, :5][0]
    A = np.sin(N)
    def testbluestein(self):
        B = fM.fft.bluestein(self.A)
        res = np.fft.fft(self.A)
        np.testing.assert_allclose(B, res, atol=1e-7, rtol=1e-7)
    
    def bluestein2d(self):
        b = fM.fft.bluestein2d(self.a)
        res = np.fft.fft2(self.a)
        np.testing.assert_allclose(b, res, rtol=1e-7, atol=1e-7)
