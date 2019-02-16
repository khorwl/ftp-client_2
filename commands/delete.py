from commands.command import ICommand
from constants import end_msg
from tools.helper import send_command
from tools.response_reader import read_response


class Delete(ICommand):
    def __init__(self, s, encoding, change_some_code):
        super().__init__(s, encoding, change_some_code)

    def execute_command(self, args):
        file_name = " ".join(args)

        send_command(self.conn, "dele {}".format(file_name) + end_msg, self.encoding, self.change_some_code)

        print(read_response(self.conn, self.encoding, self.change_some_code))

