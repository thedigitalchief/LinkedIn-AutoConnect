import time, random, os, csv, platform
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import pyautogui
from urllib.request import urlopen
from webdriver_manager.chrome import ChromeDriverManager
import re
import yaml
from datetime import datetime, timedelta

# setting parameters so Chrome and webpage detect botting

#System.setProperty("webdriver.chrome.driver","/Users/dylannguyen/Documents/Coding - Local/Projects/Automated LinkedIn Networking Bot/automated-linkedin-networking-bot")
#options = webdriver.ChromeOptions()
#options.add_argument("--no-sandbox")
#options.add_argument("--headless")
#options.add_argument("--window-size=1920,1080")
#options.add_argument("--disable-extensions")


#log in to the LinkedIn account
def login():

    driver.get(login_url)
    sleep(2)

    # Setting up login details
    email_element = driver.find_element_by_id('username')
    password_element = driver.find_element_by_id('password')
    # Sending Input in the field
    email_element.send_keys(email)
    password_element.send_keys(password)

    # Submitting the login request
    driver.find_element_by_xpath(
        '//*[contains(concat( " ", @class, " " ), concat( " ", "mercado-button--primary", " " ))]').click()


def check_password():
    try:
        error = driver.find_element_by_id("error-for-password")
        if "Hmm, that's not the right password" in error.text:
            print("Wrong Password")
            return 0
        elif "Password must be 6 characters or more" in error.text:
            print("Short Password")
            return 0

    except NoSuchElementException:
        return 1
    else:
        return 0


def check_email():
  return 1

def check_credentials():
  return 0


def open_networks():
  driver.get(network_url)
  driver.maximize_window()


def send_requests():

    flag = 1
    count_skipped = 0
    requests = 0

    while flag:
        #Getting all button elements
        button_elements = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "artdeco-button__text", " " ))]')

        for i in button_elements:
            if i.text == 'Connect':
                try:
                    i.click()
                    print("Connection Request send")
                    requests += 1
                except:
                    print("Skipped", count_skipped)
                    try:
                        driver.find_element_by_class_name("artdeco-button ip-fuse-limit-alert__primary-action artdeco-button--2 artdeco-button--primary ember-view").click()
                    except NoSuchElementException:
                        pass
                    count_skipped += 1
                    if count_skipped == 4:
                        flag = 0
                sleep(1)
            if requests >= no_of_requests:
                break
        if requests >= no_of_requests:
            break

        # scrolls down webpage and refresh the button list
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(2.5)



def visibilty(company_name):

    driver.get("https://www.linkedin.com/company/" + company_name + "/people/")
    list = []
    sleep(2)

    number = driver.find_element_by_xpath("//*[@class='t-20 t-black']")
    c = number.text

    print("Total", c)
    number = int(input("Enter Number Of profiles you want to visit:"))

    while True:
        number -= 10
        try:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(2.5)
        except WebDriverException:
            break
        if number < 0:
            break

    links_list = driver.find_elements_by_xpath("//*[@class='ember-view link-without-visited-state']")

    for i in links_list:
        list.append(i.get_attribute('href'))

    for i in list[0:number]:
        print(i)
        sleep(2)
        try:
            driver.get(i)
            print("visited", i)
        except WebDriverException:
            break


if __name__ == '__main__':

  login_url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
  network_url = "https://www.linkedin.com/mynetwork/"

  # asking for user input to set credentials and automate login process
  email = input("Enter your email: ")
  password = input("Enter your password: ")

  # runs the driver, this one is chrome
  driver = webdriver.Chrome()

  # calls my login function
  login()

  # wrong email check condition is now remaining...

  # Check for correct password
  if check_credentials():
      sleep(5)




    
