document.addEventListener('DOMContentLoaded', function() {
    const addIngredientBtn = document.getElementById('add-ingredient-btn');
    const ingredientFormset = document.querySelector('#ingredient-forms');
    const totalFormsInput = document.querySelector('#id_recipeingredient_set-TOTAL_FORMS');

    let formNum = ingredientFormset.children.length;

    addIngredientBtn.addEventListener('click', function() {
        if (ingredientFormset.children.length > 0) {
            const newForm = ingredientFormset.children[0].cloneNode(true);
            const formRegex = new RegExp(`recipeingredient_set-(\\d+)-`, 'g');
            const newFormNum = formNum;

            newForm.innerHTML = newForm.innerHTML.replace(formRegex, `recipeingredient_set-${newFormNum}-`);

            // Update the ID attributes for each input
            newForm.querySelectorAll('[id]').forEach(function(element) {
                const newId = element.id.replace(formRegex, `recipeingredient_set-${newFormNum}-`);
                element.id = newId;
            });

            // Update the name attributes for each input
            newForm.querySelectorAll('[name]').forEach(function(element) {
                const newName = element.name.replace(formRegex, `recipeingredient_set-${newFormNum}-`);
                element.name = newName;
            });

            // Clear the values of the cloned form fields
            newForm.querySelectorAll('input, select, textarea').forEach(function(element) {
                if (element.type === 'checkbox' || element.type === 'radio') {
                    element.checked = false;
                } else {
                    element.value = '';
                }
            });

            ingredientFormset.appendChild(newForm);
            formNum++;
            totalFormsInput.value = formNum;  // Update TOTAL_FORMS with the new count
        }
    });
});
