import json
from models.predcit import Predictor
from utils import parsers


def handler(event, context):
    """Lambda app entrypoint"""

    # 1. Read inputs
    query = parsers.read_query(event)
    dnis = parsers.parse_dnis(query["dnis"])
    model_info = parsers.parse_model_info(query.get("model_info"))

    # 2. Load model
    predictor = Predictor(model_info)

    # 3. Estimate with model
    estimated_birthdates = predictor.predict(dnis)

    # 4. Return predictions
    body = f"Estimated birthdates: {dict(zip(dnis, estimated_birthdates))}"
    ret = {"statusCode": 200, "body": json.dumps(body)}

    return ret
