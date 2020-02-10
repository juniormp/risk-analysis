from django.test import TestCase
from web.serializer.user_information_serializer import UserInformationSerializer


class TestUserInformationSerializer(TestCase):
    def setUp(self):
        self.user_information_attributes = {
            "age": 30,
            "dependents": 0,
            "income": 100,
            "marital_status": "married",
            "risk_question": [0, 1, 1]
        }

        self.user_information_serializer = UserInformationSerializer(data=self.user_information_attributes)
        self.user_information_serializer.is_valid()

    def test_serializer_should_contains_expected_fields(self):
        expected_fields = {'age', 'dependents', 'risk_question', 'income', 'marital_status'}

        user_information_data = self.user_information_serializer.data

        self.assertEqual(set(user_information_data.keys()), expected_fields)
