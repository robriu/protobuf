mkdir python\pb2_gen

protoc -I=%CD%\proto --python_out=%CD%\python\pb2_gen %CD%\proto\print_settings.proto
protoc -I=%CD%\proto --python_out=%CD%\python\pb2_gen %CD%\proto\request.proto
protoc -I=%CD%\proto --python_out=%CD%\python\pb2_gen %CD%\proto\response.proto
