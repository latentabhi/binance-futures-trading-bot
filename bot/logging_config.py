import logging

def setup_logging(log_file="trading_bot.log"):
    log = logging.getLogger("binance_bot")
    log.setLevel(logging.DEBUG)

    # Standard python logging format
    fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # file handler
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)

    # console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    ch.setFormatter(fmt)

    log.addHandler(fh)
    log.addHandler(ch)

    return log

logger = setup_logging()
