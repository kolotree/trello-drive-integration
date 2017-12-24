import unittest
from integration.configuration.configuration import Configuration

class TestConfigurationReadWrite(unittest.TestCase):

    def test_set_property(self):
        Configuration().save_property('test_key', 'test_value', 'TEST_SECTION')

    def test_read_all_members_from_auto_assign_section(self):
        Configuration().save_property('test_member_1', 'test_company_1, test_company_2, test_company_3', 'AUTO_ASSIGN_MEMBER_TO_CARD')
        Configuration().save_property('test_member_2', 'test_value_1', 'AUTO_ASSIGN_MEMBER_TO_CARD')
        dictionary_of_members = Configuration().get_dict_in_section()
        self.assertIn('test_member_1', dictionary_of_members.keys())
        self.assertIn('test_member_2', dictionary_of_members.keys())

    def test_getting_user_assigned_to_company(self):
        Configuration().save_property('test_member_1', 'test_company_1, test_company_2, test_company_3',
                                      'AUTO_ASSIGN_MEMBER_TO_CARD')
        Configuration().save_property('test_member_2', 'test_value_1', 'AUTO_ASSIGN_MEMBER_TO_CARD')

        member = Configuration().get_assigned_user_for_company('test_company_2')
        self.assertEqual('test_member_1', member)

    def test_getting_user_assigned_to_company_with_extended_company_name(self):
        Configuration().save_property('test_member_1', 'test_company_1, test_company_2, test_company_3',
                                      'AUTO_ASSIGN_MEMBER_TO_CARD')
        Configuration().save_property('test_member_2', 'test_value_1', 'AUTO_ASSIGN_MEMBER_TO_CARD')

        member = Configuration().get_assigned_user_for_company('test_company_2 (UF: 1, IF: 3)')
        self.assertEqual('test_member_1', member)

    def test_getting_user_assigned_to_company_with_company_name_containing_spaces(self):
        Configuration().save_property('test_member_1', 'test_company_1, test_company_2, company with spaces, test_company_3',
                                      'AUTO_ASSIGN_MEMBER_TO_CARD')
        Configuration().save_property('test_member_2', 'test_value_1', 'AUTO_ASSIGN_MEMBER_TO_CARD')

        member = Configuration().get_assigned_user_for_company('company with spaces')
        self.assertEqual('test_member_1', member)

    def test_searching_user_for_invalid_company(self):
        Configuration().save_property('test_member_1', 'test_company_1, test_company_2, test_company_3',
                                      'AUTO_ASSIGN_MEMBER_TO_CARD')
        Configuration().save_property('test_member_2', 'test_value_1', 'AUTO_ASSIGN_MEMBER_TO_CARD')

        member = Configuration().get_assigned_user_for_company('unexisting_company')
        self.assertEqual(None, member)

if __name__ == '__main__':
    unittest.main()