
from models.base_model import BaseModel
if __name__ == "__main__":
    mymodel = BaseModel()
    
    print(mymodel)
    
    mymodel.save()
    my_model_json = mymodel.to_dict()
    print()
    print("_____________________________________________")
    print("JSON of my_model")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
    