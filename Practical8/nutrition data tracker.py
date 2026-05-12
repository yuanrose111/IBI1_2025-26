# Practical 8 - Task 2: Nutrition Data Tracker
# IBI1 2025/26

class food_item:
    """Store name, calories, protein, carbohydrates, fat for a food item"""
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat


def calculate_daily_nutrition(food_list):
    """
    Calculate total nutrition from a list of food_item objects.
    Print summary and warnings if calories > 2500 or fat > 90 g.
    """
    total_cal = 0
    total_prot = 0
    total_carb = 0
    total_fat = 0

    for food in food_list:
        total_cal += food.calories
        total_prot += food.protein
        total_carb += food.carbs
        total_fat += food.fat

    print("\n===== 24-Hour Nutrition Summary =====")
    print(f"Total Calories:      {total_cal:.2f} kcal")
    print(f"Total Protein:       {total_prot:.2f} g")
    print(f"Total Carbohydrates: {total_carb:.2f} g")
    print(f"Total Fat:           {total_fat:.2f} g")

    if total_cal > 2500:
        print("WARNING: Calories exceed 2500 kcal!")
    if total_fat > 90:
        print("WARNING: Fat exceeds 90 g!")

    return total_cal, total_prot, total_carb, total_fat


# Example usage (required)
if __name__ == "__main__":
    print("===== Nutrition Tracker Example =====")
    apple = food_item("Apple", 60, 0.3, 15, 0.5)
    chicken = food_item("Chicken Breast", 165, 31, 0, 3.6)
    rice = food_item("Rice", 130, 2.7, 28, 0.3)

    daily_food = [apple, chicken, rice, rice]
    calculate_daily_nutrition(daily_food)

    # Warning test
    print("\n===== Warning Test =====")
    big_meal = food_item("Big Meal", 3000, 50, 100, 100)
    calculate_daily_nutrition([big_meal])