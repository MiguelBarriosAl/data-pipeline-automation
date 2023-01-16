from app.pipeline import Pipeline
from constant import PATH_DIR, N_BATCH_FILES, DATE


def main():
    """
        Class called "Pipeline", passing in three arguments: DATE, PATH_DIR, and N_BATCH_FILES.
        The script then calls a method on the pipeline object called "etl_json()".
        Taking into account that the number of files and the content of each file is unknown, for a better performance
        and scaling of the project, the pipeline allows to configure through constants such as number
        of batches of reading files.
        This class has a method that receives the three parameters passed in the main function and
        stores them as instance variables.
        The "etl_json()" method is performs extraction, transformation, and loading (ETL) process on JSON files.
    """
    pipeline = Pipeline(DATE, PATH_DIR, N_BATCH_FILES)
    pipeline.etl_json()


if __name__ == "__main__":
    main()
