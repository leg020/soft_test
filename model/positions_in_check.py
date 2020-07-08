

class PositionsInCheck:

    def __init__(self, place_in_list=None, cout=None, need_mark=False, mark=None):
        self.place_in_list = place_in_list
        self.cout = cout
        self.need_mark = need_mark
        self.mark = mark

class Checks:

    def __init__(self, ckeck_number=None, positions=None, type_close=None, sale=False):
        self.ckeck_number = ckeck_number
        self.positions = positions
        self.type_close = type_close
        self.sale = sale