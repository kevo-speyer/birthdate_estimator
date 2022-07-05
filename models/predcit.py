import pickle
import shutil
import numpy as np
import datetime as dt
from pathlib import Path


class Predictor:
    def __init__(self, model_info):
        self.model = self.get_model(model_info)

    def predict(self, dnis):
        dnis = np.array([dnis]).reshape(-1, 1)
        preds = self.model.predict(dnis)
        dates = []
        for pred in preds:
            date = self.year_frac_to_date(pred)
            dates.append(date.strftime("%Y-%m-%d"))
        return dates

    @staticmethod
    def year_frac_to_date(year_frac):
        year = int(np.floor(year_frac))
        days = (year_frac - year) * 365
        date = dt.datetime(year, 1, 1) + dt.timedelta(int(days))
        return date

    def get_model(self, model_source):
        filename = model_source["filename"]
        try:  # Check out cache first
            model = pickle.load(open(f"/tmp/{filename}", "rb"))
        except:
            if model_source.get("location") == "filesystem":
                model_path = model_source.get("path", Path(__file__).parent.absolute())
                src, dst = f"{model_path}/{filename}", f"/tmp/{filename}"
                shutil.copyfile(src, dst)
                model = pickle.load(open(f"/tmp/{filename}", "rb"))

        return model
