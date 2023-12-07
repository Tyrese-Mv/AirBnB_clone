
from models import storage
from models.base_model import BaseModel

if __name__ == "__main__":
    allobjs = storage.all()
    print("___reloaded objects___")
    for items in allobjs.keys():
        obj = allobjs[items]
        print(obj)
    print()
    print("__created obj__")
    mymodel = BaseModel()
    for i in range(1000):
        pass
    mymodel.save()
    print(mymodel)