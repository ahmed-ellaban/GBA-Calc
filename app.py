from flask import Flask, render_template
from flask import request

app = Flask(__name__)
subjects = {"BS-103": "الجبر الخطي", "CS-103": "البرمجة الشيئية", "BS-102": "تراكيب محددة",
            "BS-104": "تطبيقات الاحتمالات والاحصاء في الحاسب", "IS201": "مقدمة في نظم المعلومات",
            "CS102": "البرمجة الهيكلية", "UNV-102": "لغة انجليزية", "UNV-103": "الكتابة العلمية والفنية"}


@app.route('/gpa_calculator', methods=['POST'])
def gpa_calculator():
    data = request.get_json()
    items = []
    second_gpa = 0
    first_gpa = float(data['first_semiterm_gpa'])
    for key, val in list(data.items())[:5]:
        mark = float(val)
        gpa = gpa_counter(mark)
        items.append({"name": subjects[key], "code": key, "mark": mark, "gpa": gpa})
        second_gpa += gpa

    if data.get('subject1') and not (data.get('subject2') or data.get('subject3')):
        # Replaced programming with two courses (Writing and English)
        mark = float(data['optional-CS102'])
        gpa = gpa_counter(mark)
        items.append({"name": subjects['CS102'], "code": 'CS102', "mark": mark, "gpa": gpa})
        second_gpa += gpa
        second_gpa /= 6
        total_gpa = ((first_gpa * 5 * 3) + (second_gpa * 6 * 3)) / 30
    elif data.get('subject1') and (data.get('subject2') or data.get('subject3')):
        # 2: Replaced programming with one course (3 hours)
        mark = float(data['optional-CS102'])
        gpa = gpa_counter(mark)
        items.append({"name": subjects['CS102'], "code": 'CS102', "mark": mark, "gpa": gpa})
        second_gpa += gpa
        second_gpa /= 6
        total_gpa = ((first_gpa * 5 * 3) + (second_gpa * 6 * 3)) / 27
    else:
        # 3: No changes
        second_gpa /= 5
        total_gpa = (first_gpa + second_gpa) / 2
    return {"items": items, "total_gpa": total_gpa, "second_gpa": second_gpa, "first_gpa": first_gpa}


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


if __name__ == '__main__':
    app.run(debug=True)
