import unittest

main_components = {1 : "I", 5: "V", 10: "X", 50: "L"}

def arabske_na_rimske(ar):
    return main_components[ar]



class TestArabskeNaRimske(unittest.TestCase):
    def test_main_components(self):
        self.assertEqual(arabske_na_rimske(1), "I")
        self.assertEqual(arabske_na_rimske(5), "V")
        self.assertEqual(arabske_na_rimske(10), "X")
        self.assertEqual(arabske_na_rimske(50), "L")