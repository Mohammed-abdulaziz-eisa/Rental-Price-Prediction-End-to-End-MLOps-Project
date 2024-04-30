from model_services import ModelService

def main():
    ml_svc = ModelService()
    ml_svc.load_model('hypered_rf.pkl')
    pred = ml_svc.predict([85 , 2015 , 2 ,20 , 1 ,1 ,0 ,0 ,1])
    print(pred)
    

if __name__ == '__main__':
    main()