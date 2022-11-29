"""TO DO: Add a Shebang"""
#!/usr/bin/env python3

"""TO DO: Import urljoin from urllib.parse"""
from urllib.parse import urljoin

"""TO DO: Import the requests"""
import requests

class API(object):

    def __init__(self, base_url):
        """ Creates the API client.
        Parameters:
            base_url (str): The base URL for the API.
        Returns:
            New API class for testing an API.
        """
        self.base_url = base_url

    def create_task(self, cookie, Text, Date):
        """ Create a new task
        Parameters:
            cookie (str): Pre-authorized cookie
            Text (str): Text/description of the task.
            Date (str): Due date of the task
        Returns:
            Response from the server
        """
        url = urljoin(self.base_url, "api/v1/tasks")
        data = '{ "Text": "%s", "Date": "%s" }' % (Text, Date)
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'it210_session=' + cookie
        }
        response = requests.request("POST", url, headers=headers, data=data)
        return response

    def read_all_tasks(self, cookie):
        """ Read all tasks
        Parameters:
            cookie (str): Pre-authorized cookie
        Returns:
            Response from the server
        """
        url = urljoin(self.base_url, "api/v1/tasks")
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'it210_session=' + cookie
        }
        response = requests.request("GET", url, headers=headers)
        return response

    def read_task(self, cookie, task_id):
        """ Read specific task
        Parameters:
            cookie (str): Pre-authorized cookie
            task_id: Identifying number assigned to task in the database
        Returns:
            Response from the server
        """
        url = urljoin(self.base_url, "api/v1/tasks/" + task_id)
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'it210_session=' + cookie
        }
        response = requests.request("GET", url, headers=headers)
        return response

    def update_task(self, cookie, task_id, Done): 
        """ Update a task with completion status
        Parameters:
            cookie (str): Pre-authorized cookie
            task_id: Identifying number assigned to task in the database
            Done (str): Mark task as done
        Returns:
            Response from the server
        """
        url = urljoin(self.base_url, "api/v1/tasks/" + task_id)
        data = '{ "Done": "%s" }' % (str(Done).lower())
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'it210_session=' + cookie
        }
        response = requests.request("PUT", url, headers=headers, data=data)
        return response

    def delete_task(self, cookie, task_id):
        """ Delete a task
        Parameters:
            cookie (str): Pre-authorized cookie
            task_id: Identifying number assigned to task in the database
        Returns:
            Response from the server
        """
        url = urljoin(self.base_url, "api/v1/tasks/" + task_id)
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'it210_session=' + cookie
        }
        response = requests.request("DELETE", url, headers=headers)
        return response

    def read_current_user(self, cookie):
        url = urljoin(self.base_url, "api/v1/user")
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'it210_session=' + cookie
        }
        response = requests.request("GET", url, headers=headers)
        return response

if __name__ == "__main__":
    # Remember, this section of code is for you. Do with
    # it what you will, to see what the code looks like
    # for different requests. You may add more api calls
    # or remove them. I have found that if I add too
    # many `print()`s, the output becomes overloaded and
    # unhelpful, but again, this is personal preference.
    base_url = "https://s1.byu-itc-210.net:1337"
    cookie = "s:f9j--gAqO30dmhX0awfGiNaFuq_xmLJT.i8VUGln61vuBZvVSDwFm3qvk/pQ598PWiyTHvbAtVPA"
    id = "63692e586bcd2d42d3529515"
    api = API(base_url)
    #response = api.create_task(cookie, "Test the API", "2020-02-20") #works!
    #response = api.read_all_tasks(cookie) #works!
    #response = api.read_task(cookie, id) #works! 
    response = api.update_task(cookie, id, True) #works!
    #response = api.delete_task(cookie, id) #works!
    #response = api.read_current_user(cookie) #works!

    print(response.ok)
    print(response.status_code)
    print(response.text)
    print(response.json())


