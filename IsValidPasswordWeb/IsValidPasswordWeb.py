from flask import Flask, render_template_string, request
import numpy as np

app = Flask(__name__)

# Validation functions
def is_valid_length(s):
    return len(s) >= 6

def is_valid_lowercase(s):
    return any(char.islower() for char in s)

def is_valid_uppercase(s):
    return any(char.isupper() for char in s)

def is_valid_numeric(s):
    return any(char.isdigit() for char in s)

def is_valid_special(s):
    return any(not char.isalnum() for char in s)

def is_valid_sum(s):
    return sum(int(char) for char in s if char.isdigit()) == 25

def is_valid_month(s):
    return any(month in s.lower() for month in ["january", "february", "march", "april", "may", "june", "july",
                                                "august", "september", "october", "november", "december"])

def is_valid_root(s):
    return any(np.sqrt(int(char)) > 2 for char in s if char.isdigit())

def is_valid_char(s):
    return '%' in s

def validate_password(input_str):
    if not is_valid_length(input_str):
        return "Must be at least 6 characters long."
    elif not is_valid_lowercase(input_str):
        return "Must contain at least one lowercase letter."
    elif not is_valid_uppercase(input_str):
        return "Must contain at least one uppercase letter."
    elif not is_valid_numeric(input_str):
        return "Must contain at least one number."
    elif not is_valid_special(input_str):
        return "Must contain at least one special character."
    elif not is_valid_sum(input_str):
        return "Digits must sum to 25."
    elif not is_valid_month(input_str):
        return "Must contain a month name."
    elif not is_valid_root(input_str):
        return "Must have a number whose square root is > 2."
    elif not is_valid_char(input_str):
        return "Must contain %."
    return None

# Simple HTML UI using template string
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Password Validator</title>
</head>
<body>
    <h1>Password Validator</h1>
    <form method="post">
        <label for="password">Enter password:</label>
        <input type="text" name="password" required>
        <button type="submit">Submit</button>
    </form>
    {% if result %}
        <p style="color: {{ 'green' if success else 'red' }}">{{ result }}</p>
    {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    success = False
    if request.method == "POST":
        password = request.form["password"]
        error = validate_password(password)
        if error:
            result = error
        else:
            result = "Password is valid. You win!"
            success = True
    return render_template_string(HTML_TEMPLATE, result=result, success=success)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
