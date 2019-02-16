import socket

from tools.handler import Handler
from tools.helper import from_string_to_command_and_args
from tools.response_reader import read_response


def run(addr, port, encoding, change_ff_code):
    with socket.socket() as s:
        s.connect((addr, port))

        print(read_response(s, encoding, change_ff_code))

        handler = Handler(s, encoding, change_ff_code)

        while True:
            print(">>>", end='')
            cmd = input()

            if cmd == '':
                print("You input empty string", end="\n\n")
                continue

            handler.execute_command_by_string(cmd)

            command_name = from_string_to_command_and_args(cmd)[0]

            if command_name == "quit":
                break
