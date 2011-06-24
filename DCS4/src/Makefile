all:
	g++ -c -fPIC -Wall -O -ansi -pedantic utils.cpp -I/usr/include/libnoise -I.
	g++ -shared -o utils.so utils.o -lnoise 

clean:
	rm -rf *.o *.cxx *.so *.pyc
