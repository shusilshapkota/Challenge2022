# Shopify Winter 2022 Challenge

This app is created as a solution to the Shopify's Developer Intern Challenge for the year of 2022. The app is hosted using [pythonanywhere.com](https://www.pythonanywhere.com/) and can be accessed using [shusil.pythonanywhere.com](http://shusil.pythonanywhere.com/)

## Image-Repo

This app is called Image-Repo and it lets user upload images to their account. Users can upload one or many images by logging in to the site. 

When user uploads the image, they have an option to either make their images private or make them public. If the user makes the images public, anyone that browses the website can see the images but if the user makes the images private, then only the user himself can view the images after logging in. 

## Tech Stack

This app's backend is built using Django, and SQLite database. The frontend is built using HTML, JavaScript and CSS. 

### How to use the app?

There are two ways to test and access the application:

* Accessing the app via website
* Cloning the repo and running it locally

### Accessing the app via website:

1. Please go to [shusil.pythonanywhere.com](http://shusil.pythonanywhere.com/). Images you see in this page are all public images uploaded by the users.
2. Click Register on the top right bar. You can register using any emails, emails verification is turned off to make it easier to test out the core functionality.
3. Once you register, it will take you to the login page where you can sign in.
4. Once signed in, you will see all of your private pictures if you have uploaded previously. You'll also see an upload option if you want to upload the images.
5. If you want to logout, you can simply click on the logout button on the top right bar which will take you to the public pics page.

### Cloning the repo and running it locally:
1. Clone the repo using: `git clone https://github.com/shusilshapkota/Challenge2022.git`
2. cd into the Challenge2022 directory: `cd Challenge2022` and then cd into image_repo directory `cd image_repo`
3. Then, install all the required packages to run this app locally: `pip3 install -r requirements.txt`
4. Now, run database migrations: `python3 manage.py migrate`
5. Run the server: `python3 manage.py runserver`
6. Now, access the app via [localhost:8000](http://localhost:8000/) and follow the steps in "Accessing the app via website" section above to test out the functionality 

