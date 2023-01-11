from pathlib import Path

# Data routing
DATA_FOLDER = '\\app\\data\\'
BASE_DIR = Path(__file__).resolve(strict=True).parent
PATH_DIR = (str(BASE_DIR) + DATA_FOLDER)

# Data processing configuration
DATE = '2019-06-01'  # datetime.now().strftime("%Y-%m-%d")
ALLOWED_EXTENSIONS = {'json'}
N_BATCH_FILES = 50  # Reading Files every 50
JSON_CHUNKS_SIZE = 10000  # Reading Lines every 10000
