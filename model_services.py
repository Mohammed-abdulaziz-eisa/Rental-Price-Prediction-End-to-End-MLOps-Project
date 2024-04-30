from pathlib import Path
from model import build_model
import pickle as pkl
class ModelServices:
    def __init__(self):
        self.model = None
        
        
    def load_model(self , model_name = "hypered_rf.pkl"):
        model_path = Path("/model/hypered_rf.pkl")
        
        if not model_path.exists():
            build_model()
            
        self.model = pkl.load('./model/hypered_rf.pkl' , 'rb')
        
        
    def predict(self , input_parameters):
        return self.model.predict([input_parameters])


#test
ml_svr = ModelServices()
ml_svr.load_model('/model/hypered_rf.pkl')