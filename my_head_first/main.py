import mysql.connector
from flask import Flask, render_template, request, redirect, session
from checker import check_logged_in
from config import dbconfig, secret_key, admin_id, admin_phone

# create table restaurant ( resid int primary key auto_increment, restaurant varchar(20) not null, menu varchar(20) not null );
# create table history ( hisid int primary key auto_increment, date date, resid int, foreign key(resid) references restaurant (resid) );

app = Flask(__name__)
app.secret_key = secret_key

@app.route('/login', methods=['POST'])
def log_in():
    if request.form['admin'] == admin_id and request.form['phone'] == admin_phone:
        session['logged_in'] = True
        return redirect('/')
    else:
        return '입장 불가'

@app.route('/logout')
def log_out():
    session.pop('logged_in')
    return render_template('noPermission.html')

@app.route('/')
@check_logged_in
def index() -> 'html':
    _SQL = f'''select * from restaurant;'''
    restaurants = dbconnect(dbconfig, _SQL=_SQL)
    return render_template('menu.html',
                           restaurants=restaurants,
                           title='점심뭐먹지')

@app.route('/history')
@check_logged_in
def show_history() -> 'html':
    _SQL = f'''select history.hisid, history.date, restaurant.restaurant, restaurant.menu
    from history, restaurant
    where history.resid=restaurant.resid;'''
    restaurants = dbconnect(dbconfig, _SQL=_SQL)
    return render_template('history.html',
                           restaurants=restaurants,
                           title='전에 먹은 메뉴')

@app.route('/randompic')
@check_logged_in
def pick_random_restaurant() -> 'html':
    _SQL = f'''select * from restaurant order by rand() limit 1;'''
    picked_restaurant = dbconnect(dbconfig, _SQL=_SQL)
    return render_template('randompick.html',
                           picked_restaurant=picked_restaurant,
                           title='오늘 여기갈래?')

@app.route('/savepick', methods=['POST'])
@check_logged_in
def save_picked_restaurant() -> 'html':
    picked_restaurant_id = request.form['restaurant']
    _SQL = f"""insert into history (date, resid) values (curdate(), {picked_restaurant_id});"""
    dbconnect(dbconfig, _SQL=_SQL)

    _SQL = f'''select history.hisid, history.date, restaurant.restaurant, restaurant.menu
    from history, restaurant
    where history.resid=restaurant.resid;'''
    restaurants = dbconnect(dbconfig, _SQL=_SQL)
    picked_restaurant = restaurants[-1]
    return render_template('history.html',
                           restaurants=restaurants,
                           picked_restaurant=picked_restaurant,
                           title=f'오늘 {picked_restaurant[-2]} 가자♡')

@app.route('/append', methods=['POST'])
@check_logged_in
def append_restaurant() -> 'html':
    new_restaurant = request.form['restaurant']
    new_menu = request.form['menu']
    print(new_restaurant, new_menu)
    _SQL = f"""insert into restaurant (restaurant, menu) 
    values 
    ('{new_restaurant}', '{new_menu}');"""
    dbconnect(dbconfig, _SQL=_SQL)
    return redirect('/')

def dbconnect(dbconfig, _SQL):
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = _SQL
    cursor.execute(_SQL)
    try:
        data = cursor.fetchall()
        return data
    except Exception as err:
        print(err)
    finally:
        conn.commit()
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
