container_bin:=podman
test_runner:=bfforth-tester
cc_runner:=cc-runner

all: test

bff4/bff4: bff4/bff4.c tomb/$(cc_runner)
	$(container_bin) container run --mount=type=bind,source=./,destination=/mnt $(cc_runner) -O2 $@.c -o $@

tomb/$(test_runner): Dockerfile.$(test_runner)
	$(container_bin) image build . -f Dockerfile.$(test_runner) -t $(test_runner)
	touch $@

tomb/$(cc_runner): Dockerfile.$(cc_runner)
	$(container_bin) image build . -f Dockerfile.$(cc_runner) -t $(cc_runner)
	touch $@

.PHONY: test
test: tomb/$(test_runner) bff4/bff4 ./runtests
	$(container_bin) container run --mount=type=bind,source=./,destination=/mnt $(test_runner) ./runtests
