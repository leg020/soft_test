from flask import Flask, request, jsonify
import json
from fixture.main import Maining
from driver.convertor import Convertor
import threading
from driver.loging import Loging


server = Flask(__name__)
convertor = Convertor()
log = Loging()
main = Maining(log=log)


def start_testing(data):
    main.set_object_data(data)
    main.start_frontol()
    main.make_document()
    main.exit_frontol()


@server.route('/add_task', methods=['GET', 'POST'])
def read_json_file():
    #convertor = Convertor()
    file = request.get_json(silent=True)
    flag = convertor.convert_to_test_model(file)
    if flag == 0:
        thread = threading.Thread(target=start_testing, args=(convertor.data, ))
        thread.start()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    if flag == -1:
        err = convertor.err
        return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}

@server.route('/get_err', methods=['GET', 'POST'])
def get_err():
    return jsonify({'exception': convertor.err})

@server.route('/get_log', methods=['GET', 'POST'])
def get_log():
    return jsonify({'log_file': log.log_list})



if __name__ == '__main__':
    server.run(host="127.0.0.1", port="8000", debug=True)