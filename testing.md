# Manual Testing for Kenan's Cook Book
## Testing Responsiveness
#### Am I Responsive
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618914685/images/albums/MS3/Testing/responsive/responsive-am-i_sybx2p.png" width="450"/>

#### iPhone
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618914685/images/albums/MS3/Testing/responsive/responsive-iphone_lklivp.png" width="250"/>

#### iPad
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618914685/images/albums/MS3/Testing/responsive/responsive_ipad_iz8tuc.png" width="350"/>


## Testing user stories as a cooking enthusiast:
## User Story 1
- I want to quickly find recipes for dinner.

### Action
Navigate to recipes page by entering the web address or clicking the recipes nav link

### Expectation
The recipes page displays a list of the recipes paginated in groups of 3 

### Result
The page loads correctly, the nav link works and results are displayed paginated in groups of 3. 

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618416856/images/albums/MS3/features/recipes_qeuw7w.png" width="250"/>

## User Story 2
- I want to be able to easily sort and search for a specific recipe.

### Action
Type the name of a recipe, nationality, cooking time or difficulty in the search bar and click search or hit enter. The user can also click a list of predefined filters in the filter area

### Expectation
The page will return the desired results on the recipes page. If no results were found the user will be prompted that there were no matching recipes based on their criteria. If search is clicked or enter is pressed with an empty field the user will be prompted to enter text. If the user clicked on of the filters the results should be returned based on that filter, paginated if need be. 

### Result
The searched query is returned on the recipes page using pagination to seperate the results in groups of 3 only if there are more then 3 results. If the search did not have any results the user is shown a flash message saying that their query returned no results. The flash message also shows the name of the searched term and the amount of results if any.If no text was entered in the search bar the user will be prompted to enter text. When a filter button is clicked the user is shown a list of the relevant recipes paginated as needed. 

#### Search returns results
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618912281/images/albums/MS3/Testing/search-true_qr2wfx.png" width="250"/>  
  
#### Search returns no results  
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618912281/images/albums/MS3/Testing/search_false_qcg5mx.png" width="250"/>

#### No text is entered in the search bar
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618912742/images/albums/MS3/Testing/no-text_gmmikb.png" width="250"/>

#### Filter button is clicked
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618915769/images/albums/MS3/Testing/filter-by-british_du7ik8.png" width="250"/>


## User Story 3
- I want to be able to login to the site.

### Action
User clicks the login nav link or the link on the create account page then fills out their credentials and clicks login.

### Expectation
The user will be prompted with a login screen and prompted to enter their login credentials. If the user leaves fields blank the user will be prompted to fill in the required input fields. If the user gets the username or password wrong the user will be prompted with a flash message. 

### Result
The user is logged in and redirected to the user profile page. If the username or password is wrong a flash message will be shown. If the user leaves a required field blank they will be prompted to enter text. 

#### Login is successful
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618913255/images/albums/MS3/Testing/login-redirected_jbks56.png" width="250"/> 

#### Login is unsuccessful
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618913255/images/albums/MS3/Testing/login-wrong_ndbksw.png" width="250"/> 

#### No text entered in an input field
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618913255/images/albums/MS3/Testing/login-no-text_nndoph.png" width="250"/> 


## User Story 4
- I want to be able to create a profile.

### Action
The user clicks the register nav link or the link on the login page to register a new account. Then fills out their details and clicks create an account. 

### Expectation
The user will be able to fill out their details and create a profile/login to the website. The user will be prompted if the desired username is taken. The user will be prompted if they have used too few or many characters. The user will be prompted if they have left any required fields empty. 

### Result
The user enters all required information and is succesfully registered and redirected to their profile page. If the user leaves any required fields blank or fills them in incorrectly the user is prompted to fill them in. If the username is taken the user is prompted by a flash message. 

#### Registration is successful
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618914268/images/albums/MS3/Testing/register-success_noygtl.png" width="250"/> 

#### Username is taken
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618914268/images/albums/MS3/Testing/register-username-exists_mgngxf.png" width="250"/> 

#### No text entered in an input field
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618914268/images/albums/MS3/Testing/register-no-text_wvjnba.png" width="250"/>


## User Story 5
- I want to be able to Add my own recipes.

### Action
The user clicks add a recipe on the nav bar and inputs their selected data then clicks submit.

### Expectation
The recipe is added to the database and available and searchable by all users on the recipes page. If required field is missing the user will be prompted. The cloudinary widget will show when user clicks upload an image. More input fields will be added when the user clicks the green plus button or removed when the user clicks the red minus button. When all the info is filled in and the user clicks submit the recipe will be displayed publically on the recipes page. If the user did not submit and image the placeholder image will take its place on the recipe page.

### Result
The user has filled out everything correctly and the recipe is submitted and displayed on the recipes page. If the user has left out a required field the user is prompted to input text. The cloudinary widget opens and uploads pictures as required. Clicking the green plus and red minus buttons add or remove the extra input fields as required. Page holder image is displayed if no picture is uploaded. 

