from flask.globals import request
from flask.json import jsonify
from app import app


# it should be {'id': 'address'}
spisochek = {'recordings': []}
last_id = 0

def stop_rec_by_id(id):
    global spisochek
    # blablabla
    # work...
    address = spisochek['recordings'].pop(id)

    # address of the video
    return 'https://www.youtube.com/watch?v=-mZICVd-Oek'

@app.route('/')
@app.route('/index')
def index():
    return jsonify(spisochek)

@app.route('/rec/start', methods=['POST'])
def start_rec():
    global last_id, spisochek

    last_id += 1
    id = last_id
    id_address_pair = {id: request.get_json()['address']}

    spisochek['recordings'].append(id_address_pair)

    return {'id': id}

@app.route('/rec/stop', methods=['POST'])
def stop_rec():
    global last_id, spisochek

    required_id = request.get_json()['id']
    video_address = stop_rec_by_id(required_id)

    return {'video_address': video_address}
