import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
# from tests.test_user_repository import TestUserRepository
from tests.test_http_client import TestHTTPClient