config = {
    "DEV": {
        "default_model_info": {
            "filename": "bspline_model_date_by_dni.pickle",
            "location": "filesystem",
            "path": "./models",
        },
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
