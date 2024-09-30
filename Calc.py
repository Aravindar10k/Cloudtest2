from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    if request.method == "POST":
        num1 = float(request.form.get("num1", 0))
        num2 = float(request.form.get("num2", 0))
        operation = request.form.get("operation")

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"

    return render_template_string('''
        <form method="POST">
            <input type="number" name="num1" placeholder="Number 1" required>
            <input type="number" name="num2" placeholder="Number 2" required>
            <select name="operation">
                <option value="add">+</option>
                <option value="subtract">-</option>
                <option value="multiply">*</option>
                <option value="divide">/</option>
            </select>
            <button type="submit">Calculate</button>
        </form>
        <h2>Result: {{ result }}</h2>
    ''', result=result)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
