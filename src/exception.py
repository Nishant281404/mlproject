import sys
import logging

def error_message_detail(error, error_detail):
    _, _, exc_tb = error_detail  # Unpack the tuple
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script [{0}] at line number [{1}]: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    # Configure logging to write logs to a file
    logging.basicConfig(filename='error.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        a = 1 / 0
    except Exception as e:
        logging.error("Division error", exc_info=True)  # Log the exception
        raise CustomException(e, sys.exc_info())  # Pass sys.exc_info() tuple directly
