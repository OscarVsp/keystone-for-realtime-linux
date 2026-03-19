SUBDIR := keystone-rt

.PHONY: all
all:
	$(MAKE) -C $(SUBDIR)

%:
	$(MAKE) -C $(SUBDIR) $@