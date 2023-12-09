#!/usr/bin/python3
import cmd
import models.base_model as base

listOfClass = {
    "BaseModel": base.BaseModel
}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to to exit the program"""
        return True

    def do_create(self, creation):
        """Craetes new object"""
        if not creation:
            print("** class name missing")
        elif creation not in listOfClass:
            print("** class doesn't exist")
        else:
            new_obj = listOfClass[creation]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, showcase):
        """shows object"""
        showarguments = showcase.split(" ")
        if not showcase:
            print("** class name missing")
        elif showarguments[0] not in listOfClass:
            print("** class doesn't exist")
        elif showarguments[0] in listOfClass and len(showarguments) == 1:
            print("** instance id missing")
        else:
            storedObjs = base.storage.all()
            inputkey = "{}.{}".format(showarguments[0], showarguments[1])
            if inputkey in storedObjs.keys():
                print(storedObjs[inputkey])
            else:
                print("** instance id doesn't exist")

    def do_destroy(self, delete):
        """deletes object instance"""
        arguments = delete.split(" ")
        if not delete:
            print("** class name missing")
        elif arguments[0] not in listOfClass:
            print("** class doesn't exist")
        elif arguments[0] in listOfClass and len(arguments) == 1:
            print("** instance id missing")
        else:
            storedObjs = base.storage.all()
            inputkey = "{}.{}".format(arguments[0], arguments[1])
            if inputkey in storedObjs.keys():
                del storedObjs[inputkey]
                base.storage.save()
            else:
                print("** instance id doesn't exist")

    def do_all(self, allObj):
        if allObj == ".":
            objects = [str(x) for x in base.storage.all().values()]
            print(objects)
        elif allObj in listOfClass:
            obj = [
                str(value)
                for key, value in base.storage.all().items()
                if key.split(".")[0] == allObj
            ]
            print(obj)
        else:
            print("** class doesn't exist")

    do_EOF = do_quit


if __name__ == "__main__":
    HBNBCommand().cmdloop()
