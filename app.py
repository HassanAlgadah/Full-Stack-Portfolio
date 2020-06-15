import os
from flask import Flask, request, abort, jsonify, render_template, redirect
from auth import requires_auth
from models import setup_db, Project, Message

app = Flask(__name__)
setup_db(app)


@app.route('/')
def home():
    projects = Project.query.all()
    return render_template('index-1.html', data=projects)


@app.route('/admin')
def admin_page():
    projects = Project.query.all()
    return render_template('admin-page.html', data=projects)


@app.route('/projects')
def get_all_projects():
    try:
        projects = Project.query.all()
        data = []
        for project in projects:
            data.append({
                'id': project.id,
                'name': project.name,
                'image': project.image,
            })
        return jsonify({
            'success': True,
            'projects': data
        })
    except:
        abort(404)


@app.route('/projects/<int:id>')
def get_project(id):
    project = Project.query.get(id)
    if not project:
        abort(404)
    return jsonify(project.format())


@app.route('/messages')
@requires_auth('get:messages ')
def get_all_messages(payload):
    try:
        messages = Message.query.all()
        data = []
        for message in messages:
            data.append({
                'id': message.id,
                'name': message.name,
                'email': message.email,
                'number': message.number,
                'message': message.message
            })
        return jsonify({
            'success': True,
            'messages': data
        })
    except:
        abort(404)


@app.route('/projects', methods=['POST'])
@requires_auth('post:project')
def add_project(payload):
    try:
        data = request.get_json()
        project = Project(name=data.get('name'),
                          description=data.get('description'),
                          image=data.get('image'),
                          link=data.get('link'))
        project.insert()
        return render_template('index-1.html')
    except:
        abort(422)


@app.route('/messages', methods=['POST'])
def add_message():
    try:
        data = request.form
        if request.get_json():
            data = request.get_json()
        if data.get('name') is None:
            abort(400)
        message = Message(name=data.get('name'),
                          email=data.get('email'),
                          number=data.get('number'),
                          message=data.get('message'))
        message.insert()
        return redirect('/')
    except:
        abort(400)


@app.route('/projects/<id>', methods=['PATCH'])
@requires_auth('patch:project')
def update_project(payload, id):
    try:
        data = request.get_json()
        print(data)
        project = Project.query.get(id)
        project.name = data.get('name')
        project.description = data.get('description')
        project.image = data.get('image')
        project.link = data.get('link')
        project.update()
        return jsonify({
            'success': True,
            'project': project.format()
        })
    except:
        abort(400)


@app.route('/projects/<id>', methods=['DELETE'])
@requires_auth('delete:project')
def delete_project(payload, id):
    project = Project.query.get(id)
    if not project:
        abort(404)
    project.delete()
    if Project.query.get(id) is None:
        return jsonify({'success': True})
    else:
        abort(422)


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400


if __name__ == '__main__':
    app.run()
