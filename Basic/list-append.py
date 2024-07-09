health_check = [{'name': 'battery_capacity', 'label': 'Battery Charge Capacity', 'group': 'Battery', 'healthcheck_parameter_id': 1, 'value': 0, 'is_failed': False, 'is_actual': False, 'id_value': 154157, 'updated_at': '2023-06-09T07:58:42'}, {'name': 'battery_voltage', 'label': 'Battery Voltage', 'group': 'Battery', 'healthcheck_parameter_id': 2, 'value': 0, 'is_failed': False, 'is_actual': False, 'id_value': 154155, 'updated_at': '2023-06-09T07:58:42'}, {'name': 'battery_current', 'label': 'Charge Current', 'group': 'Battery', 'healthcheck_parameter_id': 3, 'value': 0, 'is_failed': False, 'is_actual': False, 'id_value': 154158, 'updated_at': '2023-06-09T07:58:42'}, {'name': 'external_voltage', 'label': 'External Voltage', 'group': 'Power - External', 'healthcheck_parameter_id': 4, 'value': 193, 'is_failed': False, 'is_actual': True, 'id_value': 154154, 'updated_at': '2023-06-09T07:58:42'}, {'name': 'sieve_life', 'label': 'Column Life', 'group': None, 'healthcheck_parameter_id': 5, 'value': 0, 'is_failed': False, 'is_actual': False, 'id_value': 154159, 'updated_at': '2023-06-09T07:58:42'}, {'name': 'oxygen_delivery', 'label': 'Oxygen Delivery', 'group': None, 'healthcheck_parameter_id': 6, 'value': 0, 'is_failed': False, 'is_actual': False, 'id_value': 154156, 'updated_at': '2023-06-09T07:58:42'}, {'name': 'oxygen_purity', 'label': 'Oxygen Purity', 'group': None, 'healthcheck_parameter_id': 7, 'value': 0, 'is_failed': False, 'is_actual': False, 'id_value': 154160, 'updated_at': '2023-06-09T07:58:42'}]

print(type(health_check))
print(health_check)

hc_disc1 = {"name": "power",
                "label": "Power",
                "group": "Battery",
                "healthcheck_parameter_id": 11,
                "value": "0",
                "is_failed": False,
                "is_actual": True,
                "id_value": 154210,
                "is_param_exists": "True",
                "updated_at": "2023-09-12T17:52:56+00:00"
            }

print(type(hc_disc1))
print(hc_disc1)

newlist = [{
                "name": "battery_capacity",
                "label": "Full Charge Capacity",
                "group": "Battery",
                "healthcheck_parameter_id": 1,
                "value": "0",
                "is_failed": False,
                "is_actual": False,
                "id_value": 154157,
                "is_param_exists": "True",
                "updated_at": "2023-06-09T07:58:42+00:00"
            }]
newlist.append(hc_disc1)
print('newlist ** ',newlist)
print(type(newlist))

health_check.append(hc_disc1)
print(health_check)
