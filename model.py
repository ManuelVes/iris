from pydantic import BaseModel,conlist
import joblib

classes = {
    0: 'verginica',
    1: 'versicolor',
    2: 'altro'
}

class Feature_type(BaseModel):
    #description: Optional[str] = None questo è un campo opzionale
    feature1: float = 10.6 # 10.6 default value
    feature2: float = 3.16 # 3.16 default value
    feature3: float = 2.4  # 2.4  default value
    feature4: float = 5.4  # 5.4  default valu

    #name: constr(min_length=1)  # 1
    #scores: conlist(int, min_items=1) 



model = joblib.load("iris.pkl")
#model = joblib.load("model_api1_.pkl")