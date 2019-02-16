from commands.command import ICommand
from constants import end_msg
from tools.response_reader import read_response


class Quit(ICommand):
    def __init__(self, s, encoding, change_some_code):
        super().__init__(s, encoding, change_some_code)

    def execute_command(self, args):
        self.conn.sendall(("quit" + end_msg).encode(self.encoding))
        print(read_response(self.conn, self.encoding, self.change_some_code))
