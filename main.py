from pyscript import display, document

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

display(f"Name: {studentname}", target="name")
display(f"Age: {studentage}", target="age")
display(f"Height: {height142} cm", target="height")
display(f"Countries to visit: {', '.join(countries_to_visit)}", target="countries")
display(f"New student: {student_type}", target="student")
display(f"Favorite color: {my_favorites['color']}, car brand: {my_favorites['car_brand']}, shoe size: {my_favorites['shoe_size']}, best friend: {my_favorites['best_friend']}", target="favorites")
display(f"Favorite fruits: {', '.join(favorite_fruits)}", target="fruits")
display(f"Days of the week: {', '.join(days_of_week)}", target="days")

def solve(event):
    for target in ["add", "sub", "mul", "div", "floor", "mod", "exp"]:
        document.getElementById(target).innerHTML = ""

    text1 = document.getElementById("text1").value
    text2 = document.getElementById("text2").value

    if text1 == "" or text2 == "":
        display("Please fill in both boxes.", target="add")
        return

    num1 = float(text1)
    num2 = float(text2)

    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    divide = num1 / num2 if num2 != 0 else "Cannot divide by 0"
    floor = num1 // num2 if num2 != 0 else "Cannot divide by 0"
    mod = num1 % num2 if num2 != 0 else "Cannot divide by 0"
    exp = num1 ** num2

    display(f"{num1} + {num2} = {add}", target="add")
    display(f"{num1} - {num2} = {sub}", target="sub")
    display(f"{num1} * {num2} = {mul}", target="mul")
    display(f"{num1} / {num2} = {divide}", target="div")
    display(f"{num1} // {num2} = {floor}", target="floor")
    display(f"{num1} % {num2} = {mod}", target="mod")
    display(f"{num1} ** {num2} = {exp}", target="exp")