:: Task: Make folders to store generated proto classes
mkdir cpp\pb2_gen
mkdir example_py\pb2_gen

:: Task: CXX Class Generation
REM protoc -I=%CD%\proto --cpp_out=%CD%\cpp\pb2_gen %CD%\proto\settings.proto
REM protoc -I=%CD%\proto --cpp_out=%CD%\cpp\pb2_gen %CD%\proto\request.proto
REM protoc -I=%CD%\proto --cpp_out=%CD%\cpp\pb2_gen %CD%\proto\response.proto

:: Task: Python Class Generation
protoc -I="%CD%\proto" --python_out="%CD%\example_py\pb2_gen" "%CD%\proto\settings.proto"
protoc -I="%CD%\proto" --python_out="%CD%\example_py\pb2_gen" "%CD%\proto\request.proto"
protoc -I="%CD%\proto" --python_out="%CD%\example_py\pb2_gen" "%CD%\proto\response.proto"
