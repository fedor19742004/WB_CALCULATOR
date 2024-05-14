from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
# Логирование действий пользователя
def log_user_action(action):
    with open('user_actions.log', 'a') as file:
        file.write(action + '\n')

# Логирование вычислительных операций
def log_calculation_operation(operation):
    with open('calculation_operations.log', 'a') as file:
        file.write(operation + '\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    operator = request.form['operator']

    try:
        result = eval(num1 + operator + num2)
        log_user_action(f'Calculating: {num1} {operator} {num2}')
        log_calculation_operation(f'{num1} {operator} {num2} = {result}')
        return render_template('index.html', result=result)
    except Exception as e:
        log_user_action(f'Failed calculating: {num1} {operator} {num2}')

if __name__ == '__main__':
    app.run(debug=True)