from flask import Flask, request
import json
from fixture.main import Maining
from driver.convertor import Convertor


server = Flask(__name__)


@server.route('/add_task', methods=['GET', 'POST'])
def read_json_file():
    convertor = Convertor()
    file = request.get_json(silent=True)
    flag = convertor.convert_to_test_model(file)
    if flag == 0:
        main = Maining(convertor.data)
        main.start_frontol()
        main.make_document()
        main.exit_frontol()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    if flag == -1:
        return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}

if __name__ == '__main__':
    server.run(host="127.0.0.1", port="8000", debug=True)