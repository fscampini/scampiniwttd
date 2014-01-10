# coding: utf-8
from unittest import skip
from django.contrib.auth import get_user_model
from django.test import TestCase
from eventex.myauth.backends import EmailBackend
from django.test.utils import override_settings

@skip
class EmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='felipe',
                                      email='fscampini@gmail.com',
                                      password='admin')
        self.backend = EmailBackend()
        
    def test_authenticate_with_email(self):
        user = self.backend.authenticate(email='fscampini@gmail.com',
                                         password='admin')
        self.assertIsNotNone(user)
    
    def test_wrong_password(self):
        user = self.backend.authenticate(email='fscampini@gmail.com',
                                         password='wrong')
        self.assertIsNone(user)
    
    def test_unknown_user(self):
        user = self.backend.authenticate(email='unknown@gmail.com',
                                         password='admin')
        self.assertIsNone(user)
        
    def test_get_user(self):
        self.assertIsNotNone(self.backend.get_user(1))

@skip        
class MultipleEmailTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='user1',
                                      email='fscampini@gmail.com',
                                      password='admin')
        UserModel.objects.create_user(username='user2',
                                      email='fscampini@gmail.com',
                                      password='admin')
        self.backend = EmailBackend()
        
        
    def test_multiple_emails(self):    
        user = self.backend.authenticate(email='fscampini@gmail.com',
                                  password='admin')
        self.assertIsNone(user)
        
@skip
@override_settings(AUTHENTICATION_BACKENDS=('eventex.myauth.backends.EmailBackend',))
class FunctionalEmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='felipe',
                                      email='fscampini@gmail.com',
                                      password='admin')
    
    def test_login_with_email(self):
        result = self.client.login(email='fscampini@gmail.com',
                                      password='admin')
        
        self.assertTrue(result)
        
    def test_login_with_username(self):
        result = self.client.login(username='fscampini@gmail.com',
                                      password='admin')
        
        self.assertTrue(result)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    