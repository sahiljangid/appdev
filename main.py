from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty


x = [1, 2, 3, 4, 5]
y = [12, 19, 29, 37, 45]

def sumx():
    return sum(x)

def sumy():
    return sum(y)

def sumxy():
    sm = 0
    for i in range(len(x)):
        mul = x[i]*y[i]
        sm += mul
    return sm

def sumxsq():
    sm = 0
    for i in x:
        sm += i*i
    return sm

def sqsumx():
    print(sumx()*sumx())

def slope():
    n = len(x)

    denominator = (n * sumxsq()) - sumx() ** 2

    if denominator == 0:
        raise ValueError("Denominator is zero, unable to calculate slope.")

    a = ((n * sumxy()) - (sumx() * sumy())) / denominator
    return a

def intercept():
    n = len(x)
    b = (sumy()-slope()*sumx())/n
    return b

kv = """
Screen:
    in_class: text
    MDLabel:
        text: 'Simple Linear Regression'
        size_hint: 1, 0.2
        pos_hint: {'center_x': 0.9, 'center_y': 0.9}
    
    MDRectangleFlatButton:
        text: 'See your data'
        pos_hint: {'center_x': 0.5, 'center_y': 0.85}
        on_press:
            app.data()
    
    MDLabel:
        text: ''
        id: shw
        pos_hint: {'center_x': 0.95, 'center_y': 0.7}
    
    MDTextField:
        id: text
        hint_text: 'Enter value of X'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint_x: 0.3
        required: True

    MDLabel:
        text: ''
        id: show
        pos_hint: {'center_x': 0.8, 'center_y': 0.3}

    MDRectangleFlatButton:
        text: 'Submit'
        pos_hint: {'center_x': 0.5, 'center_y': 0.15}
        on_press:
            app.predict()
    
"""


class Main(MDApp):
    in_class = ObjectProperty(None)

    def build(self):
        return Builder.load_string(kv)

    def predict(self):
        self.root.ids.show.text = ""

        try:
            a = float(self.root.in_class.text)
        except ValueError:
            label = self.root.ids.show
            label.text = "Invalid input. Please enter a valid number."
            return

        res = (slope() * a) + intercept()
        res = round(res, 2)
        label = self.root.ids.show
        label.text = f"The predicted Y value for X = {a} is {res}"

    def data(self):
        data_label = text= "Your data is:\nX               Y\n" + "\n".join([f"{x[i]}               {y[i]}" for i in range(len(x))])
        label = self.root.ids.shw
        label.text = data_label




Main().run()