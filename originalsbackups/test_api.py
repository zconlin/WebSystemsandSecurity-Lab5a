#!/usr/bin/env python3
import random
import string
import unittest
from api import API

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

def generate_random_text(l=10):
    """ Helper to generate random text for an incorrect id.
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
    base_url, cookie = "https://s1.byu-itc-210.net:1337", "s:f9j--gAqO30dmhX0awfGiNaFuq_xmLJT.i8VUGln61vuBZvVSDwFm3qvk/pQ598PWiyTHvbAtVPA" # For s1
    # base_url, cookie = "https://s2.byu-itc-210.net:1338", "s:1XLt8CqzxEe0Tm3Y_7sNp3uHrJlLrilo.m6QwumcpXM7OkoRRVNtWywZCvmwFn1vOSXapWzyvN+A" # For s2
    # base_url, cookie = "https://s3.byu-itc-210.net:1339", "s:2SR-cptPEX-7nI7W-QMpLyUbKMGEw8di.sIOFQFskTtNDguA08Y3gtLz34eO/6xNGYTtzgcJaLsk" # For s3
    # base_url, cookie = "https://s4.byu-itc-210.net:1340", "s:SAfGzDCYOLaSpCeH6s1mOOJaWtNK3kx_.o+YkhhZF7SR5YXVbV4Tj5QkUtGxc+up2IilJJckTDD8" # For s4

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
        Text = generate_random_text()
        Date = generate_random_date()

        createresp = self.api.create_task(self.cookie, Text, Date)
        id = createresp.json()["_id"]

        resp = self.api.read_task(self.cookie, id)
        self.assertTrue(resp.ok, msg=f"Read One Task failed: {resp.reason}.")
        task = resp.json()

        self.assertEqual(task["Text"], Text, msg="The task's Text did not match the expected Text.")
        self.assertEqual(task["Date"], Date, msg="The task's Date did not match the expected Date.")
        self.assertFalse(task["Done"], msg="The task's Done returned True, expected False.")
        self.assertIn("UserId", task, msg="All tasks should have a UserId, matching the Id of the user who created it.")

        self.api.delete_task(self.cookie, task["_id"])

    def test_read_all_tasks(self):
        Text = generate_random_text()
        Date = generate_random_date()

        createresp = self.api.create_task(self.cookie, Text, Date)
        self.assertTrue(createresp.ok, msg=f"Create Task failed: {createresp.reason}.")
        id = createresp.json()

        resp = self.api.read_all_tasks(self.cookie)
        self.assertTrue(resp.ok, msg=f"Read All Tasks failed: {resp.reason}.")
        task = resp.json()

        for x in task:
            self.assertIn("UserId", x, msg="All tasks should have a UserId, matching the Id of the user who created it.")
            if x["UserId"] == id["UserId"]:
                isTrue = True
            else:
                isTrue = False
                break
        self.assertTrue(isTrue, msg=f"UserId does not match user: {resp.reason}.")

        self.api.delete_task(self.cookie, id["_id"])
        

    def test_update_task(self):
        Text = generate_random_text()
        Date = generate_random_date()

        createresp = self.api.create_task(self.cookie, Text, Date)
        id = createresp.json()["_id"]
        done = createresp.json()["Done"]

        resp = self.api.update_task(self.cookie, id, done)
        self.assertTrue(resp.ok, msg=f"Read One Task failed: {resp.reason}.")
        task = resp.json()

        self.assertFalse(task["Done"], msg="The task's Done returned True, expected False.")

        self.api.delete_task(self.cookie, task["_id"])

    def test_delete_task(self):
        Text = generate_random_text()
        Date = generate_random_date()

        createresp = self.api.create_task(self.cookie, Text, Date)
        id = createresp.json()["_id"]

        deleteresp = self.api.delete_task(self.cookie, id)
        self.assertTrue(deleteresp.ok, msg="The task was not deleted.")

        readresp = self.api.read_task(self.cookie, id)
        self.assertFalse(readresp.ok, msg="Reading the task succeeded.")
        
    def test_user(self):
        resp = self.api.read_current_user(self.cookie)
        self.assertTrue(resp.ok, msg=f"Read Current User failed: {resp.reason}.")
        task = resp.json()

        self.assertIn("Id", task, msg="The user's ID did not match the expected Text.")
        self.assertIn("UserName", task, msg="The user's Username did not match the expected Text.")
        self.assertIn("Email", task, msg="The user's Email did not match the expected Text.")


############################   Failing Tests   ############################

    def test_read_one_task_fail(self):
        fakeid = generate_random_text(24)

        resp = self.api.read_task(self.cookie, fakeid)
        self.assertFalse(resp.ok, msg=f"Read One Task (Fail) failed successfully: {resp.reason}.")

    def test_update_task_fail(self):
        fakeid = generate_random_text(24)

        resp = self.api.update_task(self.cookie, fakeid, True)
        self.assertFalse(resp.ok, msg=f"Update Task (Fail) failed successfully: {resp.reason}.")

    def test_delete_task_fail(self):
        fakeid = generate_random_text(24)
        deleteresp = self.api.delete_task(self.cookie, fakeid)
        self.assertFalse(deleteresp.ok, msg="The task was not deleted.")

    def test_delete_task_invalidID(self):
        fakeid = generate_random_text(23)

        deleteresp = self.api.delete_task(self.cookie, fakeid)
        self.assertFalse(deleteresp.ok, msg="The task was not deleted.")

    def test_read_all_tasks_no_cookies(self):
        fakeCookie = "This is an oatmeal raisin cookie."
        resp = self.api.read_all_tasks(fakeCookie)
        
        self.assertFalse(resp.ok, msg=f"Read All Tasks failed: {resp.reason}.")        
    
    def test_create_task_not_enough_data(self):
        Text = ""
        Date = ""

        resp = self.api.create_task(self.cookie, Text, Date)
        self.assertFalse(resp.ok, msg=f"The Create Task failed: {resp.reason}.")   
        

# Inside this `if` statement will only run if we call the program as
# the top-level module, i.e. when we run this file, not when we import
# this file
if __name__ == "__main__":
    unittest.main()