from flask import Flask, render_template
from excel import ExcelFile

excel_object = ExcelFile("cups.xlsx")
app = Flask(__name__)
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contacts/")
def contacts():
    a = "Номер телефона: +996707202228"
    b = "Gmail: kruwki@gmail.com"
    return render_template("contacts_list.html", a=a, b=b)

@app.route("/about/")
def about():
    return render_template("about.html")

# @app.route("/cups/")
# def cups_list():
#     cup_names = excel_object.get_cup_names()
#     # <br> - перенос строки
#     response_str = cup_names.replace("\n", "<br>")
#     return response_str # тип - строка

@app.route("/cups/")
def cups_list():
    cup_names = excel_object.get_cup_names()
    cup_names = cup_names.split("\n")
    return render_template("cup_list.html", cup_names=cup_names)

@app.route("/cup/<number>")
def cup_detail(number):
    cup_info, cup_info_2, img_path = excel_object.get_cup_info(number)
    cup_info = cup_info
    cup_info_2 = cup_info_2
    return render_template("cup_detail.html", cup_info=cup_info, cup_info_2=cup_info_2, img_path=img_path)

app.run()
