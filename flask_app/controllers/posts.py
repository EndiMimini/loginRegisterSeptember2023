from flask_app import app

from flask import render_template, redirect, session, request, flash

from flask_app.models.user import User
from flask_app.models.post import Post



@app.route('/add/post')
def addPost():
    if 'user_id' not in session:
        return redirect('/')
    loggedUserData = {
        'user_id': session['user_id']
    }
    return render_template('addPost.html',loggedUser = User.get_user_by_id(loggedUserData))


@app.route('/create/post', methods = ['POST'])
def createPost():
    if 'user_id' not in session:
        return redirect('/')
    if not Post.validate_post(request.form):
        return redirect(request.referrer)
    data = {
        'title': request.form['title'],
        'content': request.form['content'],
        'user_id': session['user_id']
    }   
    Post.create_post(data)
    return redirect('/')

@app.route('/delete/post/<int:id>')
def deletePost(id):
    if 'user_id' not in session:
        return redirect('/')
    
    data = {
        'user_id': session['user_id'],
        'post_id': id
    }
    loggedUser = User.get_user_by_id(data)
    post = Post.get_post_by_id(data)
    if loggedUser['id'] == post['user_id']:
        Post.delete_post(data)
        return redirect(request.referrer)
    return redirect(request.referrer)