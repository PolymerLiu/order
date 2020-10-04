from application import app

def main():
  app.run(host='0.0.0.0',debug=True)


if __name__ == '__main__':
  try:
    # 引入sys来捕获工程的所有异常
    import sys
    sys.exit(main())

  except Exception as e:
    import traceback
    traceback.print_exc()