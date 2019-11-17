import toml
from tornado import ioloop, web

from src.handler import MainHandler


def main_app():
    return web.Application([
        ('/', MainHandler),
    ])


if __name__ == '__main__':
    with open('./config.toml') as fp:
        config = toml.load(fp)

    port = config['server']['port']

    print(f'Running at http://localhost:{port}')
    app = main_app()
    app.listen(port)
    ioloop.IOLoop.current().start()
