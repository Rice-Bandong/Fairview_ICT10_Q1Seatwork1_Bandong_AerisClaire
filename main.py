from pyscript import document, display

studentname = "Aeris Bandong"

studentage = 15 

height142 = 142.24  

countries_to_visit = ["Japan", "Korea", "Canada"]

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
Name: {studentname}<br>
Age: {studentage}<br>
Height: {height142} cm<br>
Countries to visit: {', '.join(countries_to_visit)}<br>
New student: {student_type}<br>
Favorite color: {my_favorites['color']}<br>
Car brand: {my_favorites['car_brand']}<br>
Shoe size: {my_favorites['shoe_size']}<br>
Best friend: {my_favorites['best_friend']}<br>
Favorite fruits: {', '.join(favorite_fruits)}<br>
Days of the week: {', '.join(days_of_week)}
"""
display(info_text, target="info", append=False)

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

    result_text = f"""
    {n1} + {n2} = {add}<br>
    {n1} - {n2} = {sub}<br>
    {n1} * {n2} = {mul}<br>
    {n1} / {n2} = {div}<br>
    {n1} // {n2} = {floor}<br>
    {n1} % {n2} = {mod}<br>
    {n1} ** {n2} = {exp}
    """
    display(result_text, target="results", append=False)