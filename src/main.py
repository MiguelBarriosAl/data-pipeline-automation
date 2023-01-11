from src.app.pipeline import Pipeline
from src.constant import PATH_DIR, N_BATCH_FILES, DATE


def main():
    pipeline = Pipeline(DATE, PATH_DIR, N_BATCH_FILES)
    pipeline.load_json()


if __name__ == "__main__":
    main()
