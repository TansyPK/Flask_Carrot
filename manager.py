# import Flask Script object
from flask_script import Manager, Server
from extension import db
from Blog.data_model.models import User
import run
# Init manager object via app object
manager = Manager(run.app)

# Create a new commands: server
# This command will be run the Flask development_env server
manager.add_command("server", Server())


@manager.command
def init_db():
    db.create_all()
    user = User(name='KoiCarrot', email='xxx', password='xxx')
    db.session.add(user)
    db.session.commit()


@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    # 确保有导入 Flask app object，否则启动的 CLI 上下文中仍然没有 app 对象
    return dict(app=run.app)

if __name__ == '__main__':
    manager.run()
