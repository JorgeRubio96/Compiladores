all: test
 
parser.cc: parser.y
        bison++ -d -hparser.h -o $@ $<
 
scanner.cc: scanner.l
        flex++ -d -o$@ $<
 
test:  parser.o scanner.o test.o
        g++ -o $@ test.o parser.o scanner.o
 
clean:
        $(RM) *~ *# test *.o *.h
        $(RM) parser.cc scanner.cc