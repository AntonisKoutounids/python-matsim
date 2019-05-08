.PHONY: all maven python python_pbf

all: maven python

maven:
	cd java/ && mvn install -DskipTests=true

python_pbf: maven
	cp -v java/target/generated-sources/python/*_pb2.py python/

python: python_pbf
