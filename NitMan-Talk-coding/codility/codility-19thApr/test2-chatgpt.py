from flask import Flask, request, jsonify

app = Flask(__name__)

# Mocked-up database
def get_users():
    return [
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

@app.route('/users', methods=['GET'])
def get_users_by_name():
    users = get_users()
    name = request.args.get('name')

    if name:
        filtered_users = [user for user in users if user['name'] == name]
        return jsonify(filtered_users), 200
    else:
        return jsonify(users), 200

if __name__ == '__main__':
    app.run(debug=True)