#### Recipe creation is successful
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618916178/images/albums/MS3/Testing/add%20recipe/add-recipe-success-no-pic_olkmnb.png" width="250"/> 

#### Missing an input field text
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618916178/images/albums/MS3/Testing/add%20recipe/add-recipe-no-text_jkhduk.png" width="250"/> 

#### Clicking to add input
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618916178/images/albums/MS3/Testing/add%20recipe/add_recipe_new_ing_ub95tl.png" width="250"/> 

#### Clicking to upload an image
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618916178/images/albums/MS3/Testing/add%20recipe/add-recipe-upload-image_pnyea9.png" width="250"/> 

## User Story 6
- I want to be able to Edit and Delete my recipes.

### Action
The user clicks edit or delete on a recipe they have created on their profile page. 

### Expectation
When the user clicks delete on one of the recipes they have created, a modal will pop up and ask them to confirm or cancel. Upon clicking confirm the recipe will be deleted from the database. Upon clicking cancel the modal will be closed and the user redirected back to their profile page. When the user clicks Edit the user will be redirected to the edit recipe page where the information about the recipe will be filled in. Upon submiting the edit the recipe will appear on the recipes page with the new information. 

### Result
The user clicks delete the modal is triggered, if the user clicks delete on the modal the recipe is deleted and a flash message is displayed notifying the user. If the user clicks cancel the modal is closed and user is redirected to the user profile page. The user clicks edit and is redirected to the edit recipe page where the input fields are filled out. The user can edit the fields as need be and add or remove steps or ingredients. The user can upload a new image. The user clicks submit and the edited recipe is saved to the database and viewable on the recipes page.


#### Edit Recipe
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618917788/images/albums/MS3/Testing/delete%20and%20edit/edit-recipe_vxretq.png" width="250"/>

#### Edit successful
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618917788/images/albums/MS3/Testing/delete%20and%20edit/edit-recipe-updated_u9kaa7.png" width="250"/>

#### Recipe deleted
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618917788/images/albums/MS3/Testing/delete%20and%20edit/recipe-deleted_snh51j.png" width="250"/>

#### Delete confirm modal
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618917788/images/albums/MS3/Testing/delete%20and%20edit/delete-recipe-modal_z0hbyc.png" width="250"/>

## User Story 7 
- I want the recipes I have created publically available to all other active people on the site.

See result from User Story 5 as this has already been covered.

### User Story 8
- I want a page with all my recipes I have created that I can easily access once logged in. 

### Action
The user clicks the User Profile link on the nav bar when logged in. 

### Expectation
The user will be redirected to the User Profile page where all the reciped they have created are displayed with an edit and delete button present on each item. 

### Result
The user is redirected to the user profile page. All recipes created by the user are present. Each recipe has an edit and delete button. 

#### User profile page
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618913255/images/albums/MS3/Testing/login-redirected_jbks56.png" width="250"/>

#### Edit and delete buttons
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618918739/images/albums/MS3/Testing/edit-delete-btns_gycih1.png" width="250"/>


## User Story 9
- I want to be able to purchase any kitchen equipment I may need.

### Action 
The user clicks the premium utensils link on the nav bar

### Expectation
The user will be redirected to the products page where results will be shown paginated in groups of 3 where needed. The user also has the option to filter by product rating, knives, pots, pans and utensils. Upon clicking a filter products will be displayed accordingly. The items will have links to purchase via a third party retailer. 

### Result
The user is redirected to the product page where all results are shown paginated in groups of 3. If the user clicks any of the filter buttons the results are filtered and displayed correctly. Each item has the links to purchase via a third party retailer and the links open in a new window. 

#### Products page
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618919369/images/albums/MS3/Testing/products_page_xtuemt.png" width="250"/>

#### Filtered by rating
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618919407/images/albums/MS3/Testing/products-filter_rzngjc.png" width="250"/>

#### Buy now links
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618919476/images/albums/MS3/Testing/products-buy-now_vkynut.png" width="250"/>

## Testing user stories as the site designer:

## User Story 1
- I want the process of displaying content to be fast and seamless.

### Action 
Loading any page on the site

### Expect
All pages to load in a timely manner and feel fast

