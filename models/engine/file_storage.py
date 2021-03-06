#!/usr/bin/python3
"""
Handles I/O, writing and reading, of JSON for storage of all class instances
"""
import json
from models import base_model, amenity, city, place, review, state, user
from datetime import datetime

strptime = datetime.strptime
to_json = base_model.BaseModel.to_json


class FileStorage:
    """handles long term storage of all class instances"""
    CNC = {
        'BaseModel': base_model.BaseModel,
        'Amenity': amenity.Amenity,
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'User': user.User
    }
    """CNC - this variable is a dictionary with:
    keys: Class Names
    values: Class type (used for instantiation)
    """
    __file_path = './dev/file.json'
    __objects = {}

    def delete(self, obj=None):
        """ deletes obj from __objects if it extists """
        if obj.id in FileStorage.__objects.keys():
            del(FileStorage.__objects[obj.id])

    def all(self, cls=None):
        """returns private attribute: __objects"""
        # return FileStorage.__objects

        if cls is None:
            return FileStorage.__objects
        else:
            result = {}
            for k, v in FileStorage.__objects.items():
                if v.__class__.__name__ == cls:
                    result[k] = v
            return result

    def new(self, obj):
        """sets / updates in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            FileStorage.__objects[obj.id] = obj
#        bm_id = "{}.{}".format(type(obj).__name__, obj.id)
#        FileStorage.__objects[bm_id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        fname = FileStorage.__file_path
        d = {}
        for bm_id, bm_obj in FileStorage.__objects.items():
            d[bm_id] = bm_obj.to_json()
        with open(fname, mode='w', encoding='utf-8') as f_io:
            json.dump(d, f_io)

    def reload(self):
        """if file exists, deserializes JSON file to __objects, else nothing"""
        fname = FileStorage.__file_path
        FileStorage.__objects = {}
        try:
            with open(fname, mode='r', encoding='utf-8') as f_io:
                new_objs = json.load(f_io)
        except:
            return
        for o_id, d in new_objs.items():
            k_cls = d['__class__']
            FileStorage.__objects[o_id] = FileStorage.CNC[k_cls](**d)

    def close(self):
        """  calls reload for desirializing JSON to object  """
        self.reload()
