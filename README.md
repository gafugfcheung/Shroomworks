<h2>Shroomworks</h2>

The repository contains two directories: 
    
    MyApplication/
Is the Android application project. It can be opened in Android Studio and compiled without errors, provided the necessary SDK tools are installed - follow the Android Studio prompts.

    website-root-shroomworks/
Is the website frontent and backend code.

Our live test version has a lot of work in progress, so it may not be available all the time. Please try to access it at "www.lensapp.co.uk" or...

Feel free to test our code!

Follow the steps below:
*Note: we are using Python 2.7 and Django 1.10.4

1) Start by downloading the folder /website-root-shroomworks from our repository

2) Make sure you have Django installed - if you don't, run "pip install django" in Linux or OSX

3a) If you're on Windows, you can try to use the Unix shell. This needs to by enabled on "Programs and Features"

3b) You may have to install python too (good luck, might be easier to install Linux)

4) Once django is installed, you will also need to install the following packages. They can all be installed using pip:
    
    django-extensions
    
    djangorestframework
    
    pillow

5) Now you're ready to rock! Using the terminal, navigate to the folder 
    
    ~/website-root-shroomworks you downloaded before where the file "manage.py" is located

6) Run the command "python manage.py runserver" - you should see a success message

7) Go to your browser and access http://localhost:8000/ and you should be able to check the website!

8) Use this to login: 
    
    username: "test" 
    
    password: "123456"
    
If you have any question, please let me know at vrgimael@gmail.com
