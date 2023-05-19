from django.test import TestCase
from .models import Profile, Friend, ChatMessage
from django.contrib.auth.models import User


class ModelsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.create(user=self.user, name='Test Profile')
        self.friend = Friend.objects.create(profile=self.profile)
        self.chat_message = ChatMessage.objects.create(body='Test message', msg_sender=self.profile, msg_receiver=self.profile, seen=False)

    def test_profile_creation(self):
        # Verify that the profile is correctly linked to the user
        self.assertEqual(self.profile.user, self.user)

    def test_friend_creation(self):
        # Verify that the friend is correctly linked to the profile
        self.assertEqual(self.friend.profile, self.profile)

    def test_chat_message_creation(self):
        # Verify that the chat message is correctly linked to the sender and receiver profiles
        self.assertEqual(self.chat_message.msg_sender, self.profile)
        self.assertEqual(self.chat_message.msg_receiver, self.profile)

    def test_chat_message_string_representation(self):
        # Verify that the string representation of the chat message matches the expected format
        expected_string = 'Test message'
        self.assertEqual(str(self.chat_message), expected_string)

    def test_unseen_chat_messages(self):
        # Verify that the "seen" field of chat messages is initially set to False
        self.assertFalse(self.chat_message.seen)
        
        # Update the "seen" field
        self.chat_message.seen = True
        self.chat_message.save()

        # Verify that the "seen" field is updated correctly
        updated_chat_message = ChatMessage.objects.get(id=self.chat_message.id)
        self.assertTrue(updated_chat_message.seen)
