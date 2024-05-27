import unittest
from models import storage
from models.user import User
from models.state import State


class TestStorageMethods(unittest.TestCase):
    """Test the get and count methods"""

    def setUp(self):
        """Set up for the tests"""
        self.user = User(email="test@test.com", password="password")
        self.user.save()
        self.state = State(name="California")
        self.state.save()

    def tearDown(self):
        """Tear down after the tests"""
        storage.delete(self.user)
        storage.delete(self.state)
        storage.save()

    def test_get(self):
        """Test the get method"""
        user_id = self.user.id
        state_id = self.state.id
        self.assertEqual(storage.get(User, user_id), self.user)
        self.assertEqual(storage.get(State, state_id), self.state)
        self.assertIsNone(storage.get(User, "non-existent-id"))

    def test_count(self):
        """Test the count method"""
        initial_count = storage.count()
        self.assertEqual(storage.count(User), 1)
        self.assertEqual(storage.count(State), 1)
        self.assertEqual(storage.count(), initial_count)
        

if __name__ == "__main__":
    unittest.main()
