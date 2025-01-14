#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/parameter')
def print_string(string):
    print(string)
    return string

@app.route('/count/parameter')
def count(number):
    return '\n'.join(str(i) for i in range(number)) + '\n'

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'dev':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    return "invalid operation"
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
