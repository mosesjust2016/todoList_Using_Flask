from typing_extensions import Required
from urllib import request
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

todos = {
    1: {"task" : "Task 1" , "summary": "write code using python"},
    2: {"task" : "Task 2" , "summary": "write code using python"},
    3: {"task" : "Task 3" , "summary": "write code using python"},
    4: {"task" : "Task 4" , "summary": "write code using python"},
    5: {"task" : "Task 5" , "summary": "write code using python"},
}

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type=str, help="Task is required", required=True)
task_post_args.add_argument("summary", type=str, help="Summary is required", required=True)

class ToDo(Resource):
    def get(self, todo_id):
        return todos[todo_id]

    def post(self, todo_id):
        args = task_post_args.parse_args()
        if todo_id in todos:
            abort(409, "Task already taken")
        todos[todo_id] = {"task" : args["task"], "summary" : args["summary"] }
        return todos

class ToDoList(Resource):
    def get(self):
        return todos

api.add_resource(ToDo, '/todos/<int:todo_id>')
api.add_resource(ToDoList, '/todos')

if __name__  == '__main__':
    app.run(debug=True)