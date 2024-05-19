#!/usr/bin/python3
"""command line terminal"""
import cmd
import sys
import models.base_model as base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Startin point"""

    if sys.stdin.isatty():
        prompt = "(hbnb) "

    listOfClass = {
        "BaseModel": base.BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to to exit the program"""
        return True

    def do_eof(self, arg):
        """eof for quiting"""
        if arg == "eof":
            return True

    def do_create(self, creation):
        """Creates new object"""
        if not creation:
            print("** class name missing **")
        elif creation not in self.listOfClass:
            print("** class doesn't exist **")
        else:
            new_obj = self.listOfClass[creation]()
            new_obj.save()
            print(new_obj.id)

    def do_destroy(self, delete):
        """deletes objects"""
        arguments = delete.split(" ")
        if not delete:
            print("** class name missing **")
        elif arguments[0] not in self.listOfClass:
            print("** class doesn't exist **")
        elif arguments[0] in self.listOfClass and len(arguments) == 1:
            print("** instance id missing **")
        else:
            storedObjects = base.storage.all()
            inputkey = "{}.{}".format(arguments[0], arguments[1])
            if inputkey in storedObjects.keys():
                del storedObjects[inputkey]
                base.storage.save()
            else:
                print("** instance id doesn't exist **")

    def do_all(self, allObj):
        """prints all saved objects"""
        if allObj == ".":
            objects = [str(x) for x in base.storage.all().values()]
            print(objects)
        elif allObj in self.listOfClass:
            if hasattr(self.listOfClass[allObj], 'all'):
                obj = [
                    str(obj)
                    for obj in self.listOfClass[allObj].all()
                    ]
            else:
                obj = [
                    str(value)
                    for key, value in base.storage.all().items()
                    if key.split(".")[0] == allObj
                    ]
            print(obj)
        else:
            print("** class doesn't exist **")

    def do_show(self, showcase):
        """shows object"""
        showarguments = showcase.split(" ")
        if not showcase:
            print("** class name missing **")
        elif showarguments[0] not in self.listOfClass:
            print("** class doesn't exist **")
        elif showarguments[0] in self.listOfClass and len(showarguments) == 1:
            print("** instance id missing **")
        else:
            storedObjs = base.storage.all()
            inputkey = "{}.{}".format(showarguments[0], showarguments[1])
            if inputkey in storedObjs.keys():
                print(storedObjs[inputkey])
            else:
                print("** no instance found **")

    def do_update(self, updates):
        """updates objects of specified instance"""
        arguments = updates.split(" ")
        if arguments[0] not in self.listOfClass:
            print("** class doesn't exist **")
            return
        elif len(arguments) == 0:
            print("** class name missing **")
            return
        elif len(arguments) == 1:
            print("** instance id missing **")
            return
        inputkey = "{}.{}".format(arguments[0], arguments[1])
        storedObjs = base.storage.all()
        if inputkey not in storedObjs.keys():
            print("** no instance found **")
            return
        if len(arguments) == 2:
            print("** attribute name missing **")
            return
        if inputkey in storedObjs.keys():
            mod = storedObjs[inputkey]
            setattr(mod, arguments[2], arguments[3])
            mod.save()
        else:
            print("** value missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()