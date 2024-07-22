# Recipe Book

Site owner mission. User mission

## Design

### Wire Frames

- Add here

## Existing Features

### Login

- Login

### CRUD

- Blurb on user capabilities

- __Javascript__
 - Custom script which allows users to dynamically add new ingredient forms to a formset on a webpage. When the user clicks the "Add Ingredient" button, a new form is created by cloning the first form in the set, updating its attributes to ensure uniqueness, clearing its values, and appending it to the formset.

- Event Listener for DOMContentLoaded:
   - document.addEventListener('DOMContentLoaded', function() {
    // Code here runs after the DOM is fully loaded });
 - This event listener waits for the entire HTML document to be fully loaded and parsed before executing the enclosed function. This ensures that all the DOM elements are available for manipulation.

- Select DOM Elements:
 - const addIngredientBtn = document.getElementById('add-ingredient-btn');
     - addIngredientBtn: Selects the button with the ID add-ingredient-btn which will be used to add new ingredient forms.
  - const ingredientFormset = document.querySelector('#ingredient-forms');
     - ingredientFormset: Selects the container with the ID ingredient-forms which holds the ingredient forms.
 - const totalFormsInput = document.querySelector('#id_recipeingredient_set-TOTAL_FORMS');
     - totalFormsInput: Selects the input element with the ID id_recipeingredient_set-TOTAL_FORMS, which tracks the total number of forms.

- Initial Form Count:
  - let formNum = ingredientFormset.children.length;
    - formNum: Initializes a counter to keep track of the number of existing forms. It is set to the number of children within the ingredientFormset container.

- Add Event Listener to Button:
  - addIngredientBtn.addEventListener('click', 
    function() {
    // Code here runs when the add button is clicked
    });





### Templates
- __base.html__

  - blurb on base.html

- __recipe_list.html__
  
  - blurb on recipe list

- __create_recipe.html__
  
  - blurb on recipe list

- __recipe_detail.html__
  
  - blurb on recipe detail

- __edit_recipe.html__
  
  - blurb on edit recipe

- __delete_recipe.html__
  
  - blurb on delete


### Additional features
- add quantities model
- Add other
- improve ingredient selection

## Testing

### Testing Table

| Action    | Expectation | Result | 
| ---------|:-------------------:|----------|
| update | update | update |


### Validator Testing
- __HTML__
  - No errors returend through W3C validator.

- __CSS__
  - No errors returned through jigsaw validator.

- __JS__
  - No errors returned through jshint validator.

- __Python__
  - No errors returned through PEP8 CI Python Linter.


### Unfixed Bugs
- __TBU__
  - blurb


## Deployment

- The site was deployed to GitHub pages. The steps to deploy are as follows:
  - In the GitHub repository, navigate to the Settings tab
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

- Cloning and forking

- The live link can be found here: