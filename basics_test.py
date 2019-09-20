import unittest
import statistics
import get_column_stats
import random
import os


# Testing Basic Calculations
class TestCalc(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(get_column_stats.get_mean([1, 2, 3, 4, 5]),
                         statistics.mean([1, 2, 3, 4, 5]))
        self.assertEqual(get_column_stats.get_mean([0, 0, 0, 0, 0]),
                         statistics.mean([0, 0, 0, 0, 0]))
        self.assertEqual(get_column_stats.get_mean([-1, -2, -3, -4, -5]),
                         statistics.mean([-1, -2, -3, -4, -5]))

    def test_std(self):
        self.assertEqual(get_column_stats.get_std([1, 2, 3, 4, 5]),
                         statistics.pstdev([1, 2, 3, 4, 5]))
        self.assertEqual(get_column_stats.get_std([0, 0, 0, 0, 0]),
                         statistics.pstdev([0, 0, 0, 0, 0]))
        self.assertEqual(get_column_stats.get_std([-1, -2, -3, -4, -5]),
                         statistics.pstdev([-1, -2, -3, -4, -5]))


# Testing empty lists
class TestEmptyList(unittest.TestCase):

    def test_empty_mean(self):
        self.assertRaises(ZeroDivisionError,
                          lambda: get_column_stats.get_mean([]))

    def test_empty_stdev(self):
        self.assertRaises(ZeroDivisionError,
                          lambda: get_column_stats.get_std([]))


# Testing null lists
class TestNull(unittest.TestCase):

    def test_null_mean(self):
        self.assertRaises(TypeError,
                          lambda: get_column_stats.get_mean())

    def test_null_stdev(self):
        self.assertRaises(TypeError,
                          lambda: get_column_stats.get_std())


# Testing string in lists
class TestString(unittest.TestCase):

    def test_string_mean(self):
        self.assertRaises(TypeError,
                          lambda: get_column_stats.get_mean('hello'))

    def test_string_stdev(self):
        self.assertRaises(TypeError,
                          lambda: get_column_stats.get_std('hello'))


# Testing random mean case
class TestMeanRandom(unittest.TestCase):

    def test_mean(self):
        A = [random.randint(0, 1000) for i in range(random.randint(0, 100))]
        self.assertEqual(round(get_column_stats.get_mean(A), 5),
                         round(statistics.mean(A), 5))


# Testing random stdev case
class TestStdevRandom(unittest.TestCase):

    def test_stdev(self):
        A = [random.randint(0, 1000)
             for i in range(random.randint(0, 100))]
        self.assertEqual(round(get_column_stats.get_std(A), 5),
                         round(statistics.pstdev(A, statistics.mean(A)), 5))


# Testing random file with loop
class TestRandomFile(unittest.TestCase):

    def setUp(self):
        self.test_file_name = 'setup_test_file.txt'
        f = open(self.test_file_name, 'w')

        for i in range(100):
            rand_int = random.randint(1, 100)
            f.write(str(rand_int) + '\n')
        f.close()

    def tearDown(self):
        os.remove(self.test_file_name)

    def test_mean_file(self):
        V = []
        f = open(self.test_file_name, 'r')
        for l in f:
            A = [int(x) for x in l.split()]
            V.append(A[int(0)])
        self.assertEqual(round(get_column_stats.get_mean(V), 5),
                         round(statistics.mean(V), 5))
        f.close()

    def test_stdev_file(self):
        V = []
        f = open(self.test_file_name, 'r')
        for l in f:
            A = [int(x) for x in l.split()]
            V.append(A[int(0)])
        self.assertEqual(round(get_column_stats.get_std(A), 5),
                         round(statistics.pstdev(A, statistics.mean(A)), 5))
        f.close()

    def test_mean_file_loop(self):
        for i in range(100):
            self.setUp()
            V = []
            f = open(self.test_file_name, 'r')
            for l in f:
                A = [int(x) for x in l.split()]
                V.append(A[int(0)])
            self.assertEqual(round(get_column_stats.get_mean(V), 5),
                             round(statistics.mean(V), 5))
            f.close()

    def test_stdev_file_loop(self):
        for i in range(100):
            self.setUp()
            V = []
            f = open(self.test_file_name, 'r')
            for l in f:
                A = [int(x) for x in l.split()]
                V.append(A[int(0)])
            self.assertEqual(round(get_column_stats.get_std(V), 5),
                             round(statistics.pstdev(V), 5))
            f.close()


# Testing random file with class methods
class TestRandomFileClassMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.class_test_file_name = 'class_setup_test_file.txt'
        f = open(cls.class_test_file_name, 'w')

        for i in range(100):
            rand_int = random.randint(1, 100)
            f.write(str(rand_int) + '\n')
        f.close()

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.class_test_file_name)

    def test_mean_file_loop(self):
        V = []
        f = open(self.class_test_file_name, 'r')
        for l in f:
            A = [int(x) for x in l.split()]
            V.append(A[int(0)])
        self.assertEqual(round(get_column_stats.get_mean(V), 5),
                         round(statistics.mean(V), 5))
        f.close()

    def test_stdev_file_loop(self):
        V = []
        f = open(self.class_test_file_name, 'r')
        for l in f:
            A = [int(x) for x in l.split()]
            V.append(A[int(0)])
        self.assertEqual(round(get_column_stats.get_std(A), 5),
                         round(statistics.pstdev(A,
                                                 statistics.mean(A)), 5))
        f.close()


if __name__ == '__main__':
    unittest.main()
