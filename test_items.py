from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_present(browser):
    browser.get(link)
    assert EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket")), "Button not found"