import argparse

import server

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="ftp client")
    parser.add_argument("-e", "--encoding", default="utf-8", help="encoding for text data")
    parser.add_argument("server_address")
    parser.add_argument("-p", "--port", default=21)
    parser.add_argument("--ya", help="change code in letter я", default=False, action='store_true')

    args = parser.parse_args()

    server.run(args.server_address, int(args.port), args.encoding, args.ya)
