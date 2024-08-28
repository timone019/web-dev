# Explanation of Changes

## Ingredient Model:

Quantity: 
- Changed from CharField to DecimalField for better numerical representation.

Unit: 
- Added a new unit attribute to specify the unit of measurement for the quantity.

### Recipe Model:

Difficulty: 
- Changed to use choices for better data integrity.

Description: 
- Added a description attribute to provide more details about the recipe.

Instructions: 
- Added an instructions attribute to provide step-by-step cooking instructions.

## Exercise 2.3 Changes

### Ingredient Model: 
- Changed quantity from CharField to DecimalField and added unit attribute.

### Recipe Model: 
- Changed difficulty to use choices, and added description and instructions attributes.

- These changes improve the data structure, ensure better data integrity, and provide more detailed information about the recipes and ingredients.