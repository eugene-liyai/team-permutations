from unittest import TestCase

from controller.generate_team_array import generateXArray


class GenerateTeamTest(TestCase):

    def test_generate_team_array(self):
    """ Test key value pair check """
    self.assertFalse(UserAdapter.has_key_value(dir(self.user_payload), 'name'))
