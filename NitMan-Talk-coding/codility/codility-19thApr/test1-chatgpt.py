from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route('/service/configuration/<env>/<service_name>', methods=['GET'])
def get_configuration(env, service_name):
    config = app.config['db']
    if env in config and service_name in config[env]:
        yaml_data = yaml.dump(config[env][service_name])
        return jsonify(yaml_data), 200
    else:
        return "Configuration not found", 404

@app.route('/service/configuration/<env>/<service_name>', methods=['POST'])
def add_configuration(env, service_name):
    try:
        data = request.json['data']
        yaml_data = yaml.safe_load(data)
        if not yaml_data:
            return "Incorrect YAML format", 400
        
        if 'db' not in app.config:
            app.config['db'] = {}
        
        if env not in app.config['db']:
            app.config['db'][env] = {}
        
        app.config['db'][env][service_name] = yaml_data
        
        return "Configuration added successfully", 200
    except:
        return "Incorrect request format", 400

@app.route('/service/configuration/<env>/<service_name>', methods=['DELETE'])
def delete_configuration(env, service_name):
    config = app.config['db']
    if env in config and service_name in config[env]:
        del config[env][service_name]
        return "Configuration deleted successfully", 200
    else:
        return "Configuration not found", 404

if __name__ == '__main__':
    app.run(debug=True)
