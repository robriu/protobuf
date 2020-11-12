import sys
import utils_file as uf

from pb2_gen import request_pb2
from pb2_gen import settings_pb2

### Example functions
def ExampleWrite():
    req = CreateRequest()

    if uf.VerifyRequestMessage(req):
        uf.WriteRequestToFile(req, input("[INPUT] Enter output filename: "))

### Util Functions
def CreateRequest():
    req = request_pb2.Request()

    req.id = 1
    req.sequence = 1
    req.request_message = "Quality Enhancement Request"   # Optional field

    settings = CreateSettings()
    # req_settings = req.set_request.set_settings
    req.set_request.set_settings.MergeFrom(settings)

    return req

def CreateSettings():
    set_settings = request_pb2.Request().set_request.set_settings
    set_settings.profile_id = int(input("Enter profile id: "))
    set_settings.requirements = input("Enter requirements: ") if input("Wish to add requirements? (y/n): ") == 'y' else 'Empty'
    set_settings.print_settings.quiality.layer_height = 1.5

    return set_settings

# Main
ExampleWrite()
