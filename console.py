#!/usr/bin/python3
import cmd
import sys
import models.base_model as base


class HBNBCommand(cmd.Cmd):
    if sys.stdin.isatty():
        prompt = "(hbnb) "

    listOfClass = {
        "BaseModel": base.BaseModel
    }

    def do_quit(self, arg):
        """Quit command to to exit the program"""
        return True

    def do_create(self, creation):
        """Craetes new object"""
        if not creation:
            print("** class name missing **")
        elif creation not in self.listOfClass:
            print("** class doesn't exist **")
        else:
            new_obj = self.listOfClass[creation]()
            new_obj.save()
            print(new_obj.id)

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

    def do_destroy(self, delete):
        """deletes object instance"""
        arguments = delete.split(" ")
        if not delete:
            print("** class name missing **")
        elif arguments[0] not in self.listOfClass:
            print("** class doesn't exist **")
        elif arguments[0] in self.listOfClass and len(arguments) == 1:
            print("** instance id missing **")
        else:
            storedObjs = base.storage.all()
            inputkey = "{}.{}".format(arguments[0], arguments[1])
            if inputkey in storedObjs.keys():
                del storedObjs[inputkey]
                base.storage.save()
            else:
                print("** instance id doesn't exist **")

    def do_all(self, allObj):
        if allObj == ".":
            objects = [str(x) for x in base.storage.all().values()]
            print(objects)
        elif allObj in self.listOfClass:
            obj = [
                str(value)
                for key, value in base.storage.all().items()
                if key.split(".")[0] == allObj
            ]
            print(obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, updates):
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
        
        if inputkey in storedObjs.keys(): # and arguments[2] in storedObjs[inputkey]:
            mod = storedObjs[inputkey]
            setattr(mod, arguments[2], arguments[3])
            mod.save()
        else:
            print("** value missing **")

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
