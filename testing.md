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

### Tested On
- Google Chrome
- Mozilla firefox
- Chrome for Ios
- Safari


## User Story 2
- I want to be able to easily sort and search for a specific recipe.

### Action
Type the name of a recipe, nationality, cooking time or difficulty in the search bar and click search or hit enter

### Expectation
The page will return the desired results on the recipes page. If no results were found the user will be prompted that there were no matching recipes based on their criteria. If search is clicked or enter is pressed with an empty field the user will be prompted to enter text. 

### Result
The searched query is returned on the recipes page using pagination to seperate the results in groups of 3 only if there are more then 3 results. If the search did not have any results the user is shown a flash message saying that their query returned no results. The flash message also shows the name of the searched term and the amount of results if any.If no text was entered in the search bar the user will be prompted to enter text.

#### If search returns results
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618912281/images/albums/MS3/Testing/search-true_qr2wfx.png" width="250"/>  
  
#### If search returns no results  
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618912281/images/albums/MS3/Testing/search_false_qcg5mx.png" width="250"/>

#### If no text is entered in the search bar
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618912742/images/albums/MS3/Testing/no-text_gmmikb.png" width="250"/>

### Tested On
- Google Chrome
- Mozilla firefox
- Chrome for Ios
- Safari

## User Story 3
- I want to be able to login to the site.

### Action
User clicks the login nav link or the link on the create account page then fills out their credentials and clicks login.

### Expectation
The user will be prompted with a login screen and prompted to enter their login credentials. If the user leaves fields blank the user will be prompted to fill in the required input fields. If the user gets the username or password wrong the user will be prompted with a flash message. 

### Result
The user is logged in and redirected to the user profile page. If the username or password is wrong a flash message will be shown. If the user leaves a required field blank they will be prompted to enter text. 

#### If login is successful
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618913255/images/albums/MS3/Testing/login-redirected_jbks56.png" width="250"/> 

#### If login is unsuccessful
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618913255/images/albums/MS3/Testing/login-wrong_ndbksw.png" width="250"/> 

#### If no text entered in an input field
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618913255/images/albums/MS3/Testing/login-no-text_nndoph.png" width="250"/> 

### Tested On
- Google Chrome
- Mozilla firefox
- Chrome for Ios
- Safari

## User Story 4
- I want to be able to create a profile.

### Action
The user clicks the register nav link or the link on the login page to register a new account. Then fills out their details and clicks create an account. 

### Expectation
The user will be able to fill out their details and create a profile/login to the website. The user will be prompted if the desired username is taken. The user will be prompted if they have used too few or many characters. The user will be prompted if they have left any required fields empty. 

### Result
The user enters all required information and is succesfully registered and redirected to their profile page. If the user leaves any required fields blank or fills them in incorrectly the user is prompted to fill them in. If the username is taken the user is prompted by a flash message. 

#### If registration is successful
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618914268/images/albums/MS3/Testing/register-success_noygtl.png" width="250"/> 

#### If username is taken
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618914268/images/albums/MS3/Testing/register-username-exists_mgngxf.png" width="250"/> 

#### If no text entered in an input field
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618914268/images/albums/MS3/Testing/register-no-text_wvjnba.png" width="250"/>

### Tested On
- Google Chrome
- Mozilla firefox
- Chrome for Ios
- Safari

