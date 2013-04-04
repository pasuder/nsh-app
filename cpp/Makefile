CXX=g++
CXXFLAGS=-Wall -Wextra -pedantic-errors -std=c++0x
LFLAGS=
OBJS=activation_function.o neuronal_network.o

all: main.out

main.out:
	$(CXX) $(CXXFLAGS) $(LFLAGS) src/main.cpp src/activation_function.cpp src/neuronal_network.cpp -o $@

$(OBJS): %.o: src/%.cpp
	$(CXX) -c $(CXXFLAGS) $< -o $@

clean:
	rm -f *.o

.PHONY: all clean