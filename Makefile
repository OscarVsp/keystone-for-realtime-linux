SUBDIR := keystone-rt

KEYSTONE_PLATFORM ?= hifive_unmatched

.PHONY: all
all:
	$(MAKE) -C $(SUBDIR)

%:
	$(MAKE) -C $(SUBDIR) $@