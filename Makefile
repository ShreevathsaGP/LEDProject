main: src/main.cpp writing
	g++ build/writing.o src/main.cpp -o bin/run -I include

writing: src/writing.cpp
	g++ -c src/writing.cpp -o build/writing.o -I include

run: main
	./bin/run
