pizzas = [
  {
    "name":"capriciossa pizza",
    "img": 'caprisiossa.png',
    "description":"Saus tomat, mozarella, basil leave, zaitun oil, sea salt"
  },
  {
    "name":"Chicken tikka pizzza",
    "img":'Chicken_Tikka_pizza.png',
    "description":"Saus tomat, chicken tikka, mozarella, red onion slice, cilantro, jalapeno, cheddar, yogurt drizzle"
  },
  {
    "name":"margherita pizza",
    "img":'magherita.png',
    "description":"Saus tomat, mozarella, basil leave, zaitun oil, sea salt"
  },
  {
    "name":"chicken pizza",
    "img":'chicken pizza.png',
    "description":"Daging ayam, saus tomat, mozarella"
  },
  {
    "name":"BBQ chicken pizza",
    "img":'bbq chicken pizza.png',
    "description":"Saus BBQ, grilled chicken mozarella, smoked gouda, red onion slice, cilantro"
  },
  {
    "name":"Hot honey pepperoni pizza",
    "img":'hot honey.png',
    "description":"Saus tomat, mozarella Pepperoni, hot honey, oregano pamersan"
  },
  {
    "name":"Neopolitan pizza",
    "img":'NEOPOLITAN.png',
    "description":"Saus tomat, mozarella basil leave, zaitun oil, pamersan, sea salt"
  },
  {
    "name":"marinara pizza",
    "img":'MARINARA.png',
    "description":"Saus tomat,  onion slice, oregano, zaitun oil, sea salt"
  },
  {
    "name":"supreme pizza",
    "img":'SUPREME.png',
    "description":"pepperoni, italian sausage, droun beef, Ham, mushroom, onions, mozarella, black olives"
  },
  {
    "name":"Hawaii pizza",
    "img":'HAWAIIAN PIZZA.png',
    "description":"pineapple, Ham, mozarella,  saus tomat, crispy bacon, red onion, jalapeno"
  },
  {
    "name":"Campesana pizza",
    "img":'campesana.png',
    "description":"Sweet corn, beef, red paprica, onions, black zaitun, mozarella, saus tomat"
  },
  {
    "name":"Vegie delight pizza",
    "img":'VEGIE DELIGH4.png',
    "description":"Bell peppers, red onions, mushrooms, black olives, cherry tomatoes, spinach, mozarella, tomato sauce"
  },
  {
    "name":"Chicken supreme pizza",
    "img":'SUPREME (2).png',
    "description":"Bell peppers, Grilled chicken, paprica slice, mushroom, mozarella, black zaitun, saus tomat"
  },
  {
    "name":"Mushroom & onions pizza",
    "img":'mushroom pizza.png',
    "description":"Mushroom portobello, red onions, mozarella, saus tomat"
  },
  {
    "name":"Pepperoni pizza",
    "img":'pepperoni pizza.png',
    "description":"Saus tomat, mozarellla, pepperoni, oregano"
  },
  {
    "name":"Hawaiian Pepperoni pizza",
    "img":'PINEAPPLE.png',
    "description":"pepperoni, pineapple, mozarella, saus tomat, oregano, zaitun oil"
  }
]
beverages = [
  {
    "name":"Fanta orange",
    "img":"fanta oren.png",
    "description":"Fanta orange 1m"
  },
  {
    "name":"Fanta strawberry",
    "img":"fanta strw.png",
    "description":"Fanta strawberry 1m"
  },
  {
    "name":"Teh botol sosro",
    "img":"sosro.png",
    "description":"Teh botol sosro"
  },
  {
    "name":"Vanilla Milksahe",
    "img":"VANILLA.png",
    "description":"vanilla milkshake"
  },
  {
    "name":"chocolate milksahek",
    "img":"chocolate milkshake.png",
    "description":"chocolate milksahek"
  },
  {
    "name":"Strawberry milkshake",
    "img":"starwberry milk sahke.png",
    "description":"Strawberry milkshake"
  },
  {
    "name":"Aqua Water",
    "img":"aqua.png",
    "description":"Aqua Water 1m"
  },
  {
    "name":"Coca cila",
    "img":"cola-removebg-preview.png",
    "description":"Coca cila"
  },
  {
    "name":"Sprite",
    "img":"SPRITE.png",
    "description":"Sprite"
  },
  {
    "name":"Teh pucuk harum",
    "img":"PUCUK HARUM.png",
    "description":"Teh pucuk harum"
  }
 ]
desserts = [
  {
    "name":"Cookies",
    "img":"cookies.png",
    "description":"8 mangkuk cookies renyah"
  },
  {
    "name":"Tiramisu",
    "img":"Tiramisu-removebg-preview.png",
    "description":"Tiramisu manis manis dadakan"
  },
  {
    "name":" Brownies",
    "img":"brownies.png",
    "description":"Brownies  semanis coklat"
  },
  {
    "name":"Panna Cotta",
    "img":"PANNA COTTA.png",
    "description":"Pudding kentak, manis khas italy"
  },
  {
    "name":"Chocolate kit kat",
    "img":"kit kat.png",
    "description":"Coklat kit kat"
  },
  {
    "name":"Churros",
    "img":"churros.png",
    "description":"8 mangkuk churros dengan selai coklat"
  },
  {
    "name":"Ice cream",
    "img":"ice cream.png",
    "description":"3 scop ice cream menyegarkan"
  }
]

users = {"admin": "1234", "user": "abcd"}

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
    
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@app.route("/")
def index():
    return redirect(url_for('register'))

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(password)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            return redirect(url_for('dash'))  # use url_for for consistency
        else:
            return "Invalid credentials", 401
    return render_template('login.html')

# @app.route('/auth', methods=['POST'])
# def auth():
#     username = request.form['username']
#     password = request.form['password']
#     if username in users and users[username] == password:
#         return redirect(url_for('index'))  # Arahkan ke index.html
#     else:
#         return "Invalid credentials. Please try again."

@app.route("/dash")
def dash():
    return render_template("index.html", pizzas=pizzas, beverages=beverages, desserts=desserts)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/order")
def order():
    return render_template("order.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
