Необходимые настройки:

Закрытие чека должно вызываться комбинацией - 'Ctrl + F2'
Начисление скидки 'Ctrl + 5'
Отмена начисленной скидки 'Ctrl + 6'
Заранее настроенный скаанер в настройках оборудования, работа осуществляется через com2com

Настройка json

Общие:
have_cassa - Наличие кассы необходимо для разработки скрипта, в остальных случаях требуется подключение, значение True
target - место откуда запускать фронтол, обратите внимание на двойные слэши
scaner_port - порт для подключения сканера работа осуществляется через com2com
scaner_boundrate - скорость подключения сканера, 9600 - приемлемо

Настройки чека:
check_number - номер чека, исчисление внутри скрипта необязательно
document_type - тип документа
    registration - формирование чеков
    report - формирование отчетов
report_type - тип отчета
    1 - Открытие смены
    7 - Закрытие смены
    в зависимости от порядка в списке, возможно и другие работают
sale - добавить скидку на чек True, False
type_close - тип оплаты чека:
    1 - наличными
    2 - безналичными
    3 - предоплатой (авансом)
    4 - постоплатой (кредитом)
check_type - Тип открываемого чека
    None - настройка игнорируется
    1 - Продажа
    2 - Возврат продажи
        Для возврата продажи требуется указать тип возвращаемого документа
        1 - пустой
        2 - на основании
    3 - Внесение
    4 - Выплата
    12 - Расход
    13 - Возврат расхода

Настройки позиции:

place_in_list - номер позиции в списке, которую требуется добавить, ВНИМАНИЕ!!! порядковый номер в настройках товаров и в
режиме регистрации может отличаться, интересует пофакту в режиме регистрации
cout - количество товара в позиции, ВНИМАНИЕ!!! не рекомендуется для товара с маркой вводить значение более 1.
mark - марка для сканирования в позицию
need_mark - необходимость введения марки, работает в комбинации с -> mark <-
1) Если need_mark = False, то позиция считается не маркированной и марка игнорируется
2) Если need_mark = True, то позиция считается маркированной и проверяется марка
    если mark = None, то считается, что позиция маркированная, но без штрихкода маркировки
    если mark имеет значение, значит это значение будет просканировано, как марка и добавиться в позицию


Пример запроса:

res = requests.post('http://localhost:8000/add_task', json={
  "py/object": "model.data.Data",
  "settings": {
    "py/object": "model.settings.Settings",
    "target": "C:\\Program Files (x86)\\ATOL\\Frontol6\\BIN\\Frontol.exe",
    "scaner_port": "COM258",
    "scaner_boundrate": 9600,
    "have_cassa": True
  },
  "data": [
    {
      "py/object": "model.positions_in_check.Checks",
      "check_number": 1,
      "document_type": "registration",
      "report_type": 1,
      "check_type": None,
      "help_setting": None,
      "positions": [
        {
          "py/object": "model.positions_in_check.PositionsInCheck",
          "place_in_list": 1,
          "cout": 1,
          "need_mark": False,
          "mark": None
        },
        {
          "py/object": "model.positions_in_check.PositionsInCheck",
          "place_in_list": 1,
          "cout": 1,
          "need_mark": False,
          "mark": None
        }
      ],
      "type_close": 1,
      "sale": False
    },
    {
      "py/object": "model.positions_in_check.Checks",
      "check_number": 1,
      "document_type": "report",
      "report_type": 7,
      "check_type": None,
      "help_setting": None,
      "positions": [
        {
          "py/object": "model.positions_in_check.PositionsInCheck",
          "place_in_list": 1,
          "cout": 1,
          "need_mark": False,
          "mark": None
        },
        {
          "py/object": "model.positions_in_check.PositionsInCheck",
          "place_in_list": 1,
          "cout": 1,
          "need_mark": False,
          "mark": None
        },
      ],
      "type_close": 1,
      "sale": False
    }
  ]
})

Получить лог

res = requests.get('http://localhost:8000/get_log')

Получить информацию об ошибке

res = requests.get('http://localhost:8000/get_err')



