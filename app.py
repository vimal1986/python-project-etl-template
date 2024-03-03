import os
import logging
import sys
import traceback
import requests
LOGGER = logging.getLogger(__name__)

from utilty.db_connect import *
from utilty.helper import insertOrUpdateRecordQD, createTableQB, createQBApp
from dotenv import load_dotenv

load_dotenv()


def extract_data(arg1: str)-> str:
   
   return ""
      
      
def load_data(student_data):
    pass

def transform_data():
    pass
    

def main():
    init_logs()
    

if __name__ == '__main__':
    main()