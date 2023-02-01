#encoding:utf-8
import argparse
import os
from sanic import Sanic

import server

def run(args):
    app = server.create_app()
    app.run(host=args.host, port=args.port)

def create_argument_parser() -> argparse.ArgumentParser:
    """ """
    # create the top-level parser
    parser = argparse.ArgumentParser(
                prog="funnybox",
                description="funnybox command line interface."
            )
    subparsers = parser.add_subparsers()

    # create the parser for the "run" command
    parser_run = subparsers.add_parser('run')
    parser_run.add_argument('--host', default='0.0.0.0', type=str, help="运行服务的host")
    parser_run.add_argument('--port', default=8000, type=int, help="运行服务的port")
    parser_run.set_defaults(func=run)

    return parser_run

def main():
    parser = create_argument_parser()
    cmdline_arguments = parser.parse_args()
    cmdline_arguments.func(cmdline_arguments)

if __name__ == "__main__":
    main()
