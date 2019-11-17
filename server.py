from tornado import ioloop, web

from src.handler import MainHandler


def main_app():
    return web.Application([
        ('/', MainHandler),
    ])


if __name__ == '__main__':
    print('Running at http://localhost:8080')
    app = main_app()
    app.listen(8080)
    ioloop.IOLoop.current().start()
