from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

data_object = [
    {"id": 1, "data": 8},
    {"id": 2, "data": 9}
]


@app.route('/math/api/v1.0/data', methods=['GET'])
def get_datas():
    return jsonify({'data': data_object})


@app.route('/math/api/v1.0/data/<int:data_id>', methods=['GET'])
def get_data(data_id):
    data = [data for data in data_object if data['id'] == data_id]
    if len(data) == 0:
        abort(404)
    return jsonify({'data': data[0]})


@app.route('/math/api/v1.0/data', methods=['POST'])
def create_task():
    print(request.json)
    if not request.json or not 'data' in request.json:
        abort(400)
    data = {
        'id': data_object[-1]['id'] + 1,
        'data': request.json['data']
    }
    data_object.append(data)
    return jsonify({'data': data}), 201


@app.route('/math/api/v1.0/data/<int:data_id>', methods=['PUT'])
def update_task(data_id):
    print(request.json)
    data = [data for data in data_object if data['id'] == data_id]
    if len(data) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if not 'data' in request.json:
        abort(400)
    data[0]['data'] = request.json.get('data', data[0]['data'])
    return jsonify({'data': data[0]})


@app.route('/math/api/v1.0/data/<int:data_id>', methods=['DELETE'])
def delete_task(data_id):
    data = [data for data in data_object if data['id'] == data_id]
    if len(data) == 0:
        abort(404)
    data_object.remove(data[0])
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run()