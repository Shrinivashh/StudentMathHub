from flask import Flask, request, render_template, redirect, url_for
import math

app = Flask(__name__, static_url_path='/static')


def matrix_multiplication(A, B):
    rows_A = len(A)
    common_dim = len(A[0])
    cols_B = len(B[0])

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(common_dim):
                result[i][j] += A[i][k] * B[k][j]

    return result


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    return render_template('calculate.html')


@app.route('/multiplication_table', methods=['GET', 'POST'])
def multiplication_table():
    table = None
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            table = [[i * j for j in range(1, number + 1)] for i in range(1, 11)]
        except ValueError:
            table = 'Error: Invalid input. Please enter a positive integer.'

    return render_template('multiplication_table.html', table=table)


@app.route('/log', methods=['POST', 'GET'])
def log():
    log_result = None
    if request.method == 'POST':
        try:
            number = float(request.form['number'])
            option = request.form['option']
            if option == 'e':
                log_result = math.log(number)
            elif option == '10':
                log_result = math.log10(number)
            elif option == '2':
                log_result = math.log2(number)
        except (ValueError, KeyError) as e:
            log_result = str(e)

    return render_template('log.html', log=log_result)


@app.route('/factorial', methods=['POST', 'GET'])
def factorial_value():
    factorial_result = None
    if request.method == 'POST':
        try:
            number = int(request.form['factorial'])
            if number < 0:
                factorial_result = "Factorial is not defined for negative numbers."
            else:
                factorial_result = math.factorial(number)
        except ValueError:
            factorial_result = "Please enter a valid integer."
    return render_template('factorial.html', factorial=factorial_result)


@app.route('/solutions', methods=['GET', 'POST'])
def solutions():
    solutions_result = None
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])

            discriminant = b ** 2 - 4 * a * c
            if discriminant < 0:
                solutions_result = "No real solution"
            elif discriminant == 0:
                solutions_result = f"One real solution: {(-b) / (2 * a)}"
            else:
                solutions_result = f"Two real solutions: {(-b - math.sqrt(discriminant)) / (2 * a)}, {(-b + math.sqrt(discriminant)) / (2 * a)}"
        except ValueError:
            solutions_result = "Please enter valid numbers for a, b, and c."

    return render_template('solutions.html', solutions=solutions_result)


@app.route('/asci', methods=['GET', 'POST'])
def ascii_value():
    aci = None
    if request.method == 'POST':
        letter = request.form['letter']
        aciv = ord(letter)
        aci = aciv
    return render_template('asci.html', ascii_value=aci)


@app.route('/square_cube_root', methods=['GET', 'POST'])
def square_cube_root():
    lis_t = None
    if request.method == 'POST':
        try:
            number = float(request.form['number'])
            option = int(request.form['option'])
            if option == 2:
                sq_root = math.sqrt(number)
                lis_t = sq_root
            elif option == 3:
                cub_root = number ** (1 / 3)
                lis_t = cub_root
        except ValueError:
            sq_root = cu_root = "Please enter a valid number."
    return render_template('square_cube_root.html', square_cube_root=lis_t)


@app.route('/area_perimeter', methods=['GET', 'POST'])
def area_perimeter():
    total_area = None
    if request.method == 'POST':
        choice = request.form['choice']
        if choice == 'Area':
            shape = request.form['shape']
            if shape == 'Rectangle':
                length = float(request.form['length'])
                width = float(request.form['width'])
                area = length * width
                total_area = area
            elif shape == 'Square':
                side = float(request.form['side'])
                area = side ** 2
                total_area = area
            elif shape == 'Circle':
                radius = float(request.form['radius'])
                area = math.pi * radius ** 2
                total_area = area
            elif shape == 'Triangle':
                base = float(request.form['base'])
                height = float(request.form['height'])
                area = 0.5 * base * height
                total_area = area
        elif choice == 'Perimeter':
            shape = request.form['shape']
            if shape == 'Rectangle':
                length = float(request.form['length'])
                width = float(request.form['width'])
                perimeter = 2 * (length + width)
                total_area = perimeter
            elif shape == 'Square':
                side = float(request.form['side'])
                perimeter = 4 * side
                total_area = perimeter
            elif shape == 'Circle':
                radius = float(request.form['radius'])
                perimeter = 2 * math.pi * radius
                total_area = perimeter
            elif shape == 'Triangle':
                base = float(request.form['base'])
                height = float(request.form['height'])
                perimeter = base + math.sqrt(base ** 2 + height ** 2) + height
                total_area = perimeter
    return render_template("area_perimeter.html", area_perimeter=total_area)


@app.route('/matrix', methods=['GET', 'POST'])
def matrix():
    if request.method == 'POST':
        rowsA = int(request.form['rowsA'])
        colsA = int(request.form['colsA'])
        rowsB = int(request.form['rowsB'])
        colsB = int(request.form['colsB'])

        if colsA != rowsB:
            return render_template('matrix.html', error="Matrix multiplication is not possible with these dimensions.")

        A = []
        for i in range(rowsA):
            row = []
            for j in range(colsA):
                element = float(request.form[f'a-{i}-{j}'])
                row.append(element)
            A.append(row)

        B = []
        for i in range(rowsB):
            row = []
            for j in range(colsB):
                element = float(request.form[f'b-{i}-{j}'])
                row.append(element)
            B.append(row)

        result = matrix_multiplication(A, B)
        return render_template('matrix.html', result=result)

    return render_template('matrix.html')


if __name__ == '__main__':
    app.run(debug=True)
