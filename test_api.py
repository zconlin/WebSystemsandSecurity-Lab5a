#!/usr/bin/env python3
import random
import string
import unittest

"""TODO: Import the `API` class from the api.py file"""

def generate_random_text(l=10):
    """ Helper to generate random text for creating new tasks.
    This is helpful and will ensure that when you run your tests,
    a new text string is created. It is also good for determining
    that two tasks are unique.
    Keyword arguments:
        l (int): How long the generated text should be (default 10)
    Returns:
        A randomly-generated string of length `l`
    """
    chars = string.hexdigits
    return "".join(random.choice(chars) for i in range(l)).lower()

def generate_random_date(year=None, month=None, date=None):
    """ Helper to generate random date for creating new tasks.
    This is helpful as another way of generating random tasks
    Keyword arguments:
        year: Specify a year (default None)
        month: Specify a month (default None)
        date: Specify a date (default None)
    Returns:
        A randomly-generated string representation of a date
    """
    if not year:
        year = str(random.randint(2000, 2025))
    if not month:
        month = str(random.randint(1, 12))
    if not date:
        date = str(random.randint(1, 28))
    return str(year) + "-" + str(month).zfill(2) + "-" + str(date).zfill(2) + "T00:00:00.000Z"

class TestAPI(unittest.TestCase):

    # TODO: update the cookie value and uncomment the desired `base_url, cookie` pair when ready to test
    # base_url, cookie = "https://s1.byu-itc-210.net:1337", "s%3A3t..." # For s1
    # base_url, cookie = "https://s2.byu-itc-210.net:1338", "s%3Adq..." # For s2
    # base_url, cookie = "https://s3.byu-itc-210.net:1339", "s%3A-t..." # For s3
    # base_url, cookie = "https://s4.byu-itc-210.net:1340", "s%3AJi..." # For s4

    # This will be ran once, when you start your tests.
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.api = API(self.base_url)

    def test_create_task(self):
        """ Tests creating a task is successful.
        This is an example test:
            - Create the task w/dummy data
            - Verify that the task was created
            - Delete the task we created
        You will be required to implement the other tests
        that are defined in BaseTestCase. They will be marked
        with @abc.abstractmethod.
        """
        Text = generate_random_text()
        Date = generate_random_date()

        resp = self.api.create_task(self.cookie, Text, Date)
        self.assertTrue(resp.ok, msg=f"The Create Task failed: {resp.reason}.")
        task = resp.json()

        self.assertEqual(task["Text"], Text, msg="The task's Text did not match the expected Text.")
        self.assertEqual(task["Date"], Date, msg="The task's Date did not match the expected Date.")
        self.assertFalse(task["Done"], msg="The task's Done returned True, expected False.")
        self.assertIn("UserId", task, msg="All tasks should have a UserId, matching the Id of the user who created it.")

        # cleanup - we don't want to conflict with other tests
        # or have a test task in our database.
        self.api.delete_task(self.cookie, task["_id"])

    def test_read_one_task(self):
        pass

    def test_update_task(self):
        pass

    # Make more methods that begin with 'test` to test all endpoints
    # properly work and fail when you expect them to.

# Inside this `if` statement will only run if we call the program as
# the top-level module, i.e. when we run this file, not when we import
# this file
if __name__ == "__main__":
    unittest.main()
