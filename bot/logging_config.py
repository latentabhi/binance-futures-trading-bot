import logging

def setup_logging(log_file="trading_bot.log"):
    log = logging.getLogger("binance_bot")
    log.setLevel(logging.DEBUG)

    fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # log to file
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)

    # console logger for critical errors only
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    ch.setFormatter(fmt)

    log.addHandler(fh)
    log.addHandler(ch)
    
    # disable propagation to prevent double logging in cli
    log.propagate = False

    return log

logger = setup_logging()
