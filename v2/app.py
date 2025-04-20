from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_cors import CORS
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from dotenv import load_dotenv
import os

# .env fayldan o‘qish
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'admin_login'

def send_message(name,mail,text):
    from telebot import TeleBot
    bot = TeleBot(token=os.getenv("BOT_TOKEN"))
    bot.send_message(chat_id=os.getenv("ADMIN_ID"),text=f"<b>Saytdan yangi xabar yo'llandi!!!</b>\n\nIsmi:{name}\nEmail:{mail}\nMatn:{text}",parse_mode="HTML")

# Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(200), nullable=True)
    feedback = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Project {self.name}>'

# User modeli (admin uchun)
class AdminUser(UserMixin):
    id = 1  # faqat bitta admin
    username = os.getenv("ADMIN_USERNAME")
    password = os.getenv("ADMIN_PASSWORD")

    def check_password(self, pw):
        return self.password == pw

@login_manager.user_loader
def load_user(user_id):
    if user_id == "1":
        return AdminUser()
    return None

# Custom AdminIndexView
class MyAdminIndexView(AdminIndexView):
    @expose('/')
    @login_required
    def index(self):
        return super(MyAdminIndexView, self).index()

# Login protected ModelView
class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('admin_login'))

# Admin login route
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        admin_user = AdminUser()
        if username == admin_user.username and admin_user.check_password(password):
            login_user(admin_user)
            return redirect('/admin')
    return render_template('admin_login.html')

# Admin logout
@app.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('admin_login'))

# HTML sahifalar (admin_login.html kerak)
@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

@app.route('/messages', methods=['POST'])
def receive_message():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    send_message(name,email,message)
    print(f"Xabar qabul qilindi: {name} | {email} | {message}")
    return jsonify({'status': 'success'}), 200

# Admin panel
admin = Admin(app, name='Project Admin Panel', template_mode='bootstrap3', index_view=MyAdminIndexView())
admin.add_view(MyModelView(Project, db.session))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False,host="0.0.0.0",port=1717)
