CC = g++
CFLAGS = -c -Wall
LDFLAGS = -lwiringPi

SOURCES = main.cpp bme280.cpp
OBJECTS = $(SOURCES:.cpp=.o)
EXECUTABLE = bme280

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(OBJECTS) -o $@ $(LDFLAGS)

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm -f $(OBJECTS) $(EXECUTABLE)
