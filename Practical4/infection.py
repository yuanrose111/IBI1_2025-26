# 1. Define basic variables：初始感染人数initial_infected、日增长率growth_rate（小数）、总学生数total_students=91
# 2. Define a counter：days=0（records the number of infected days），current_infected=initial_infected（current number of infected people, initial value
# 3. Create a while loop：continuously execute the loop when current_student <total_student
# 4. loop operation：print the number of infected people onn the current day --calculate the number of infected people on the next day --add 1 to the number of days
# 5. After the cycle ends : print the final number of infected individuals(≥91) and the total number of infected days

initial_infected = 5
growth_rate = 0.4
total_students = 91

# define counter :
current_infected = initial_infected  
days = 0 #initial is 0
print("daily changes in IBI1 class infected count：")

# while：calculate when infected don not finish
while current_infected < total_students:
    print(f"at {days} day：{current_infected:.1f} people infected")  
    current_infected = current_infected * (1 + growth_rate)  #calculate the number of next day
    days += 1  

print(f"at {days} day：{current_infected:.1f} people infected （all people (91) in the class have been infected)")

print(f"spend ：{days} day to infected all the people")
