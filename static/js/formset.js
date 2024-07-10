document.addEventListener('DOMContentLoaded', function() {
    const addIngredientBtn = document.getElementById('add-ingredient-btn');
    const ingredientFormset = document.querySelector('#ingredient-formset');
    let formNum = ingredientFormset.children.length;

    addIngredientBtn.addEventListener('click', function() {
        // Clone the first form and reset its values
        const newForm = ingredientFormset.children[0].cloneNode(true);
        const formRegex = new RegExp(`form-(\\d){1}-`, 'g');
        newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`);
        
        // Append the new form to the formset
        ingredientFormset.appendChild(newForm);
        
        // Increment the total number of forms
        formNum++;

        console.log('New form added. Total forms:', formNum);
    });
});
