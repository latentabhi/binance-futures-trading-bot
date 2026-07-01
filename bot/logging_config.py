import logging

def setup_logging(log_file="trading_bot.log"):
    log = logging.getLogger("bot")
    log.setLevel(logging.DEBUG)

    fmt = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

    # dump everything to file
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)

    # just show errors in console so we don't mess up the CLI UI
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    ch.setFormatter(fmt)

    log.addHandler(fh)
    log.addHandler(ch)

    return log

logger = setup_logging()
