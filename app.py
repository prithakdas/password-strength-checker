import string
import random
from flask import Flask, render_template, request

app = Flask(__name__)

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = not any(char.isdigit() for char in password)
    uppercase_error = not any(char.isupper() for char in password)
    lowercase_error = not any(char.islower() for char in password)
    symbol_error = not any(char in string.punctuation for char in password)

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    error_count = sum(errors)

    if error_count == 0:
        return "Strong", None
    elif error_count <= 2:
        suggestions = []
        if uppercase_error: suggestions.append("an uppercase letter")
        if symbol_error: suggestions.append("a special character (@#$&!)")
        return "Moderate", f"Try adding: {', '.join(suggestions)}"
    else:
        return "Weak", generate_strong_password()

def generate_strong_password():
    chars = string.ascii_letters + string.digits + "@#$&!"
    return ''.join(random.choice(chars) for i in range(12))

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    suggestion = None
    if request.method == 'POST':
        pwd = request.form.get('password')
        result, suggestion = check_password_strength(pwd)
    return render_template('index.html', result=result, suggestion=suggestion)

if __name__ == '__main__':
    app.run(debug=True)