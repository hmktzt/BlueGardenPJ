from behave import *
import re

@given("at the signup screen")
def step_impl(context):
    context.browser.get(context.address + "/signup")
    signup_found = re.search("signup", context.browser.page_source, re.IGNORECASE)
    assert signup_found

@when("a new user submits {username} {email} and {password}")
def step_impl(context, username, email, password):
    """
    :type context: behave.runner.Context
    :type username: str
    :type email: str
    :type password: str
    """
    signup(context, username, email, password)

def signup(context, username, email, password):
    username_field = context.browser.find_element_by_name("username")
    password_field = context.browser.find_element_by_name("password")
    email_field = context.browser.find_element_by_name("email")
    username_field.send_keys(username)
    password_field.send_keys(password)
    email_field.send_keys(email)
    username_field.submit()
    context.response = context.browser.page_source

@then('the system should return "{text}" as the signup status of the user')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    assert text in context.response

