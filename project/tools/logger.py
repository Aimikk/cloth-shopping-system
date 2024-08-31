import sys
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    encoding="UTF-8",
    handlers=[
        # logging.FileHandler(r"D:\gozaresh.log"),
        logging.StreamHandler(sys.stdout)
        ]
)