### Result
All pages load very quickly thanks to the speed of [MongoDB](http://www.mongodb.com) as well as using the [Cloudinary](http://www.cloudinary.com) caching server to host all images. 

## User Story 2 
- I want to dynamically generate content based on collections in MongoDB.

### Action
Opening the recipes or product page dynamically adds content based on the data stored in MongoDb.

### Expect
All content should be dynamically generated and layed out based on entries in mongoDB.

### Result
Recipes and products get generated based on the data stored in mongodb and are displayed according to my styles and filters.

#### Recipes page
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618920119/images/albums/MS3/Testing/recipes_victcg.png" width="250"/>

#### Products page
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618919369/images/albums/MS3/Testing/products_page_xtuemt.png" width="250"/>


## User Story 3
- I want the site to be eye catching and engaging.

### Action
The user looks at the design and layout of the site.

### Expectation 
The user will have a good experience and find the layout eye-catching, simple and easy to use. 

### Result
The site looks good and clean according to friends and family. 

## User Story 4
- I want the site to be easy to use and intuitive with clear stylistic choices.

### Action
The user engaging with the site and navigating its functions.

### Expectation
The user will not struggle to find any content and easily navigate around the site and make use of the features. 

### Results
According to friends and family the site is easy to use, creating an account and logging in is easy and intuitive. Creating deleting and editing recipes is strait forward and obvious. 

## User Story 5 
- I want the site to be as bug free as possible.

## Action
The user browses the site and navigates its functions

## Expect 
The site should work without any bugs that hinder funtionality or break the site. The user shouldn't leave the site due to bugs and glitches. Any remaining bugs should not break functions or cause a poor user experience. 

## Result
Very few bugs are present and none break functionality or cause a bad user experience. 
See Issues and Toubleshooting section in this document.

## User Story 6
- I want the site to be responsive to a large number of devices and screen sizes.  
See the Testing Responsiveness section at the beginning of this document. 


## Code Validation
### HTML
The HTML validated with errors for open elements however I think this is due to using flask and Jinja templating to dynamically add content as I have checked all my templates for open tags and I do not find any. Not sure how to validate properly however the site works fine as it should. [W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2F8080-amber-moth-tp3mni7w.ws-eu03.gitpod.io%2Frecipes)
![HTML Validation](https://res.cloudinary.com/dyxe4g62g/image/upload/v1618922410/images/albums/MS3/validation/html_fg1yrh.png)



### CSS
My CSS file validated without any errors on the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/validator)
![CSS Validation](https://res.cloudinary.com/dyxe4g62g/image/upload/v1618921380/images/albums/MS3/validation/css_s1auqi.png)

### Custom 404 SEO Validation 
My Site passed custom 404 SEO validation on [SEO Site Checkup](https://seositecheckup.com/tools/custom-404-error-page-test)  
![SEO Validation](https://res.cloudinary.com/dyxe4g62g/image/upload/v1618921301/images/albums/MS3/validation/SEO-validation_k9rv9b.png)

### PEP8 Compliance
My Site passed PEP8 compliance at [PEP8 Checker](http://pep8online.com/checkresult)
![SEO Validation](https://res.cloudinary.com/dyxe4g62g/image/upload/v1618921766/images/albums/MS3/validation/PEP8_check_ppeevc.png)

### JSHint Validation
My JS functions showed no errors and only a few warnings about ES6 compatibility in Mozilla.
![Main JS](https://res.cloudinary.com/dyxe4g62g/image/upload/v1618921948/images/albums/MS3/validation/JSHint1_zd8gu3.png)  
![Materialize doc ready Validation](https://res.cloudinary.com/dyxe4g62g/image/upload/v1618921949/images/albums/MS3/validation/JSHint2_cz9irl.png) 

## Issues and Troubleshooting

### Issues I encountered and solved     
- I couldnt fetch the name attribute on login - login method only inserted user attribute into cookies so when the user was creating a recipie it was insterting null into the created by field. I fixed this by adding the name field into cookie upon login.  
- I couldnt make the search function work - Tutor support Kevin assisted me in fixing this by adding the propper form action to my search bar as well as using request.args.get("query") instead of request.form.get("query") 
- integrating cloudinary api - after upload from widget the image url will be passed to the hidden input on the form and then gets written by the back end and saved to the db.  
- Edit recipie functionality, have the data from the recipe im editing already filled in and find a way to show multiple steps/ingredients that were filled in previously - this was fixed with for loop and using loop index to number ingredient and steps.  
- Recipe sorting list as string - fixed by storing cook time as integer rather than string in MongoDB  
- Changing underline color of the materialize input fields - I had to look at the materialize rules targeting these items and had to use !important as I could not create a specific enough rule. 
- Pagination not getting propper offset - fixed by using offset = offset = (page - 1) * 3  
 
  

## Known Bugs
I unfortunately ran out of time to fix the remaining bugs, however they do not break any functionality or cause a bad user experience in my opinion.  
- Chrome autofill background color is white in search and some form elements - I tried many many solutions from stack overflow and other sites, however no matter what I tried Chrome still uses that horrible white background color when it autoflls form data. 
- Possible unbalanced tuple unpacking with sequence defined at line 237 of flask_paginate - Im not sure what this means, I spent a long time googling and couldn't find a solution. I think its something to do with the flask paginate component which I used for pagination. 
- When editing recipe if you click add ingredient or step it adds another ingredient 2/3/4 field instead of the next one. I couldnt find a way to solve this is when creating the recipe it uses a variable which increases and decreases when you add or remove input fields. However I couldn't find a way to store this variable somehow so that when editing a recipe it will remember the variable.
- The nationality field is not pre filled in when editing a recipe - I could not get this to work in time, The only way I could think of doing this is to use a Jinja if statement but you would have to add the whole input field in every if and elif and would add a lot more coding and wouldn't look clean.  
