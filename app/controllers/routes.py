from app import app, db, login
from flask import render_template, redirect, url_for, request, jsonify, make_response
from flask_login import login_user, logout_user, login_required, current_user

from app.models.tables import Tasks, Users
from app.models.forms import LoginForm, RegisterForm, AddTaskForm

import json

@login.user_loader
def load_user(id):
    return Users.query.filter_by(id=id).first()

@app.route("/", methods=["GET", "POST"])
def login():
    title = 'Autenticação'

    form = LoginForm()
    if form.validate_on_submit():
        users_sql = Users.query.filter_by(username=form.username.data).first()
        if users_sql and users_sql.passwd == form.passwd.data:
            login_user(users_sql)
            return redirect(url_for('index'))
        else:
            return """
                    <html>
                    <script>
                        alert("Usuário ou senha, incorretos!");
                        window.location.href = "http://localhost:5000/";
                    </script>
                    </html>"""

    return render_template('login.html',
                            title=title,
                            form=form)

@app.route("/logout")
@login_required
def logout():

    logout_user()

    return """
            <html>
            <script>
                alert("Você saiu!");
                window.location.href = "http://localhost:5000/";
            </script>
            </html>"""

@app.route("/register", methods=["GET", "POST"])
def register():
    title = 'Cadastro'

    form = RegisterForm()
    if form.validate_on_submit():
        users_sql = Users.query.filter_by(username=form.username.data).all()
        if users_sql:
            return """
                    <html>
                    <script>
                        alert("Usuário já existente na base de dados!");
                        window.location.href = "http://localhost:5000/register";
                    </script>
                    </html>"""
        else:
            users_sql = Users(form.name.data, form.surname.data, form.username.data, form.passwd.data)
            db.session.add(users_sql)
            db.session.commit()
            return """
                    <html>
                    <script>
                        alert("Usuário criado com sucesso!");
                        window.location.href = "http://localhost:5000/";
                    </script>
                    </html>"""

    return render_template('register.html',
                            title=title,
                            form=form)
    
@app.route("/index", methods=["GET"])
@login_required
def index():
    title = 'Pagina Inicial'
    
    sql1 = Tasks.query.filter_by(users_id=current_user.id, status='0').all()
    sql2 = Tasks.query.filter_by(users_id=current_user.id, status='1').all()

    return render_template('index.html',
                            title=title,
                            sql1=sql1,
                            sql2=sql2)

@app.route("/add_task", methods=["GET", "POST"])
@login_required
def add_task():
    title = 'Criar Tarefa'

    form = AddTaskForm()
    if form.validate_on_submit():
        status_padrao = '0'
        user = current_user.id
        add_task_sql = Tasks(user, form.title.data, form.description.data, status_padrao)
        db.session.add(add_task_sql)
        db.session.commit()
        return """
                <html>
                <script>
                    alert("Tarefa criada com sucesso!");
                    window.close();
                </script>
                </html>"""

    return render_template('add_task.html',
                            title=title,
                            form=form)

@app.route("/details/<val_task>", methods=["GET"])
@login_required
def details(val_task):
    title = 'Detalhes Tarefa'

    if val_task:
        task_sql = Tasks.query.filter_by(id=val_task).first()

    return render_template('details.html',
                            title=title,
                            task_sql=task_sql)

@app.route("/update_task/<int:concluir>")
@app.route("/update_task/<int:deletar>")
def update_task(concluir=None, deletar=None):

    if concluir:
        sql = Tasks.query.filter_by(id=concluir).first()
        sql.status = '0'
        db.session.commit()
    
    if deletar:
        sql = Tasks.query.filter_by(id=deletar).first()
        sql.status = '1'
        db.session.commit()

    return None
