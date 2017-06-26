import unittest
from integration.configuration import Configuration

class TestConfigurationReadWrite(unittest.TestCase):
    def __init__(self):
        pass

    def test_set_property(self):
        Configuration().save_property('test_key', 'test_value', 'TEST_SECTION')
