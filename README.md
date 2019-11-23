# [Cookbook](https://cookbook-project3.herokuapp.com/)

This project is part of my [Code Institute](https://codeinstitute.net/) Full Stack Software Development, specifically the **Data Centric Development** module. The objective for this milestone project is to "*Create a web application that allows users to store and easily access cooking recipes*", using the **CRUD** operations of **C**reate, **R**ead, **U**pdate, and **D**elete for their recipes.

---

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)
3. [**Technologies Used**](#technologies-used)
    - [**Version Control**](#version-control)
    - [**Hosting**](#hosting)
4. [**Testing**](#testing)
    - [**Login Page**](#login-page)
    - [**Home Page**](#home-page)
    - [**Add Recipe Page (Registered users only)**](#add-recipe-page)
    - [**Recipe Details Page**](#recipe-details-page)
    - [**Username (Registered users only)**](#username)
    - [**Responsiveness Testing**](#responsiveness-testing)
5. [**Code Validation**](#code-validation)
    - [**Cross Browser Testing**](#cross-browser-testing)
6. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)
7. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Acknowledgements**](#acknowledgements)

---

## UX
This application is an online cookbook - a place where users can find recipes for any occasion. Users can also create their own free account and add any number of recipes which they can share with other users and visitors.
The front-end display and functionality uses HTML, CSS and JavaScript. The back-end functionality uses Python, Flask and MongoDB.
### User Stories
"**_As a user, I would like to_** _____"
- view the site from any device (mobile, tablet, desktop). 
- view all recipes as a Guest. 
- filter recipes by Cuisine type. 
- filter recipes by Dish Type.
- filter recipes by Allergen. 
- create my own account as a registered user.
- see instructions on how to add a recipe.
- add my own recipes.
- edit my own recipes.
- delete my own recipes.
- be able to log out.
### Design
I received inspiration for the styling of my app from a website I came across called [**_A Basic Cook_**](http://www.abasiccook.com/). I thought the clean simplistic look of the site looked really modern and professional, so I wanted to reflect this in my own app.
#### Framework
- [Materialize 1.0.0](https://materializecss.com/)
    - I really like the modern and clean layout of Materialize as a framework, with its simple-to-understand documentation.
- [jQuery 3.4.0](https://code.jquery.com/jquery/)
    - In an effort to keep the JavaScript minimal, I have decided to use jQuery as foundation to my scripts framework.
- [Flask 1.0.2](http://flask.pocoo.org/)
    - Flask is a microframework that I've used to render the back-end Python with the front-end Materialize.

##### back to [top](#table-of-contents)

---

## Features
### Existing Features
- **Register Account** - Allows new users to register for a free account. The form's username field only accepts alphanumeric values. I've included checks to ensure that the username doesn't already exist in the database before users are successfully registered. Passwords stored in the database are hashed for security purposes.
- **Log In to Account** - Allows existing users to login to their account. The form's username field only accepts alphanumeric values. I've included authorization checks to verify the username and password (hashed password) against the details stored in the database before users can be logged in.
- **Log Out of Account** - Allows users to logout of their account by clicking the 'Logout' link in the navbar/sidenav. Upon clicking the button, the user session ends.
- **Flash Messages** - Displayed at the top of the page below the navbar. These messages differ based on user interaction and provides helper messages for users.
- **View All Recipe** - On the *home* page pagination is used for the unfiltered results to display 8 recipes per page. The previous page button is only available if there is a previous page. The next page button is only available if there is a next page.
- **Add a Recipe** - [**C**RUD] Create or 'add' a new recipe will be available for users who are logged in. The 'Add' button is located in navigation bar next to the username. This will take the user to a full page form that will allow them to submit detailed information about a new recipe as well as adding an image (a remotely hosted image, added by URL) dynamically adding and removing ingredients and steps in the recipe method.
- **View a Recipe** - [C**R**UD] Read or 'review' recipes, either from the main page, or the user recipe page. Users can click on the recipe card to displays the recipe's full details on a page.
- **Update a Recipe** - [CR**U**D] Update or 'edit' is available only when the user is logged in. Clicking it takes the user to the Edit Recipe page and only the author of the recipe can edit the recipe.
- **Delete a Recipe** - [CRU**D**] Delete or 'remove' recipe is only available if the user is logged in and if the user added that recipe.
### Features Left to Implement
In an ideal world, there are a couple functions that I would've loved to have completed but didn't have the time or knowledge on how to implement these features.
- **Print / Email** - Being able to print the recipe as well as able to email the recipe to friends and family.
- **Account profile** - Allows for the user to personalise their account and add additional information about the user such as images etc.
- **Favorites** - Quick and easy to way for the user to review and store recipes they like.
- **User comments** - Having a comments section allows for all users to review and leave feedback on recipes.
- **Date recipe added** - Shows when the recipe was added to the database.
- **Able to upload images** - Currently you can only use the URL to upload an image, having an additional feature which allows the user to upload from a local drive.
- **Recipe star ratings** - Upvote so users can see how popular a recipe is, this can then be used to sort recipes by most liked.
- **Buy the ingredients** - Feature to take the user, for example to a site where the ingredients can be purchased.

##### back to [top](#table-of-contents)

---

## Technologies Used
- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses **HTML** to create the basic elements and content of my app.
- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
    - The project uses **CSS** to apply the custom styles to my app.
- [**Materialize**](https://materializecss.com/)
    - The project uses the **Materialize** framework to add a responsive grid system, prebuilt components, plugins built on jQuery, and Materialize styles to my app, before adding my custom styles.
- [**jQuery**](https://jquery.com)
    - The project uses **jQuery** as the primary JavaScript functionality. This is both the standard jQuery that is built with Materialize components.
- [**Python**](https://www.python.org/)
    - The project uses **Python** as the back-end programming language for my app.
- [**PyMongo**](https://api.mongodb.com/python/current/)
    - The project uses **PyMongo** as the Python API for MongoDB. This API enables linking the data from the back-end database to the front-end app.
- [**Flask**](https://flask.palletsprojects.com/en/1.0.x/)
    - The project uses **Flask**, which is a Python microframework.
- [**Jinja**](https://jinja.palletsprojects.com/en/2.10.x/)
    - The project uses **Jinja** for templating with Flask in the HTML code. I used **Jinja** to simplify my HTML code, avoid repetition, and allow simpler linking of the back-end to the front-end.
- [**MongoDB**](https://cloud.mongodb.com/)
    - The project uses **MongoDB** to store the database in the cloud. The information displayed in the front-end app is pulled from the database store.
- [**Google Fonts**](https://fonts.google.com/)
    - The project uses **Google Fonts** to style the text and suit my chosen theme. The brand logo uses the *_Liu Jian Mao Cao_* font and the rest of the site uses the *_Cairo_* font.
- [**Font Awesome**](https://fontawesome.com/)
    - The project uses **Font Awesome** for the various icons in my app.
- [**AWS Educate Cloud9**](https://aws.amazon.com/education/awseducate/)
    - I've used **AWS Educate Cloud9** as the development environment to write the code for my website.
### Version Control
- [**Git**](https://git-scm.com/)
    - I've used **Git** as a version control system to regularly add and commit changes made to project in AWS Educate Cloud9, before pushing them to GitHub.
- [**GitHub**](https://github.com/)
    - I've used **GitHub** as a remote repository to push and store the committed changes to my project from Git.
### Hosting
- [**Heroku**](https://www.heroku.com/)
    - I've used **Heroku** as the hosting platform to deploy my app.

##### back to [top](#table-of-contents)

---

## Testing
All tests were carried out manually. Testing process was as follows:
##### Login Page
###### Logo
* Click on *logo* and verify that page refreshes.
###### Guest User
* Click on *continue* button and verify that website home page appears.
###### Sign In
* Click on *sign in* button with all or some incomplete fields and verify that an error message (next to the first incomplete field) appears stating, 'Please fill in this field'. Form does not get submitted unless all input fields are filled.
* Enter incorrect username or/and password, click on *sign in* button and verify that error message appears stating, 'Login failed. Incorrect username or/and password. Please try again.'
* Enter correct username (case-insensitive) and password (case-sensitive), click on *sign in* button and verify that website home page appears
###### Sign Up
* Click on *sign up* button with all or some incomplete fields and verify that an error message (next to the first incomplete field) appears stating, 'Please fill in this field'. Form does not get submitted unless all input fields are filled.
* Enter existing username (case-insensitive), any full name and password, click on *sign up* button and verify that error message appears stating, 'Sorry that username already exists. Please use a different username.'
* Enter new username, any full name and password, click on *sign up* button and verify that error message appears stating, 'You are successfully registered. Please login below.'
##### Home Page
###### Navigation links
* Click on *logo* or *Home* and verify that home page appears.
* Click on *Add Recipe* and verify that page appears with *Add a Recipe* form. (Registered users only)
* Click on *Username* and verify that dropdown menu appears with menu items *My recipes* and *Logout*. (Registered user only)
* Click on *My recipes* and verify that all recipes added by current user appears on *My recipes* webpage. (Registered users only)
* Click on *Logout* and verify that session ends and login page appears. (Registered user only)
* Click on *Sign in* and verify that login page appears with sign in tab active.
* Click on *Sign up* and verify that login page appears with sign up tab active.
* Click on *Dish Types*, *Cuisines* or *Allergens* and verify that dropdown menu shows all available dish types, cuisine names, and main allergens respectively.
###### All Recipes
* Verify that home page loads with a display of all recipes available on the website.
###### Filtered Recipes
* Click on any dish type in *Dish Types* and verify that only recipes with dish type will appear. 
* Click on any cuisine name in *Cuisines* and verify that only recipes with cuisine name will appear.
* Click on any allergen in *Allergens* and verify that only allergen free recipes will appear.
###### Pagination/Search result summary
* Go to home page and verify that maximum 8 recipes are displayed per page.
* Verify that pagination only appears when page number is greater than one.
* Click on previous or next arrow and verify that page display recipes in the previous and next page respectively.
* Click on previous arrow when first page is active and verify that it is disabled.
* Click on next arrow when last page is active and verify that it is disabled.
* Click on any page number and verify that page displays the recipes on that page.
* Click on any page number and verify that active page is shown by black background.
###### Recipe cards
* Verify that all images are responsive
* Click on *View this Recipe* and verify that webpage with all recipe details appear.
* Click on *three vertical dots* and verify that *short recipe description* slides up.
##### Add Recipe Page (Registered users only)
* Click on 'Save recipe' button with all or some incomplete fields and verify that an error message (next to the first incomplete field) appears stating, 'Please fill in this field'. Form does not get submitted unless all input fields are filled.
* Click on *add* icon and verify that an input field for ingredient or method step appears with *delete* icon. 
* Click on *delete* icon and verify that the input field next to it is removed.
* Verify that at least one ingredient or method step is required to submit the form.
* Enter image in a format other than url and verify that the form is not submitted unless correct url format is entered.
* When all the fields are filled in, click on 'Save recipe' button and verify that:
  * user is redirected to *My recipes* page.
  * new recipe is added to the page.
##### Recipe Details Page 
* Click on 'View this Recipe' button on any recipe card (either on home page or any other webpage with recipe cards) and verify that recipe page opens with recipe details in it.
* Verify that *Edit* and *Delete* icon only appears if user is the author of recipe. 
* Click on *Edit* icon and verify that *Edit recipe* form page appears: 
  * Verify that all input fields are prepopulated with the previously saved values.
  * Verify that all the tests mentioned in *Add Recipe Page* section pass here too.
  * Click on *Save changes* and verify that:
    * user is redirected to *My Recipes* page.
    * recipe is successfully changed
* Click on *Delete* icon and verify that:
    * user is redirected to *My Recipes* page.
    * recipe is deleted from *My recipes* page and from the app.
##### Username (Registered users only)
###### My recipes 
* Verify that all recipes displayed on *My recipes* page are current users recipes.
###### Logout 
* Click *Logout* and verify that current user session is cleared and user is redirected to login page.
##### Responsiveness Testing
Dev Tools, Galaxy S9 and iPad were used to test the appearance of app on mobile/tablet screen size.  
Following features were verified:
* A *Menu* icon appears on the left corner and all menu items disappear.
* On clicking *Menu* icon, side navigation slides in with all menu items.
* In login page, container widths change responsively for different screen sizes.
* Materializecss cards for displaying recipes, cuisine names and dish types rearranges responsively for different screen sizes.
* Images changes responsively for different screen sizes.
* Recipe page rearranges images and texts responsively for different screen sizes.
### Code Validation
- [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) used to validate my HTML code.
    - The W3C Validator tool doesn't recognise the Jinja templating, which has resulted in showing a lot of errors in relation to the Jinja code. However, all other code is validating fine.
- [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) used to validate my CSS code.
- [Esprima Syntax Validator tool](http://esprima.org/demo/validate.html) used to validate my JavaScript syntax.
- [Pep8 Online tool](http://pep8online.com/) used to validate my Python syntax.
##### Cross Browser Testing
- [CanIuse.com](https://caniuse.com/) - was used to check browser support for CSS codes and use correct prefixes, where required.
- The website was tested to function as expected on following browsers:
  - Chrome
  - Firefox
  - IE 
  - Edge 
  - Safari

##### back to [top](#table-of-contents)

---

## Deployment
### Local Deployment
Please note - in order to run this project locally on your own system, you will need the following installed:
- [Python3](https://www.python.org/downloads) to run the application.
- [PIP](https://pip.pypa.io/en/stable/installing) to install all app requirements.
- Any IDE such as [Microsoft Visual Studio Code](https://code.visualstudio.com).
- [GIT](https://www.atlassian.com/git/tutorials/install-git) for cloning and version control.
- [MongoDB](https://www.mongodb.com) to develop your own database either locally or remotely on MongoDB Atlas.
Next, there's a series of steps to take in order to proceed with local deployment:
- Clone this GitHub repository by either clicking the green *Clone or download* button and downloading the project as a zip-file (remember to unzip it first), or by entering the following into the Git CLI terminal:
    - `https://github.com/pramcistudent/cookbook-project3.git`
9. Navigate to the `.bashrc` terminal and add your MongoDB URI in the following format:
    - `MONGO_URI="insert your mongo uri details here"`
- Install all requirements from the [requirements.txt](https://github.com/pramcistudent/cookbook-project3/blob/master/requirements.txt) file using this command:
    - `sudo -H pip3 -r requirements.txt`
- Sign up for a free account on [MongoDB](https://www.mongodb.com) and create a new Database called **Cookbook**. The *Collections* in that database should be as follows:

**ALLERGENS**
```
_id: <ObjectId>
allergen_name: <array>
```
**CUISINES**
```
_id: <ObjectId>
cuisine_name: <array>
```
**DISHES**
```
_id: <ObjectId>
dish_type: <array>
```
**RECIPES**
```
_id: <ObjectId>
recipe_title: <string>
recipe_author_name: <string>
recipe_image_url: <string>
recipe_short_description: <string>
recipe_prep_time: <string>
recipe_cook_time: <string>
total_time: <string>
recipe_serves: <string>
allergen_name: <array>
cuisine_name: <string>
dish_type: <string>
recipe_ingredients: <array>
recipe_steps: <array>
```
**USERS**
```
_id: <ObjectId>
fullnamee: <string>
username: <string>
password: <string>
```
- You should now be able to run the app locally using the `python3 run.py` command.
- The app should now be running on *localhost* on an address similar to `http://127.0.0.1:5000`. Simply copy/paste this into the browser of your choice!
### Remote Deployment
This site is currently deployed on [Heroku](https://www.heroku.com/) using the **master** branch on GitHub. To implement this project on Heroku, the following steps were taken:
1. Create a **requirements.txt** file so Heroku can install the required dependencies to run the app.
    - `sudo pip3 freeze --local > requirements.txt`
    - My file can be found [here](https://github.com/pramcistudent/cookbook-project3/blob/master/requirements.txt).
2. Create a **Procfile** to tell Heroku what type of application is being deployed, and how to run it.
    - `echo web: python run.py > Procfile`
    - My file can be found [here](https://github.com/pramcistudent/cookbook-project3/blob/master/Procfile).
3. Sign up for a free Heroku account, create your project app, and click the **Deploy** tab, at which point you can *Connect GitHub* as the Deployment Method, and select *Enable Automatic Deployment*.
4. In the Heroku **Settings** tab, click on the *Reveal Config Vars* button to configure environmental variables as follows:
    - **IP** : `0.0.0.0`
    - **PORT** : `5000`
    - **MONGO_URI** : `<link to your Mongo DB>`
    - **SECRET_KEY** : `<your own secret key>`
5. Your app should be successfully deployed to Heroku at this point.

##### back to [top](#table-of-contents)

---

## Credits
#### Content
- Template Inheritance - [Jinja Article](https://jinja.palletsprojects.com/en/2.10.x/templates/)
- Flash Messages - [Flask Article](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/)
- Register and Login page backend code - [Pretty Printed](https://www.youtube.com/watch?list=PLXmMXHVSvS-Db9KK1LA7lifcyZm4c-rwj&v=vVx1737auSE&app=desktop) & [Flask docs](http://flask.pocoo.org/docs/1.0/quickstart/#sessions) 
- How to convert strings to integers - [stackoverflow](https://stackoverflow.com/questions/38857366/integer-gets-converted-to-string-when-passed-into-jinja-template)
- For Loops - [stackoverflow](https://stackoverflow.com/questions/34877236/for-loop-not-working-in-jinja-flask)
- Dynamically adding and removing form input fields - [Youtube video](https://www.youtube.com/watch?v=jSSRMC0F6u8)
- Pagination - [Codementor](https://www.codementor.io/arpitbhayani/fast-and-efficient-pagination-in-mongodb-9095flbqr) & [Flask-paginate](https://pythonhosted.org/Flask-paginate/) & [Stackoverflow](https://stackoverflow.com/questions/8676455/flask-current-page-in-request-variable)
- Bug found in materializecss **disabled** class was used to disable left and right chevron in pagination [Resolved issue](https://github.com/Dogfalo/materialize/issues/3835)  
- Recipe for my site - [BBC Food Website](https://www.bbc.co.uk/food)
#### Acknowledgements
- I would like to thank my mentor [Guido Cecilio](https://github.com/guidocecilio) for all his help and support during the development of this project. 
- I would also like to thank other code institute students for sharing their projects which was extremely useful in designing this website. 
- Thanks to the Slack community for their feedback and help on how to debug my Python code.
### Disclaimer
This project is for educational purposes only.

##### back to [top](#table-of-contents)

---