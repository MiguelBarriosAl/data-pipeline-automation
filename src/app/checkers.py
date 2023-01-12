from src.constant import ALLOWED_EXTENSIONS


def check_allowed_file(filename: str):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def check_fields(data: dict, fields: list):
    missing_fields = []
    for field in fields:
        if field not in data:
            missing_fields.append(field)
    assert not missing_fields, f"Following fields do not exist: {missing_fields} in {data}"
    return True

