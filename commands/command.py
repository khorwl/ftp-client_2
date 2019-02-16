class ICommand:
    def __init__(self, s, encoding, change_some_code):
        self.conn = s
        self.encoding = encoding
        self.change_some_code = change_some_code

    def execute_command(self, args):
        pass
