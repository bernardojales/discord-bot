import unittest
from unittest.mock import Mock
from newClassLEVELDB import on_message

class TestLevelingSystem(unittest.TestCase):

    def setUp(self):
        self.bot = Mock()
        self.message = Mock()
        self.message.content = "!award @mentioned_user"
        self.message.author.guild_permissions.administrator = True
        self.message.mentions = [Mock(id=123456789)]  # Replace with a valid user ID

    def test_award_star(self):
        user_levels = Mock()
        user_levels.find_one.return_value = {"_id": 123456789, "stars": 0, "level": 1}
        self.bot.mongo_client.__getitem__.return_value = user_levels

        on_message(self.message)

        user_levels.find_one.assert_called_with({"_id": 123456789})
        user_levels.update_one.assert_called_with({"_id": 123456789}, {"$inc": {"stars": 1}})
        self.message.channel.send.assert_called_with("@mentioned_user has received a star! They are now at level 1 with 1 stars.")

if __name__ == '__main__':
    unittest.main()