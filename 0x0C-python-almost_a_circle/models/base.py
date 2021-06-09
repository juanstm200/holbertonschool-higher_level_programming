#!/usr/bin/python3
"""Modeules Class Import"""
import json
import csv
from collections import OrderedDict


class Base():
    """ Class: Base, stores the basic attribute. """

    __nb_objects = 0

    def __init__(self, id=None):
        """init :id(int): value for the id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draw: Prints the objects on an external Xwindow."""
        # Setup for the screen.
        import turtle
        from random import randint
        screen = turtle.getscreen()
        screen.title("Almost A Circle!!")
        screen.setup(width=500, height=500, startx=None, starty=None)
        turtle.setworldcoordinates(-40, -7, 180, 180)
        turtle.hideturtle()
        turtle.speed(1)
        screen.bgcolor("black")
        screen.colormode(255)
        turtle.pensize(3)

        def move_turtle(list_r, list_s):
            """Moves the turtle according to the object's dimensions and"""
            for obj in list_r:
                turtle.pu()
                turtle.home()
                turtle.setpos(obj.x, obj.y)
                turtle.pencolor(randint(80, 255),
                                randint(80, 255),
                                randint(80, 255))
                for lines in range(2):
                    turtle.pd()
                    turtle.forward(obj.width)
                    turtle.left(90)
                    turtle.forward(obj.height)
                    turtle.left(90)

            for obj in list_s:
                turtle.pu()
                turtle.home()
                turtle.setpos(obj.x, obj.y)
                turtle.pencolor(randint(80, 255),
                                randint(80, 255),
                                randint(80, 255))
                for lines in range(4):
                    turtle.pd()
                    turtle.forward(obj.size)
                    turtle.left(90)

        def draw_title():
            turtle.pu()
            turtle.setpos(71, 155)
            turtle.pencolor(randint(80, 255),
                            randint(80, 255),
                            randint(80, 255))
            turtle.write("              Almost a Circle\n" +
                         "By Diego Lopez @HolbertonSchool\n" +
                         "                      2021",
                         False, align="center", font=("Arial", 16, "normal"))
            turtle.pu()

        draw_title()
        move_turtle(list_rectangles, list_squares)
        turtle.getscreen()._root.mainloop()

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves the given list of object"""
        filename = "{}.csv".format(cls.__name__)
        if list_objs:
            list_of_dictionaries = list(map(cls.to_dictionary, list_objs))
            list_of_headers = list(list_of_dictionaries[0].keys())
        with open(filename, 'w', newline='') as csv_file:
            if list_objs is None or bool(list_objs) is False:
                csv_file.write("[]")
            else:
                writer = csv.DictWriter(csv_file, list_of_headers)
                writer.writeheader()
                writer.writerows(list_of_dictionaries)

    @classmethod
    def load_from_file_csv(cls):
        """Reads from .csv file and returns a list"""
        filename = "{}.csv".format(cls.__name__)
        list_of_dictionaries = []
        tmp_dictionary = {}
        list_of_objects = []
        try:
            with open(filename, newline='') as scv_file:
                reader = csv.DictReader(scv_file)
                for row in reader:
                    for key in row:
                        tmp_dictionary[key] = int(row[key])
                    dummy = cls.create(**tmp_dictionary)
                    list_of_objects.append(dummy)

        except FileNotFoundError:
            list_of_objects = []

        return(list_of_objects)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file"""
        filename = "{}.json".format(cls.__name__)
        list_dict = []
        if list_objs is None:
            pass
        else:
            list_dict = list(map(cls.to_dictionary, list_objs))

        with open(filename, "w") as json_txt_file:
            json_txt_file.write(cls.to_json_string(list_dict))

    @classmethod
    def load_from_file(cls):
        """ load_from_file"""
        filename = "{}.json".format(cls.__name__)
        list_of_dictionaries = []
        list_of_objects = []

        try:
            with open(filename) as json_txt:
                list_of_dictionaries = cls.from_json_string(json_txt.read())
                for attributes in list_of_dictionaries:
                    list_of_objects.append(cls.create(**attributes))

        except FileNotFoundError:
            list_of_objects = []

        return list_of_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to_json_string"""
        if list_dictionaries is None or bool(list_dictionaries) is False:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ from_json_string"""
        if json_string is None:
            json_string = []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an object with pre-set attributes."""
        default = cls(1, 1)
        default.update(**dictionary)
        return(default)
