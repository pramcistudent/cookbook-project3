# [Cookbook](https:)

This project is part of my [Code Institute](https://codeinstitute.net/) Full Stack Software Development, specifically the **Data Centric Development** module. The objective for this milestone project is to "*Create a web application that allows users to store and easily access cooking recipes*", using the **CRUD** operations of **C**reate, **R**ead, **U**pdate, and **D**elete for their recipes.
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
## Features
### Existing Features
**Register Account**
- Anybody can register for free and create their own unique account. 
**Log In to Account**
- Allows new users to register for a free account. The form's username field only accepts alphanumeric values.
**Log Out of Account**
- Allows users to logout of their account by clicking the 'Logout' link in the navbar/sidenav. Upon clicking the button, the user session ends.
- **Flash Messages** 
- Displayed at the top of the page below the navbar. These messages differ based on user interaction and provides helper messages for users.
**View All Recipe**
- On the *home* page pagination is used for the unfiltered results to display 8 recipes per page. The previous page button is only available if there is a previous page. The next page button is only available if there is a next page.
**Add a Recipe**
- [**C**RUD] Create or 'add' a new recipe will be available for users who are logged in. The 'Add' button is located in navigation bar next to the username. This will take the user to a full page form that will allow them to submit detailed information about a new recipe as well as adding an image (a remotely hosted image, added by URL) dynamically adding and removing ingredients and steps in the recipe method.
**View a Recipe**
- [C**R**UD] Read or 'review' recipes, either from the main page, or the user recipe page. Users can click on the recipe card to displays the recipe's full details on a page.
**Update a Recipe**
- [CR**U**D] Update or 'edit' is available only when the user is logged in. Clicking it takes the user to the Edit Recipe page and only the author of the recipe can edit the recipe.
**Delete a Recipe**
- [CRU**D**] Delete or 'remove' recipe is only available if the user is logged in and if the user added that recipe.
### Features Left to Implement
- Hash passwording for login / Register
- print / email receipe
- Account profile page
- Favorites page
- Commets section
- Date recipe added
- Able to upload image
- Star ratings
- Allow for multipul images of the recipe to be displayed
## Technologies Used


## Testing

##### Login Page

###### Guest User

###### Sign In

###### Sign Up

###### Navigation links

###### All Recipes

###### Filtered Recipes

###### Pagination/Search result summary

###### Recipe cards

##### Add Recipe Page (Registered users only)

##### Recipe Details Page 

###### My recipes (Registered users only)

###### Logout 

##### Responsiveness Testing

##### HTML and CSS validator

##### Cross Browser Testing

###### Accessibility / Screen Reader Application Testing

##### Dev Tools

##### HTML and CSS validator

##### Cross Browser Testing

###### Accessibility / Screen Reader Application Testing

## Deployment

## Credits

#### Content

#### Acknowledgements