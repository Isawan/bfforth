container_bin:= podman
tester_name:="bfforth-tester"

bff4/bff4: bff4/bff4.c
	gcc -O2 $^ -o $@

.PHONY: test
test:
	$(container_bin) build . -t $(tester_name)
	$(container_bin) run --mount=type=bind,source=./,destination=/mnt $(tester_name) ./runtests
