# Manual Testing for Kenan's Cook Book

## Testing user stories
### User Story 1
- I want to quickly find recipes for dinner.

#### Action
Navigate to recipes page by entering the web address or clicking the recipes nav link

#### Expectation
The recipes page displays a list of the recipes paginated in groups of 3 

#### Result
The page loads correctly, the nav link works and results are displayed paginated in groups of 3. 

[<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618416856/images/albums/MS3/features/recipes_qeuw7w.png" width="250"/>](Recipes page)

#### Tested On
- Google Chrome
- Mozilla firefox
- Chrome for Ios
- safari


### User Story 2
- I want to be able to easily sort and search for a specific recipe.

#### Action
Type the name of a recipe, nationality, cooking time or difficulty in the search bar and click search or hit enter

#### Expectation
The page will return the desired results on the recipes page. If no results were found the user will be prompted that there were no matching recipes based on their criteria. 

#### Result
The searched query is returned on the recipes page using pagination to seperate the results in groups of 3 only if there are more then 3 results. If the search did not have any results the user is shown a flash message saying that their query returned no results. 

[<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1618416856/images/albums/MS3/features/recipes_qeuw7w.png" width="250"/>](search results)