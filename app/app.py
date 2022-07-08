import json
from models.predcit import Predictor
from utils.parsers import read_query, parse_dnis, parse_model_info 


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