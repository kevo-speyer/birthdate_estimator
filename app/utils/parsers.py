import json
from utils import variant_handler


def parse_model_info(model_info):
    """Make different model_info input formats compatible"""

    if model_info is None:  # Select model from config
        return variant_handler.select_model()

    print(f"request model_info {model_info}")

    model_info = json.loads(json.dumps(model_info))
    if isinstance(model_info, str):
        model_info = json.loads(model_info.replace("'", '"'))

    print(f"clean model_info {model_info}")

    return model_info


def parse_dnis(dnis):
    """Make different dni input formats compatible"""

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
