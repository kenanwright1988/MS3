# Manual Testing for Kenan's Cook Book
## Testing Responsiveness
#### Am I Responsive
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618914685/images/albums/MS3/Testing/responsive/responsive-am-i_sybx2p.png" width="450"/>

#### iPhone
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618914685/images/albums/MS3/Testing/responsive/responsive-iphone_lklivp.png" width="250"/>

#### iPad
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618914685/images/albums/MS3/Testing/responsive/responsive_ipad_iz8tuc.png" width="350"/>


## Testing user stories
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
The user clicks delete the modal is triggered, if the user clicks delete on the modal the recipe is deleted and a flash message is displayed notifying the user. If the user clicks cancel the modal is closed and user is redirected to the user profile page. The user clicks edit and is redirected to the edit recipe page where the input fields are filled out*. The user can edit the fields as need be and add or remove steps or ingredients**. The user can upload a new image. The user clicks submit and the edited recipe is saved to the database and viewable on the recipes page.

### Known Bugs in Edit Form
See Issues and Toubleshooting in [readme](README.md)  
*The nationality field is not pre filled in, I could not get this to work in time.  
** When adding or removing ingredients the step number and ingredient numbers get messed up. I did not have time to fix this or find a solution before the deadline.   

#### Edit Recipe
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618917788/images/albums/MS3/Testing/delete%20and%20edit/edit-recipe_vxretq.png" width="250"/>

#### Edit successful
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618917788/images/albums/MS3/Testing/delete%20and%20edit/edit-recipe-updated_u9kaa7.png" width="250"/>

#### Recipe deleted
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618917788/images/albums/MS3/Testing/delete%20and%20edit/recipe-deleted_snh51j.png" width="250"/>

#### Delete confirm modal
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618917788/images/albums/MS3/Testing/delete%20and%20edit/delete-recipe-modal_z0hbyc.png" width="250"/>

