from django.test import TestCase
from api.models import Project
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class ModelTestCase(TestCase):
    """
    This test case defines the test suite for project model.
    """

    def setUp(self):
        """
        Defining test client and other test variables
        """
        self.project_name = "New Project 1"
        self.project_description = "Awesome Project"
        self.project = Project(name=self.project_name, description=self.project_description)

    def test_model_can_create_project(self):
        """
        Test the project model can create a project
        """
        old_count = Project.objects.count()
        self.project.save()
        new_count = Project.objects.count()
        self.assertNotEqual(old_count, new_count)


class RegisterViewTestCase(TestCase):
    """
    Test suite for the api views
    """

    def setUp(self):
        """
        Define the test client and other test variables
        """
        self.client = APIClient()
        self.user_data = {"username":"pamela","email":"pamela@example.com","password":"pamela123456"}
        self.response = self.client.post(
            reverse('user_registration'),
            self.user_data,
            format='json'
        )

    def test_api_can_create_a_user(self):
        """
        Test the api has project creation capability
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

class ProjectViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.project_data = {"name": "Awesome project 2", "description": "Great one again"}
        self.response = self.client.post(
            reverse('projects-list'),
            self.project_data,
            format='json'
        )

    def test_api_can_not_unauthorized_create_a_project(self):
        self.assertEqual(self.response.status_code, status.HTTP_401_UNAUTHORIZED)
