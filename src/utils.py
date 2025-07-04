def create_folder(folder_path):
    import os
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def log_message(message):
    import logging
    logging.basicConfig(level=logging.INFO)
    logging.info(message)