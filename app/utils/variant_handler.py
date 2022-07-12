import os
import random
from config import config


def select_model():
    """Chooses one model taking into account variants for A/B testing"""

    env = os.getenv("ENV", "DEV")
    print(f"Environment: {env}")

    models = config[env]["default_model_info"]
    models = models if isinstance(models, list) else [models]

    if len(models) == 0:  # Only one variant
        return models[0]

    # At this point models is a list with dict models with key "proba"
    # Choose model variant according to their probabilities in config
    model_info = random.choices(models, weights=[model["proba"] for model in models])
    model_info = model_info.pop()

    print(f"model_info chosen from variants: {model_info}")

    return model_info
