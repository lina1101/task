import time

from django.test import TestCase, SimpleTestCase

from api.tasks import time_func


class UtilTestCase(SimpleTestCase):
    def test_time_func(self):
        """
        Here we just sanity check the output execution time from time_func.
        """
        def test_func(x):
            return x

        start_time = time.time()
        exec_time, _ = time_func(test_func, 1)
        result_time = (time.time() - start_time) * 1000

        self.assertGreater(result_time, 0)
        self.assertLessEqual(exec_time, result_time)
