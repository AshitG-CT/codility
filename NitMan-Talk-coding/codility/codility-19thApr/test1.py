'''create a configuration server using Flask
Overview
Imagine that you have serval services in your system. Most probably, each one of them has its own configuration, as well as there beging multiple envionment (like dev, prod) and serveal developers.
you need to create a server to be able to view, add and delete configuration.

Form the storage side, all the data form GET, POST, requests should be storafe in the Flask application config: app.config["db"].

To parase YAMS data - you can use PyYAML module (already import in your initial solution).

Operations:
1. get a configuration
    GET /service/configuration/<env>/<service_name>
an existing configuration
    - <env> - Environment (dev, prod etc)
    - <service_name> - service Name
Response:
    200 - successfully return a proper configuration in YAML format
    404 - configuration not found

2. add a configuration
    POST /service/configuration/<env>/<service_name>
add a new configuration
    - <env> - Environment (dev, prod etc)
    - <service_name> - service Name
Request in JSON format:
    - data - string that contains correct YAML - formatted configuration; otherwise, if it is not correct, return 400 error code
Response:
    200 - successfully added new configuration
    404 - wrong YAML format

3. delete a configuration
    DELETE /service/configuration/<env>/<service_name>
deletes an existing configuration
    - <env> - Environment (dev, prod etc)
    - <service_name> - service name
Response:
    200 - successfully delete a configuration by give path
    404 - configuration not found

Example
Calling: POST /service/configuration/dev/agent with the following request data: {"data": "redis:\nhosh:dev.agent.website.com"}
will cause the following YAML to be added to the configuration:

redis:
    host: dev.agent.website.com

Calling: GET /service/configuration/dev/agent will return the following configuration:
redis:
    host: dev.agent.website.com

Calling: DELETE /service/configuration/dev/agent will cause the configuration for agent service and dev environment to be deleted.
    
'''
from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)
app.config["db"] = dict()

## Snehal's answer
@app.route('/service/configuration/<env>/<service_name>', methods=['GET'])
def get_configuration(env, service_name):
    # config = app.config['db']
    # if env in config and service_name in config[env]:
    config_key = f"{env}/{service_name}"
    if config_key in app.config["db"]:
        return yaml.dump(app.config["db"][config_key], default_flow_style=False), 200
    else:
        return "Configuration not found", 404

@app.route("/service/configuration/<env>/<service_name>", methods=["POST"])
def add_service_configuration(env, service_name):
    config_key = f"{env}/{service_name}"
    req_data = request.get_json()
    if req_data and "data" in req_data:
        try:
            new_config = yaml.safe_load(req_data["data"])
            app.config["db"][config_key] = new_config
            return "Configuration added successfully", 200
        except yaml.YAMLError:
            return "Invalid YAML format", 400
    else:
        return "Invalid request data", 400

@app.route("/service/configuration/<string:env>/<string:service_name>",
           methods=["DELETE"])
def delete_service_configuration(env, service_name):
    config_key = f"{env}.{service_name}"
    if config_key in app.config["db"]:
        del app.config["db"][config_key]
        return "Configuration deleted successfully", 200
    else:
        return "Configuration not found", 404


if __name__ == "__main__":
    app.run(debug=True)
