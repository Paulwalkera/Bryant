from app import Bryant
from app.utils.logger import Log


@Bryant.route('/')
def index():
    log = Log()
    log.info("你")
    return 'Hello word'


if __name__ == '__main__':
    Bryant.run(host="0.0.0.0", debug=True, threaded=True, port=7777)
