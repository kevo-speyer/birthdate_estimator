config = {
    "DEV": {
        "default_model_info": [  # each dict is a model variant to do A/B testing
            {
                "filename": "bsplines.pickle",
                "location": "s3",
                "path": "prd",
                "bucket": "dni-bdai-models",
                "proba": 0.75,  # variant probability
            },
            {
                "filename": "linear.pickle",
                "location": "filesystem",
                "path": "./models",
                "proba": 0.25,
            },
        ]
    },
    "PRD": {
        "default_model_info": {
            "filename": "mega_spline_model.pickle",
            "location": "s3",
            "path": "prd",
            "bucket": "dni-bdai-models",
        }
    },
}
