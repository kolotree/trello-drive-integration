import unittest
from integration.configuration import Configuration

class TestConfigurationReadWrite(unittest.TestCase):

    def test_set_property(self):
        Configuration().save_property('test_key', 'test_value', 'TEST_SECTION')


if __name__ == '__main__':
    unittest.main()