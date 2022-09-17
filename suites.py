import unittest
import HtmlTestRunner
from activation import TestActivationStep1


class TestSuite(unittest.TestCase):

    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            #unittest.defaultTestLoader.loadTestsFromTestCase(TestLoginWithCredentials_Firefox),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestActivationStep1),
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Test',
            report_name='Test Results'
        )

        runner.run(smoke_test)