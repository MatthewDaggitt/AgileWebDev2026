
import multiprocessing
from unittest import TestCase

from flask import url_for

from app import create_app, db
from app.config import TestConfig
from app.models import Group, Student, create_test_data
from selenium import webdriver

localHost = "http://127.0.0.1:5000/"

class SeleniumTests(TestCase):
    def setUp(self):
        self.testApp =  create_app(TestConfig)
        self.app_context = self.testApp.app_context()
        self.app_context.push()
        db.create_all()
        create_test_data()

        self.server_thread = multiprocessing.Process(target=self.testApp.run)
        self.server_thread.start()

        self.driver = webdriver.Chrome()
        return super().setUp()
    
    def tearDown(self):
        self.server_thread.terminate()
        self.driver.close()

        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        return super().tearDown()
    
    def test_password_hashing(self):
        self.driver.get(localHost)