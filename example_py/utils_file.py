from pb2_gen import request_pb2
from pb2_gen import settings_pb2

def VerifyRequestMessage(request):
    print("-----------")
    print(request)

    return request.IsInitialized()

def ReadRequestFromFile(file_name):
    print("[UPDATE] Attempt to read data...")
    request = request_pb2.Request()

    try:
        with open(file_name, "rb") as f:
            if request.ParseFromString(f.read()):
                print("[SUCCESS] Done.\n")
                print(f"{request}")
                return True
            else:
                print("[ERROR] Failed to parse data from file.\n")
    except IOError:
        print (f"{file_name}: Could not open file. Creating a new one.")

def WriteRequestToFile(request, file_name):
    print("[UPDATE] Attempt to write data...")
    
    try:
        with open(file_name, "wb") as f:
            if f.write(request.SerializeToString()):
                print("[SUCCESS] Done.\n")
                return True
            else: 
                print("[ERROR] Failed to write data to file.\n")
    except IOError:
        print (f"{file_name}: Could not open file. Creating a new one.")