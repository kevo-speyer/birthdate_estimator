import json
from pyexpat import model
from statistics import mode
from models.predcit import Predictor

DEFAULT_MODEL_INFO = {
    "filename": "bspline_model_date_by_dni.pickle",
    "location": "filesystem",
    "path": "./models",
}

DEFAULT_S3_MODEL_INFO = {
    "filename": "test_model.pickle",
    "location": "s3",
    "path": "prd",
    "bucket": "dni-bdai-models",
}


def handler(event, context):
    """Lambda app entrypoint"""

    # 1. Read inputs
    query = read_query(event)
    dnis = parse_dnis(query["dnis"])
    model_info = parse_model_info(query.get("model_info"))

    # 2. Load model
    predictor = Predictor(model_info)

    # 3. Estimate with model
    estimated_birthdates = predictor.predict(dnis)

    # 4. Return predictions
    body = f"Estimated birthdates: {dict(zip(dnis, estimated_birthdates))}"
    ret = {"statusCode": 200, "body": json.dumps(body)}

    return ret

def parse_model_info(model_info):
    if model_info is None:
        return DEFAULT_MODEL_INFO
    print(f"raw model_info {model_info}")
    model_info = json.loads(json.dumps(model_info))
    if isinstance(model_info, str):
        model_info = json.loads(model_info.replace("'",'"'))
    print(f"clean model_info {model_info}")
    return model_info

def parse_dnis(dnis):
    """Make different input formats compatible"""

    def unnest_list(nested_list):
        if isinstance(nested_list[0], list):
            return unnest_list(nested_list[0])
        return nested_list

    print(f"raw dnis: {dnis}")
    dnis = json.loads(f"[{str(dnis)}]")
    dnis = unnest_list(dnis)
    dnis = [int(dni) for dni in dnis]
    print(f"clean dnis: {dnis}")
    return dnis


def read_query(event):
    """Normalize query string depending on source"""
    print(f"raw query {event}")
    if "queryStringParameters" in event:  # Source: API Gateway
        query = event["queryStringParameters"]
    else:  # Direct Lambda call (Tests)
        query = event

    return query
