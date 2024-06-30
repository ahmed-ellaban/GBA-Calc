from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/gpa_calculator', methods=['POST'])
def gpa_calculator():
    data = request.get_json()
    items = []
    gpa = 0
    for i in range(1, 7):
        mark = int(request.args.get(f"grade{i}"))
        grade = gpa_counter(mark)
        items.append({"grade": grade})
        gpa += grade
    gpa /= 7
    return gpa


@app.route('/')
def main_page():  # put application's code here
    return render_template('homepage.html')


def gpa_counter(mark):
    if mark >= 96:
        return 4
    elif 96 > mark >= 92:
        return 3.7
    elif 92 > mark >= 88:
        return 3.4
    elif 88 > mark >= 84:
        return 3.2
    elif 84 > mark >= 80:
        return 3
    elif 80 > mark >= 76:
        return 2.8
    elif 76 > mark >= 72:
        return 2.6
    elif 72 > mark >= 68:
        return 2.4
    elif 68 > mark >= 64:
        return 2.2
    elif 64 > mark >= 60:
        return 2
    elif 60 > mark >= 55:
        return 1.5
    elif 55 > mark >= 50:
        return 1
    else:
        return 0


def total_gpa_calculator(gpa_1, gpa_2, option):
    if option == 1:
        total_gpa = ((gpa_1 * 5 * 3) + (gpa_2 * 6 * 3)) / 30
    elif option == 2:
        total_gpa = ((gpa_1 * 5 * 3) + (gpa_2 * 6 * 3)) / 27
    else:
        total_gpa = (gpa_1 + gpa_2) / 2
    return total_gpa


if __name__ == '__main__':
    app.run(debug=True)
