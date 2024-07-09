'''
The objective of this task is to write an API with one GET endpoint.

Requirements
You are required to write an API Python and the Flask library that will contain the following endpoint:
1. GET /users
    - endpoint should return the status code 200 on a successful request;
    - endpoint should return the data taken from the mocked-up databased using the provided helper function get_users. This function returns a list of dictionaries containing id (number), name (sting) and role (string). An example list might appear as follows:
    [
        {
            "id": 1,
            "name": "John",
            "role": "admin"
        },
        {
            "id": 2,
            "name": "Juan",
            "role": "developer"
        }
    ]
    - endpoint should accept a query parameter name which will contain a string;
    - when parameter name is provided. all users whose name property is equal to the name query parameter must be returned (there may be more than one match). If no users with the given name are found, an empty list must be returned.

Hints
1. Your solution will be evaluted based on its correctness; performance and coding stylr will not be assessed.
2. you can assume that the id, name and role properties of the users returned form the database are all present and of the correct types. You do not have to verify them.
3. You do not have to take care of unsuccessful request; the reponse is always successful and the status ode must equal 200.

Examples
1. Given a database helper method returning the following data:
    [
        {
            "id": 1,
            "name": "John",
            "role": "admin"
        },
        {
            "id": 2,
            "name": "Juan",
            "role": "developer"
        }
    ]
2. A request to GET /users should retrun 200 and the following payload:
    [
        {
            "id": 1,
            "name": "John",
            "role": "admin"
        },
        {
            "id": 2,
            "name": "Juan",
            "role": "developer"
        }
    ]
3. A request GET /users?name=John should return 200 and the following payload:
    [
        {
            "id": 1,
            "name": "John",
            "role": "admin"
        }
    ]
4. A request GET /users?name=Jane should return 200 and the following payload:
    []
'''
from flask import Flask, jsonify, request
from db_users import get_users

app = Flask(__name__)

@app.route('/users')
def index():
    data = get_users()
    return data

@app.route('/user?name=<string:name>?id=<int:id>')
def get_user_by_nameid():
    args = request.args
    name = args.get("name", default="", type=str)
    id = args.get("id", default=0, type=int)

    data = get_users(name,id)
    print('data: ', data)
    response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')
    return 'Getting user data successfully: ' + response


if __name__ == '__main__':
    app.run()
