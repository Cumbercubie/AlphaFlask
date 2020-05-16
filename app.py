from flask import Flask, request, render_template
import os

app = Flask(__name__)
# auth = Blueprint('auth',__name__)

@app.route('/')
# @login_required
def index():    
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login.html')
# @app.route('/register',methods=['GET','POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data,email=form.email.data,password=form.password.data)
#         db.session.add(user)
#         db.session.commit()
#     return render_template('login.html')

# @app.route('/login',methods=['GET','POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = LoginForm()
#     if request.method=='POST':
#         if form.validate_on_submit():
#             user = User.query.filter_by(email=form.email.data).first()
#             if user and form.password.data==user.password:
#                 login_user(user)
#                 next_page = request.args.get('next')
#                 return redirect(next_page) if next_page else redirect(url_for('index'))
#             flash('Login Unsuccessfull. Please check username and password','red')
#                 # return redirect(url_for('index'))
#         else:
#             print(form.errors)
    
#     return render_template('properlogin.html',title="Login",form=form)

# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('login'))


# @app.route('userfunction/register')
# def getUserData():
#     return mongodb.querry.All() #json

@app.route('/round-2')
def round_2():
    from ExcelDriver import getQuestionsFromFile
    data = getQuestionsFromFile("static/questions.xlsx",'Sheet1')
    return render_template('round-2.html',datas=data)
if __name__ == '__main__':
    app.run(debug=True)