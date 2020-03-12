# coding:utf-8

import pymysql
pymysql.install_as_MySQLdb()

from ihome import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from gevent.pywsgi import WSGIServer


# 创建flask的应用对象
app = create_app("product")
app.app_context().push()

manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    # http_server = WSGIServer(('',5000),app)
    # http_server.serve_forever()
    manager.run()