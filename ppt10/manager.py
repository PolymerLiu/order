from application import app,manager
from flask_script import Server
import www

# web server
# 添加不同的命令
manager.add_command('runserver',Server(host='0.0.0.0',port=app.config['SERVER_PORT'],use_debugger=True,use_reloader=None))

def main():
  manager.run()


if __name__ == '__main__':
  try:
    # 引入sys来捕获工程的所有异常
    import sys
    sys.exit(main())

  except Exception as e:
    import traceback
    traceback.print_exc()