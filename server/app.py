#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:str>')
def print_string(str):
    print(str)
    return str

@app.route('/count/<string:num>')
def count(num):
    num = int(num)
    numbers = []
    for i in range(num):
        numbers.append(str(i)+"\n")
    return ''.join(numbers)

@app.route('/math/<string:num1>/<string:operation>/<string:num2>')
def math(num1, operation, num2):
    num1=int(num1)
    num2=int(num2)
    
    if operation == '+':
        return str(num1+num2)
    elif operation == '-':
        return str(num1-num2)
    elif operation == '*':
        return str(num1*num2)
    elif operation == 'div':
        return str(num1/num2)
    elif operation == '%':
        return str(num1%num2)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
