#!/usr/bin/python3
"""
testing the console for intantialization
and certain events that are worth checking
"""

import unittest
from sqlalchemy.sql.sqltypes import String
from models.engine.db_storage import DBStorage
from io import StringIO
from console import HBNBCommand
import os
import sys
from unittest.mock import patch
from models.state import State
from models.engine.file_storage import FileStorage
import models


class TestConsole(unittest.TestCase):
    """ Tests Console Class """

    # def test_destroy

    def test_create(self):
        """Test whether we make cookies"""
        with patch('sys.stdout', new=StringIO()) as x:
            HBNBCommand().onecmd("create State name=\"Fugue\"")
            state_id = x.getvalue()
        if type(models.storage) != DBStorage:
            for k in models.storage._FileStorage__file_path:
                self.assertNotEqual(x, k)

        if type(models.storage) != DBStorage:
            self.assertEqual(type(state_id), str)

        with patch('sys.stdout', new=StringIO()) as x:
            HBNBCommand().onecmd("create City name=\"Despondency\"")
            city_id = x.getvalue()

        # if type(models.storage) != DBStorage:
        #     with open(models.storage._FileStorage__file_path, 'r') as y:
        #         self.assertIs(city_id, str)

        with patch('sys.stdout', new=StringIO()) as x:
            HBNBCommand().onecmd("create State name=\"Sorrow\"")
            HBNBCommand().onecmd("create City name=\"mild_dysthymia\"")
            city_id = x.getvalue()

        if type(models.storage) != DBStorage:
            with open(models.storage._FileStorage__file_path, 'r') as y:
                self.assertNotIn(city_id, y.read())

    # def test_all

    # def test_update

if __name__ == '__main__':
    unittest.main()
