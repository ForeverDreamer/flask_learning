from flask import Flask, request
from flask_restx import Resource, Api, reqparse, fields

app = Flask(__name__)
api = Api(app)


# @api.route('/hello')
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}


todos = {}


@api.route('/todo<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


@api.route('/t1')
class Todo1(Resource):
    def get(self):
        # Default to 200 OK
        return {'task': 'Hello world'}


@api.route('/t2')
class Todo2(Resource):
    def get(self):
        # Set the response code to 201
        return {'task': 'Hello world'}, 201


@api.route('/t3')
class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}


@api.route('/hello', '/world')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


@api.route('/rp')
class ReqParse(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('rate', type=int, help='Rate to charge for this resource')
        args = parser.parse_args(strict=True)
        return args


model = api.model('Model', {
    'task': fields.String,
    'uri': fields.Url('todo')
})


class TodoDao:
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'


@api.route('/todo')
class Todo(Resource):
    @api.marshal_with(model)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')


if __name__ == '__main__':
    app.run(debug=True)
