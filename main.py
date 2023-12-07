# from models import storage
# from models.base_model import BaseModel

# if __name__ == "__main__":
#     mymodel = BaseModel()
    
#     print(mymodel.id)
#     print(mymodel)
#     mymodel.save()
#     print("_____________________________________________")
#     print(type(mymodel.created_at))
    
#     my_model_json = mymodel.to_dict()
#     print()
#     print("_____________________________________________")
#     print("JSON of my_model")
#     for key in my_model_json.keys():
#         print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
#     print()
#     print("______New Class Object_______")
#     my_new_model = BaseModel(**my_model_json)
#     print(my_new_model.id)
#     print(my_new_model)
#     print("_____________________________________________")
#     print(type(my_new_model.created_at))
    
#     print(mymodel is my_new_model)
    