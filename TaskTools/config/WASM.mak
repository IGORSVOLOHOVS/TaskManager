# make -f WASM.mak
CXX       := em++
CXX_FLAGS := -Wall -Wextra -std=c++20 -ggdb --bind -s WASM=1 -s EXPORT_ALL=1 

BIN      := bin
SRC      := src
INCLUDE  := include
LIB      := lib
MODULE   := module

MODS     := $(wildcard $(MODULE)/*.cpp)
MOD_OBJS := $(patsubst $(MODULE)/%.cpp,$(BIN)/%.o,$(MODS))

HEADERS  := $(wildcard $(INCLUDE)/*.hpp)

# WebAssembly не поддерживает нативные библиотеки, такие как pthread, sqlite3 и т.д.
# Поэтому, если вы хотите использовать их, вам нужно собрать их с помощью Emscripten.
# Подробнее: https://emscripten.org/docs/porting/pthreads.html
# mkdir build
# cd build
# emcmake cmake ..
# emmake make
# (после сборки добавь .h в /include, а .a в /lib ---> -lsqlite3)
LIBRARIES   := 
EXECUTABLE  := main

all: $(BIN)/$(EXECUTABLE).js

run: all
	start http://localhost:8000   # Для Windows
	python3 -m http.server 8000
	
$(BIN)/%.o: $(MODULE)/%.cpp
	$(CXX) $(CXX_FLAGS) -c $< -o $@

$(BIN)/%.o: $(INCLUDE)/%.hpp
	$(CXX) $(CXX_FLAGS) -c $< -o $@

$(BIN)/$(EXECUTABLE).js: $(SRC)/*.cpp $(MOD_OBJS) $(HEADERS)
	$(CXX) $(CXX_FLAGS) -I$(INCLUDE) -L$(LIB) $^ -o $(BIN)/$(EXECUTABLE).js $(LIBRARIES)
