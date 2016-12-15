<h2>Shroomworks</h2>

To test the Lens app, download 

    Lens.apk 
Onto your Android smartphone and install it using a file manager, making sure that you allow the installation of apps from sources outside of Google Play.

<hr>

The repository contains two directories: 
    
    MyApplication/
Is the Android application project. It can be opened in Android Studio and compiled without errors, provided the necessary SDK tools are installed - follow the Android Studio prompts.

    website-root-shroomworks/
Is the website frontent and backend code.

Our live test version has a lot of work in progress, so it may not be available all the time. Please try to access it at "www.lensapp.co.uk" or feel free to test our code!

Follow the steps below:

*Note: we are using Python 2.7 and Django 1.10.4

Start by downloading the folder /website-root-shroomworks from our repository. Make sure you have Django installed - if you don't, run:
   
    pip install django
    
in Linux or OSX.

If you're on Windows, you can try to use the Unix shell. This needs to by enabled on "Programs and Features". You may have to install python too (good luck, might be easier to install Linux).

Once django is installed, you will also need to install the following packages. They can all be installed using pip:
    
    pip install django-extensions
    
    pip install djangorestframework
    
    pip install pillow

Now you're ready to rock! Using the terminal, navigate to the folder: 
    
    ~/website-root-shroomworks
you downloaded before where the file "manage.py" is located and run:

    python manage.py runserver

Go to your browser and access http://localhost:8000/ and you should be able to check the website!

Use this to login: 
    
    username: "test" 
    
    password: "123456"
    
If you have any question, please let us know at vrgimael@gmail.com
