'''
Module which reads the yaml configuration.
'''
import os
import yaml

class Config:
    @staticmethod
    def get():
        config_file = os.path.join(os.path.dirname(__file__), "..", "conf", "config.yml")
        with open(config_file, "r") as f:
            return yaml.load(f.read())

