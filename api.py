"""TO DO: Add a Shebang"""

"""TO DO: Import urljoin from urllib.parse"""

"""TO DO: Import the requests"""

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
        pass

    def read_task(self, cookie, task_id):
        pass

    def update_task(self, cookie, task_id, Done):
        pass
        # Note: Cast your `Done` parameter to a
        # string, and use the `.lower()` method
        # on it, before you stick it in the
        # `data` object.

    def delete_task(self, cookie, task_id):
        pass

    def read_current_user(self, cookie):
        pass

if __name__ == "__main__":
    # Remember, this section of code is for you. Do with
    # it what you will, to see what the code looks like
    # for different requests. You may add more api calls
    # or remove them. I have found that if I add too
    # many `print()`s, the output becomes overloaded and
    # unhelpful, but again, this is personal preference.
    base_url = "https://210s1.itcyber.byu.edu"
    cookie = "s%3Avz...0dOSwwD5amLfV_wJuwVmxYmu1Kq.Wn2y9mhJAI7zlxQd%2FvSOTBB9lWfgpElvtEzhKIs6cq0"
    api = API(base_url)
    response = api.create_task(cookie, "Test the API", "2020-02-20")
    print(response.ok)
    print(response.status_code)
    print(response.text)
    print(response.json())


