
import multiprocessing
import time
from unittest import TestCase

from flask import url_for

from app import create_app, db
from app.config import TestConfig
from app.models import Group, Student, create_test_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    
    def test_group_creation(self):
        page = CreateGroupPage(self.driver).set_group_members("3").set_student1("12345678").set_student2("87654321")

        self.driver.get(localHost)

        self.driver.find_element(By.ID, "student3").send_keys("11223344")

        self.driver.find_element(By.ID, "submitBtn").click()

        # Wait for the page to reload and the new group to be displayed
        WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, "12345678"))
        )

        student1_element = self.driver.find_element(By.ID, "12345678")
        self.assertIsNotNone(student1_element)

        # Assert that the student1 element contains the correct text
        self.assertEqual(student1_element.text, "12345678", f"Expected student1 element to contain '12345678', but got '{student1_element.text}'")


    def test_invalid_group_creation(self):
        self.driver.find_element(By.ID, "groupMembers").send_keys("4")
        self.driver.find_element(By.ID, "student1").send_keys("12345678")
        self.driver.find_element(By.ID, "student2").send_keys("87654321")
        self.driver.find_element(By.ID, "student3").send_keys("11223344")

        self.driver.find_element(By.ID, "submitBtn").click()


class CreateGroupPage:
    def __init__(self, driver):
        self.driver = driver

    def set_student1(self, student_id):
        self.driver.find_element(By.ID, "student1").send_keys(student_id)
        return self

    def set_student2(self, student_id):
        self.driver.find_element(By.ID, "student2").send_keys(student_id)
        return self

    def submit_form(self):
        self.driver.find_element(By.ID, "submitBtn").click()