Installation and Running App
============================

Please follow the steps below to install and run your application:

Download the repository
-----------------------

First, you need to download the repository from GitHub. You can do this by cloning the repository using git, or by manually downloading it from GitHub.

If you want to use git, make sure you have it installed on your system. If not, you can download it from [here](https://git-scm.com/). Once git is installed, open your terminal or command prompt and navigate to the directory where you want to download the repository. Run the following command:

    git clone https://github.com/eric-official/teko/

If you want to manually download the repository, go to the repository page, click on the "Code" button, and then "Download ZIP". Unzip the downloaded file in the directory where you want to have the project.

Install Python and Required Packages
------------------------------------

You need to have Python installed on your system to run this application. If you don't have it installed, you can download it from [here](https://www.python.org/downloads/). Download the version appropriate for your system. The installation process is straightforward, just follow the prompts that suit your operating system. If you are using Unix, you can follow this bash prompt:

    sudo apt install python3

Once Python is installed and the virtual environment is activated, you can install the required packages using the `requirements.txt` file provided in the repository. From your terminal, navigate to the project directory (if you are not already there) and run the following command:

    pip3 install -r requirements.txt

Set Up API Keys
---------------

In order to run the application, you need to provide your Google Maps and OpenAI API keys. These keys should be saved in a `.env` file located in the project directory. You can create this file manually using a text editor, or by running the following command in your terminal:

    echo "GOOGLE_MAPS_API_KEY=<your-google-maps-api-key>" > .env
    echo "OPENAI_API_KEY=<your-openai-api-key>" >> .env

**Note:** please replace <your-google-maps-api-key> and <your-openai-api-key> with your actual keys.

### OpenAI API Key

1.  Go to the [OpenAI website](https://openai.com/).
2.  Click on "Sign In" in the top right corner if you have an account, or "Sign Up" if you don't.
3.  Once you've logged in, you'll be taken to the dashboard.
4.  Click on the API keys section on the left side of the dashboard.
5.  Click on the "Create new key" button.
6.  Give your key a name and optionally set a description.
7.  Click on "Create key".
8.  You will now be shown your key. Make sure to save this key somewhere secure as you won't be able to see it again.

### Google Maps API Key

1.  Go to the [Google Cloud Console website](https://console.cloud.google.com/).
2.  If you haven't created a project yet, create one by clicking on the project drop-down and selecting "New Project".
3.  Navigate to the "APIs & Services" > "Library".
4.  Search for "Maps JavaScript API" and select it.
5.  Click "Enable" to enable the API for your project.
6.  Navigate to the "APIs & Services" > "Credentials" page.
7.  Click "Create credentials" and select "API key".
8.  Your new API key will be displayed. Click "Close".

Remember, do not share these keys with anyone as they can be used to access services on your behalf. Once you have these keys, refer back to step 5 of the previous instructions to add these keys to your `.env` file.

Run the Application
-------------------

Finally, you can run the application using Streamlit. From your terminal, navigate to the project directory (if you are not already there) and run the following command:

    cd teko-main
    streamlit run home.py

If everything is set up correctly, the application should start and you should be able to access it from your web browser. The terminal will display the address where the application is running, usually this is [http://localhost:8080](http://localhost:8080).
