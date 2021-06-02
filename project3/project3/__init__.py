from flask import Flask,render_template,request,redirect
from project3.models import db,MenuModel
from werkzeug.exceptions import abort
from flask_migrate import Migrate

app = Flask(__name__)
migrate = Migrate(app, db)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()
 
@app.route('/')
def index():
    return render_template('index.html')
 
 
@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        menu_id = request.form['menu_id']
        menu_name = request.form['menu_name']
        menu_price = request.form['menu_price']
        menu_type = request.form['menu_type']
        menu = MenuModel(menu_id=menu_id, menu_name=menu_name, menu_price=menu_price, menu_type=menu_type)
        db.session.add(menu)
        db.session.commit()
        return redirect('/data/create')
 
 
@app.route('/data')
def RetrieveList():
    menues = MenuModel.query.all()
    return render_template('datalist.html',menues = menues)
 
 
@app.route('/data/<int:id>')
def RetrieveMenu(id):
    menu = MenuModel.query.filter_by(menu_id=id).first()
    if menu:
        return render_template('data.html', menu=menu)
    return f"요청한 메뉴 ID # {id} 는 등록되지 않은 메뉴입니다."
 
 
@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    menu = MenuModel.query.filter_by(menu_id=id).first()
    if request.method == 'POST':
        if menu:
            db.session.delete(menu)
            db.session.commit()
            menu_name = request.form['menu_name']
            menu_price = request.form['menu_price']
            menu_type = request.form['menu_type']
            menu = MenuModel(menu_id=id, menu_name=menu_name, menu_price=menu_price, menu_type=menu_type)
            db.session.add(menu)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"요청한 메뉴 ID # {id} 는 등록되지 않은 메뉴입니다."
 
    return render_template('update.html', menu=menu)
 
 
@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    menu = MenuModel.query.filter_by(menu_id=id).first()
    if request.method == 'POST':
        if menu:
            db.session.delete(menu)
            db.session.commit()
            return redirect('/data')
        abort(404)
 
    return render_template('delete.html')


if __name__ == "__main__":
#   app = create_app()
  app.run(debug=True)