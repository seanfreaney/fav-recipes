document.addEventListener('DOMContentLoaded', function() {
    alert('formset.js is loaded');
    const addIngredientBtn = document.getElementById('add-ingredient-btn');
    const ingredientFormset = document.querySelector('#ingredient-forms');
    let formNum = ingredientFormset.children.length;

    addIngredientBtn.addEventListener('click', function() {
        alert('Add Ingredient button clicked');
        if (ingredientFormset.children.length > 0) {
            const newForm = ingredientFormset.children[0].cloneNode(true);
            const formRegex = new RegExp(`form-(\\d){1}-`, 'g');
            newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`);
            ingredientFormset.appendChild(newForm);
            formNum++;
            alert('New form added. Total forms: ' + formNum);
        } else {
            alert('No forms to clone.');
        }
    });
});
