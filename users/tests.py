from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.test import APITestCase


class TestUsers(APITestCase):

    @classmethod
    def setUpTestData(self):
        # creating a new user without using an API
        Profile.objects.create(
            username="virat", email='virat@gmail.com', password="viratkohli")

    def test_username(self):
        # testing the username of the created user
        user = Profile.objects.get(email='virat@gmail.com')
        self.assertEqual(user.username, 'virat')

    def test_number_of_users(self):
        # get api should return total number of users
        response = self.client.get('/api/users/allUsers/')
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data), 1)

    def test_create_new_user(self):
        # adding a new user through post api
        response = self.client.post(
            '/api/users/addUser/', {'username': 'suresh', 'email': 'suresh@gmail.com', 'password': 'sureshraina'})
        self.assertEqual(response.status_code, 200)

        # get api should return 2 users
        response = self.client.get('/api/users/allUsers/')
        response_data = response.json()
        self.assertEqual(len(response_data), 2)

        # post API for getting the token for authentication
        response = self.client.post(
            '/token/', {'username': 'suresh', 'password': 'sureshraina'})
        response_data = response.json()

        token = response_data['access']
        headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}

        response = self.client.get(
            '/api/users/currentUser/', **headers)
        response_data = response.json()
        print(response_data)
