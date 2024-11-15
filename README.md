<p> Python version 3 must be installed on the local machine </p>
<p> Clone the project from the git repository </p>

<p>Create a test key on the website https://thecatapi.com/#pricing.</p>
<p>Create .env file or rename the file env.example to .env and assign the value of the created api key 
to the variable <b>API_KEY</b></p>

<p>In the console, open the repository with the project and create a virtual environment<br>
for a Windows 
<code>
    python -m venv venv
</code><br>
for a  MacOS/Linux
<code>
    python3 -m venv venv
</code>
</p>

<p>Activate the virtual environment<br>
for a Windows 
<code>
    .\venv\Scripts\activate
</code><br>
for a  MacOS/Linux
<code>
    source venv/bin/activate
</code>
</p>
<p>Install dependencies from requirements.txt<br>
for a Windows 
<code>
    pip install -r requirements.txt
</code><br>
for a  MacOS/Linux
<code>
    pip install -r requirements.txt
</code>
</p>
<p>Run tests <code> python -m pytest </code>

<b>All commands are executed in the terminal.</b>

<p>What test scenarios are covered by the tests:</p>

 * retrieving data with a valid API key - test_api_key_valid
 * checking the response for the presence of an image - test_image_retrieval
 * attempting to retrieve data with an invalid API key - invalid_api_key
 * attempting to retrieve data with an empty API key - no_api_key
 * checking that the search by breed works - test_check_filter_by_breed

