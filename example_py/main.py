import sys

from pb2_gen import request_pb2
from pb2_gen import settings_pb2

### Run Examples Below
# ExampleWrite()
# ExampleRead()
# ExampleWriteAndRead()

### Example functions
def ExampleWrite():
    pass

def ExampleRead():
    pass

def ExampleWriteAndRead():
    pass

### Util Functions
def CreateRequest():
    req = request_pb2.Request()
    
    req.id = 1
    req.sequence = 1
    req.message = "Quality Enhancement Request"   # Optional field
    
    settings = CreateSettings()
    req_settings = req.set_request.set_settings()
    req_settings.MergeFrom(settings)

    return req

def CreateSettings():
    set_settings = request_pb2.Request().set_request.set_settings
    set_settings.profile_id = int(input("Enter profile id: "))
    set_settings.requirements = input("Enter requirements: ") if input("Wish to add requirements? (y/n): ") == 'y' else 'Empty'

    

    return set_settings


CreateSettings()

