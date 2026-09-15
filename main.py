from pyscript import document, display

my_name = "Aeris Bandong" 
my_age = 15
height_cm142 = 142.24 
countries_to_visit_list = ["Japan", "Korea", "Canada"] 
student_type = False 

my_favorites = { 
    "color": "Blue",
    "car_brand": "Toyota",
    "shoe_size": 6.5,
    "best_friend": "Anchovy"
}

favorite_fruits = {"Apple", "Mango", "Rambutan", "Grape", "Orange"}  
days_of_week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun") 

info_text = f"""
Name: {my_name} ({type(my_name).__name__})
Age: {my_age} ({type(my_age).__name__})
Height: {height_cm142}cm ({type(height_cm142).__name__})
Countries: {', '.join(countries_to_visit_list)} ({type(countries_to_visit_list).__name__})
New Student: {student_type} ({type(student_type).__name__})
Best Friend: {my_favorites['best_friend']} ({type(my_favorites).__name__})
Fruits: {', '.join(favorite_fruits)} ({type(favorite_fruits).__name__})     
Days: {len(days_of_week)} ({type(days_of_week).__name__})
"""
display(info_text, target="info", innerHTML=True)

def solve(event):
    n1 = float(document.getElementById("num1").value)
    n2 = float(document.getElementById("num2").value)

    add = n1 + n2        
    sub = n1 - n2          
    mul = n1 * n2          
    div = n1 / n2 if n2 != 0 else "Cannot divide by 0"          
    floor = n1 // n2 if n2 != 0 else "Cannot divide by 0"       
    mod = n1 % n2 if n2 != 0 else "Cannot divide by 0"         
    exp = n1 ** n2        

    res_text = f"""
    <strong>Results:</strong><br>
    {n1} + {n2} = {add}<br>
    {n1} - {n2} = {sub}<br>
    {n1} * {n2} = {mul}<br>
    {n1} / {n2} = {div}<br>
    {n1} // {n2} = {floor}<br>
    {n1} % {n2} = {mod}<br>
    {n1} ** {n2} = {exp}
    """
    display(res_text, target="results", append=False)