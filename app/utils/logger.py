import logbook
from app import Bryant
from app.utils.decorator import SingletonDecorator


@SingletonDecorator
class Log:
    handler = None

    def __init__(self, name='Bryant', filename=Bryant.config['LOG_NAME']):
        """

        :param name: 业务名称,日志的分类，如果不传入则默认为Bryant
        :param filename: 文件名称
        """
        self.handler = logbook.FileHandler(filename, encoding='utf-8')
        logbook.set_datetime_format("local")  # 将日志时间设置为本地时间
        self.logger = logbook.Logger(name)
        self.handler.push_application()

    def info(self, *args, **kwargs):
        return self.logger.info(*args, **kwargs)

    def error(self, *args, **kwargs):
        return self.logger.error(*args, **kwargs)

    def warning(self, *args, **kwargs):
        return self.logger.warning(*args, **kwargs)

    def debug(self, *args, **kwargs):
        return self.logger.debug(*args, **kwargs)
