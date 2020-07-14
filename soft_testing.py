from flask import Flask, request
import json
from fixture.main import Maining
from driver.convertor import Convertor
import threading


server = Flask(__name__)

def start_testing(data):
    main = Maining(data)
    main.start_frontol()
    main.make_document()
    main.exit_frontol()


@server.route('/add_task', methods=['GET', 'POST'])
def read_json_file():
    convertor = Convertor()
    file = request.get_json(silent=True)
    flag = convertor.convert_to_test_model(file)
    if flag == 0:
        thread = threading.Thread(target=start_testing, args=(convertor.data, ))
        thread.start()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    if flag == -1:
        err = convertor.err
        return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}

if __name__ == '__main__':
    server.run(host="127.0.0.1", port="8000", debug=True)