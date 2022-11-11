Some of these procedures are very nuanced. If another developer came along and had to maintain our API using your unit tests, they might not understand all of the intricate workings of your tests. Create a README.md in your repository containing detailed instructions of how to get the cookie, how to run the code, and which file to change if you have new functionality you need to test. (The api.py file should be sufficient unless you add a new endpoint. In that case, the test_api.py should be the one changing.)

# READ ME
### Get the cookie

1. Open the URL corresponding to your server
2. Access the login endpoint by adding `/api/v1/auth/google` to the end of the URL (For example, fr server 1 it would be https://s1.byu-itc-210.net:1337/api/v1/auth/google )
3. Open the Inspect Element tool
4. Application > Cookies > [server address] > click on the cookie
5. Check the `Show URL decoded` box
6. Copy the Cookie Value that now appears below

### Run the code

1. Once there are no errors in the program, ensure that you are on the test_api.py file
2. In the top right corner of VS Code, click the small dropdown next to the run button
3. Select `Debug Python File`
4. This will run the program and will point to errors. It is now set as the default debugger,
so from now on just click the run button (which should now have a small bug icon with it)

### Adding a new test

1. Open api.py
2. Define a new function
3. Ensure that it returns a value
3. Open test_api.py 
4. Define new test 
