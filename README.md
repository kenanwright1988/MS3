# Kenan's Cook Book

Welcome to Kenan's Cook Book. For my third milestone project I have decided to make a cook book website with the goal of selling a fictional range of kitchen utensils. The site is based on the flask framwork to generate content from a database and present it to the user. I have made sure to include CRUD functionality as well as make use of a login/register/logout system which is authenticated and all passwords are protected by a hash for security.
 
## UX

### Site Goals

The goal of Kenan's Kitchen is to provide cooking enthusiasts a place to discover new recipes as well as create and edit their own which will then be available to all other users. The site will offer a range of premium utensils for sale to users to ensure they can easily make their selected recipe as well as generate revenue for the site. 
 
### User Stories
#### As an cooking enthusiast: 
- I want to quickly find recipes for dinner.
- I want to be able to easily sort and search for a specific recipe.
- I want to be able to create a profile and login to the site.
- I want to be able to Add, Edit and Delete my own recipes.
- I want the recipes I have created publically available to all other active people on the site.  
- I want a page with all my recipes I have created that I can easily access once logged in. 
- I want to be able to purchase any kitchen equipment I may need. 

#### As the site designer:
- I want the process of displaying content to be fast and seamless.
- I want to dynamically generate content based on collections in MongoDB.
- I want the site to be eye catching and engaging.
- I want the site to be easy to use and intuitive with clear stylistic choices.
- I want the site to be as bug free as possible.
- I want the site to be responsive to a large number of devices and screen sizes. 

### Wireframes

To see all wireframes created in the UX stage [Click Here!](/wireframes.md)


## Features

### Recipes(Home) Page
- Recipes are dynamically generated from the MongoDB collection and displayed on this page using Jinja templating language.
- Pagination is used to allow the user to sort through the pages of results.
- Recipes are displayed paginated in groups of 3 as they are quite large and more than that would require too much scrolling.
- The search bar allows users to search for recipe names, and difficulty etc and returns paginated results based on an index in the mongodb collection.
- The filter area allows users to click on a preset button which will display results based on their selection eg. Nationality or cook time. 

### Premium Utensils Page
- Products are dynamically generated from the MongoDB collection and displayed on this page using Jinja templating language.
- Pagination is used to allow the user to sort through the pages of results.
- Products are displayed paginated in groups of 3 as they are quite large and more than that would require too much scrolling.
- The filter area allows users to click on a preset button which will display results based on their selection eg. User rating or pots/pans etc.
- Users have the option to buy a product from one of our fictional retail partners eg. Amazon, Ebay or Buy n Large.

### Registration page
- This page allows users to create a profile and login credentials to fully utilize the website.
- The user is preseted with a registration form in which they will need to provide a Username, Name Email address and password. The password is hashed so that when its stored in the DB it will not be visible. 
- The backend python will check weather the desired username is taken or not and prompt the user accordingly. 
- All input fields are required as well as having min/max values. All input fields have the required attribute and will promp the user if something was inputed incorrectly. 
- Once all criteria have been filled in and submited the backend python will add the details to a new entry within the database as well as putting the user into the session cookie then redirect them to their user profile page. 

### User Profile Page
- This page Shows the user all recipes they have created.
- Pagination is used to allow the user to sort through the pages of results.
- Recipes created by the user will be displayed here with the option to edit and delete recipes.
- Clicking edit will take the user to the edit recipe page.
- clicking delete will trigger a confirmation modal which asks the user to confirm they would like to delete the recipe. 

### Edit Recipe Page
- This page takes the recipe id of the recipe the user wants to edit and returns a form that is mostly prefilled out with the existing recipe details. 
- The user has the option of changing any of the input fields as well as uploading a new image via the Cloudinary upload widget. 
- When the user clicks submit the backend python will update the DB as neccesary with all new inputed data. 


### Add a Recipe Page
- The add a recipe page has a form where users can input data for the recipe as well as upload an image and add more ingredients and steps.
- Images are handled by the Cloudinary Upload widget and API. 
- When a user uploads an image using the upload widget Cloudinary returns an object with the details of the image. I have used Javascript to append the URL of the uploaded image to a hidden image URL input field which then saves the URL of the image in the DB under the img_url attribute. 
- I have used Jquery to append extra fields if needed by clicking the green + button which will add another input. I have a variable which increases when the plus button is clicked and decreases when the - button is clicked. This ensures that the label will be correct eg. Ingredient 1, ingredient 2, Step 1, Step 2 etc. 
- If a user does not upload an image a placeholder image will be displayed in its place. 
- Once the submit button is clicked the backend python will insert all the information into an entry within the DB. 

### Logout Page
- When the user clicks logout the user is removed from the session cookie using the .pop() function. 
- The browser is then redirected to the login page. 
- A Flash message will appear saying that the user has successfully been logged out. 

### Login Page
- The login page presents the user with a form that takes the username and password field. 
- The backend python will check if the username exists and if the password is valid and promt the user accordingly via Flash messages. 
- If all login conditions are met the user will be redirected to the User profile page. 


### Existing Features
- Login - Allows users to login to their account.
- Register - allows users to create a profile which will allow them to create, edit and delete their own recipes.
- Create Recipe - allows users to create their own recipes and upload an image to be shared with the whole site.
- Edit Recipe - allows users to edit recipes they have already created.
- Delete - allows users to delete recipes they have already created. 
- Search - allows users to search for recipes based on Name, cooking time, difficulty or nationality. 
- Pagination - returns results in groups of 3 and allows users to click through pages instead of having to scroll all the way down the page.
- Filter buttons(Recipes) - Allows users to select predefined results based on cooking time or nationality.
- Filter buttons(Products) - Allows users to select predefined results based on product rating or pots/pans etc.

### Features Left to Implement
- Another feature idea

## Technologies Used


**Flask-Paginate** - Flask paginate was used to paginate returned database queries. 
**MongoDB** - MongoDB was used to store and access database items.
**Flask** - Used as web app framework to make creating the app faster and easier. 
**Heroku** - Heroku was used to host the live version of this app.
**Github** - Github was used for storing my code and version control.  
**Gitpod** - I used Gitpod to code the site as well as push updates to Github.  
**Python** - Python 3 was used for the backend code to run the app and logic.  
**Prettier** Code - I used Beautify to keep my code properly indented and easily readable.  
**HTML5** - The core of the site was built with HTML version 5.  
**CSS** - CSS was used to style the website and define fonts and layout.  
**Materialize CSS** - Materialize was used for layout and alignment with the grid system, forms and inputs as well as pagination.   
**JavaScript** - JavaScript was used to provide logic and funtionality to certain elements such as the Cloudinary upload widget..  
**Jquery** - Jquery was used to write the click functions that append extra inputs to the forms as well as to enable Materialize selectors and sidenav.   
**Font Awesome** - Social Media icons from Font Awesome.  
**Google Chrome** - The website was built and tested in google Chrome.  
**Auto close tag** - self explanitory.  
**HTML hint** - for faster coding.  
**Cloudinary** - Hosting images to make the site load faster as well as the API for image uploads and the upload widget.  
**Apple Safari** - Used for testing.
**Mozilla Firefox** - Used for testing.
**Opera** - Used for testing.

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X