import logging
import logging.handlers


def log_config(log_name: str):
    log = logging.getLogger(log_name)
    log.setLevel(logging.DEBUG)
    # 포맷 설정
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - [%(process)d] [%(thread)d] "
        "[%(levelname)s] (%(filename)s:%(lineno)d) > %(message)s"
    )

    # 콘솔 로그
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    log.addHandler(ch)

    return log
