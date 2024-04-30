from pathlib import Path
import pickle as pk

from model import build_model

class ModelService:
    def __init__(self):
        self.model = None

    def load_model(self, model_name='hypered_rf.pkl'):
        model_path = Path(f'model/{model_name}')

        if not model_path.exists():
            build_model()

        self.model = pk.load(open(f'model/{model_name}', 'rb'))

    def predict(self, input_parameters):
        return self.model.predict([input_parameters])
    
# Test the script

# ml_svc = ModelService()
# ml_svc.load_model('hypered_rf.pkl')
# pred = ml_svc.predict([85 , 2015 , 2 ,20 , 1 ,1 ,0 ,0 ,1])
# print(pred)