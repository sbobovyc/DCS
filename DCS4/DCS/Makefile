LIBNOISEINC = /usr/include/libnoise
all:
	g++ -c -fPIC -Wall -O -ansi -pedantic -fopenmp utils.cpp -I${LIBNOISEINC} -I.
	g++ -shared -o utils.so utils.o -lnoise -lgomp

clean:
	rm -rf *.o *.cxx *.so *.pyc
