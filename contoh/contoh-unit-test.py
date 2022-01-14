import unittest


class TestStringMethods(unittest.TestCase):

    def test_strip(self):
        self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')

    def test_isalnum(self):
        self.assertTrue('c0d1ng'.isalnum())
        self.assertFalse('c0d!ng'.isalnum())

    def test_index(self):
        s = 'dicoding'
        self.assertEqual(s.index('coding'), 2)
        # cek s.index gagal ketika tidak ditemukan
        with self.assertRaises(ValueError):
            s.index('decode')


if __name__ == '__main__':
    unittest.main()