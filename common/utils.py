import os
import base64
import pandas as pd
import logging.config
from datetime import datetime
from django.conf import settings
from urllib.parse import parse_qs
from django.shortcuts import redirect


class Authentication:

    @staticmethod
    def inventory_login_decorator(func):
        def _wrapper_view(request):
            
            if 'user_logged_in' in request.session and 'role_id' in request.session:
                if request.session['role_id'] in [1, 2] and request.session['user_logged_in'] == True:
                    result = func(request)
                    return result
                
                # Comment Redirect to wrong access page

            return redirect('inventory_logout')
        
        return _wrapper_view
    

class CustomLogging:
    
    @staticmethod
    def get_logging_config(module_name):
        """
        Returns a dictionary for logging configuration based on the module name.
        """
        # Base directory for logs
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Get the current date
        current_datetime = datetime.now()
        current_day = current_datetime.strftime('%d')
        current_month = current_datetime.strftime('%m')
        current_year = current_datetime.strftime('%Y')

        # Create directory structure for logs
        LOG_DIR = os.path.join(BASE_DIR, f"log/{current_year}/{current_month}/{current_day}")
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)

        return {
            "version": 1,
            "disable_existing_loggers": True,
            "formatters": {
                "verbose": {
                    "format": "{levelname} {asctime} {module} {lineno} {message}",
                    "style": "{",
                }
            },
            "filters": {
                "require_debug_true": {
                    "()": "django.utils.log.RequireDebugTrue",
                }
            },
            "handlers": {
                "django": {
                    "level": "DEBUG",
                    "filters": ["require_debug_true"],
                    "class": "logging.handlers.RotatingFileHandler",
                    "formatter": "verbose",
                    "filename": os.path.join(LOG_DIR, f"{module_name}.log"),
                    "maxBytes": 10 * 1024 * 1024,    # Max 10 MB
                    "backupCount": 5,                # Keep up to 5 old log files
                    "encoding": "utf-8",
                }
            },
            "loggers": {
                module_name: {
                    "handlers": ["django"],
                    "level": "DEBUG",
                    "propagate": True,
                }
            },
        }


    @staticmethod
    def setup_logger(module_name):
        """
        Configures the logger for a specific module.
        Returns a logger instance.
        """
        logging.config.dictConfig(CustomLogging.get_logging_config(module_name))
        return logging.getLogger(module_name)
    

class Cryptography:

    @staticmethod
    def query_param_decryption(encoded_key):
        # Decode the Base64 string
        decoded_bytes = base64.b64decode(encoded_key)
        # Convert the decoded bytes back to string (assuming UTF-8 encoding)
        decoded_string = decoded_bytes.decode('utf-8')

        return parse_qs(decoded_string)
    

class ExcelOperations:

    @staticmethod
    def export_data_to_csv_format(export_data, column_names, filename):
        try:
            # creating dataframe for excel
            data_frame = pd.DataFrame(export_data)
            
            # Checking if the data matches the column names
            if len(data_frame.columns) != len(column_names):
                raise ValueError("Number of columns in the data does not match the column names provided.")

            # Assigning new column names
            data_frame.columns = column_names

            # Saving dataframe to CSV
            csv_file_path = os.path.join(settings.STATIC_URL.lstrip('/'), 'assets/exports', filename + '.csv')
            print(csv_file_path)
            data_frame.to_csv(csv_file_path, index=False)

            return {"res_status": True, "res_message": "Data exported succcessfully.", "res_fileName": filename}
        
        except FileNotFoundError:
            return {"res_status": False, "res_message": "Error: The file path is invalid or not writable."}

        except PermissionError:
            return {"res_status": False, "res_message": "Error: Permission denied when trying to write to the file."}

        except ValueError as ve:
            return {"res_status": False, "res_message": f"Error: {ve}"}
            
        except Exception as e:
            return {"res_status": False, "res_message": f"An unexpected error occurred: {e}"}