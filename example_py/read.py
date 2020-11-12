import sys
import utils_file as uf

from pb2_gen import request_pb2
from pb2_gen import settings_pb2

### Example functions
def ExampleRead():
    uf.ReadRequestFromFile(input("[INPUT] Enter output filename: "))

# Main
ExampleRead()