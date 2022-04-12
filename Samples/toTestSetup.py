import pytest


class testSetup:
   def setup_module(module):
      print("INSIDE SETUP MODULE")

   def teardown_module(module):
      print("INSIDE TEARDOWN MODULE")

