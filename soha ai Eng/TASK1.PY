#Project Cost Calculator
team_members = int(input("How many people are on the team? "))
project_duration_months= int(input("How many months will the project take? ")) 
monthly_salary=float(input("What is the monthly salary?"))
total_cloud_cost=float(input("What is the total cloud cost?"))
Salary_cost=team_members*project_duration_months*monthly_salary
Subtotal = Salary_cost + total_cloud_cost
VAT=Subtotal * 0.14
Total=Subtotal + VAT
print(f"THE TOTAL COST OF THE PROJECT IS {Total}")


