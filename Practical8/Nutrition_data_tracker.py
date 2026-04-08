class food_item:
    def __init__(self, name, calories, protein, carbohydrates, fat):
        # Initialize food item with nutritional data
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat


def calculate_daily_nutrition(food_list):
    """
    Calculates total daily nutrition from a list of food_item objects,
    and reports warnings if calorie or fat intake exceeds thresholds.
    
    Args:
        food_list (list): List of food_item instances consumed in 24 hours
    
    Returns:
        tuple: (total_calories, total_protein, total_carbs, total_fat)
    """
    # Initialize total values to 0
    total_calories = 0.0
    total_protein = 0.0
    total_carbs = 0.0
    total_fat = 0.0

    # Sum nutrition from all food items
    for item in food_list:
        total_calories += item.calories
        total_protein += item.protein
        total_carbs += item.carbohydrates
        total_fat += item.fat

    # Print daily nutrition summary
    print(f"Total Calories: {total_calories} kcal")
    print(f"Total Protein: {total_protein} g")
    print(f"Total Carbohydrates: {total_carbs} g")
    print(f"Total Fat: {total_fat} g")

    # Check and print warnings for excess intake
    if total_calories > 2500:
        print("WARNING: Calorie intake exceeds 2500 kcal!")
    if total_fat > 90:
        print("WARNING: Fat intake exceeds 90 g!")

    # Return total values for further use if needed
    return total_calories, total_protein, total_carbs, total_fat


# ------------------------------
# Example Usage of the Class and Function
if __name__ == "__main__":
    # Create individual food items (example values)
    apple = food_item("Apple", 60, 0.3, 15, 0.5)
    chicken_breast = food_item("Chicken Breast (100g)", 165, 31, 0, 3.6)
    white_rice = food_item("White Rice (1 cup cooked)", 205, 4.3, 45, 0.4)
    avocado = food_item("Avocado (1 medium)", 240, 3, 9, 22)
    pizza = food_item("Pepperoni Pizza (1 slice)", 285, 12, 30, 15)
    chocolate_cake = food_item("Chocolate Cake (1 slice)", 350, 4, 50, 15)

    # List of food consumed in 24 hours
    daily_food = [
        apple,
        chicken_breast,
        white_rice,
        avocado,
        pizza,
        pizza,  # 2 slices of pizza
        chocolate_cake
    ]

    # Calculate and print daily nutrition
    calculate_daily_nutrition(daily_food)