from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    category = None
    error = None

    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])

            if weight <= 0 or height <= 0:
                error = "Weight and height must be greater than zero."
            else:
                bmi = weight / (height ** 2)

                if bmi < 18.5:
                    category = "Underweight"
                elif bmi < 25:
                    category = "Normal Weight"
                elif bmi < 30:
                    category = "Overweight"
                else:
                    category = "Obese"

                bmi = round(bmi, 2)

        except ValueError:
            error = "Please enter valid numbers."

    return render_template(
        "index.html",
        bmi=bmi,
        category=category,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)