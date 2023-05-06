project = fm
version = 0.1.3 # conanfile.py


.PHONY: build
build:
	conan create . --build=missing # build inside Conan cache (~/conan2/p)


.PHONY: publish
publish:
	conan upload --remote=astro ${project}/${version}