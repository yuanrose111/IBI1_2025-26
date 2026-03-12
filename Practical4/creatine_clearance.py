# Practical 4: Creatine Clearance Calculator 
# 1. Define input variables: age (years), weight (kg), gender (male/female), Cr (creatinine, μmol/l)
# 2. Set up input validation rules and a validity flag:
#    - Age must be less than 100 years
#    - Weight must be between 20 kg and 80 kg (exclusive)
#    - Creatinine (Cr) must be between 0 μmol/l and 100 μmol/l (exclusive)
#    - Gender must be either 'male' or 'female' (case-sensitive)
# 3. Check each input against validation rules:
#    - If any input is invalid, update validity flag and record error message
# 4. Calculate Creatinine Clearance (CrCl) only if all inputs are valid:
#    - Formula: CrCl = [(140 - age) * weight] / (72 * Cr)
#    - Multiply by 0.85 if gender is female (no multiplier for male)
# 5. Output results:
#    - If valid: Print the calculated CrCl value
#    - If invalid: Print the error message with variables that need correction

# Step 1: Define input variables (modify these values for different test cases)
age = 42               # Age in years
weight = 68            # Weight in kilograms
gender = "female"      # Gender: only 'male' or 'female' is valid
cr = 75                # Creatinine concentration in μmol/l

# Step 2: Initialize validation variables
is_input_valid = True  # Flag to check if all inputs are valid
error_message = "Invalid input(s): "  # Store error details for invalid inputs

# Step 3: Perform input validation 
# Validate age
if age >= 100:
    is_input_valid = False
    error_message += "age must be less than 100; "
# Validate weight
if weight <= 20 or weight >= 80:
    is_input_valid = False
    error_message += "weight must be 20 < kg < 80; "
# Validate creatinine concentration
if cr <= 0 or cr >= 100:
    is_input_valid = False
    error_message += "Cr must be 0 < μmol/l < 100; "
# Validate gender
if gender not in ["male", "female"]:
    is_input_valid = False
    error_message += "gender must be 'male' or 'female'; "

# Step 4: Calculate and output CrCl if inputs are valid
if is_input_valid:
    # Base CrCl calculation (applies to male)
    crcl = ((140 - age) * weight) / (72 * cr)
    # Adjust for female (multiply by 0.85)
    if gender == "female":
        crcl = crcl * 0.85
    # Print the result with 2 decimal places for readability
    print(f"Valid Inputs → Creatinine Clearance (CrCl): {crcl:.2f} ml/min")
else:
    # Print only the error message 
    print(error_message.rstrip("; "))