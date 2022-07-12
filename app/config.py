config = {
    "DEV": {
        "default_model_info": [  # each dict is a model variant to do A/B testing
            {
                "filename": "bsplines.pickle",
                "location": "filesystem",
                "path": "./models",
                "proba": 2,  # variant probability
            },
            {
                "filename": "linear.pickle",
                "location": "filesystem",
                "path": "./models",
                "proba": 1,
            },
        ]
    },
    "PRD": {
        "default_model_info": {
            "filename": "bsplines.pickle",
            "location": "s3",
            "path": "prd",
            "bucket": "dni-bdai-models",
        }
    },
}
