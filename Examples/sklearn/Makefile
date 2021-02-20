# Build as follows:
#
# - make               -- create non-SGX no-debug-log manifest
# - make SGX=1         -- create SGX no-debug-log manifest
# - make SGX=1 DEBUG=1 -- create SGX debug-log manifest
#
# Use `make clean` to remove Graphene-generated files.

GRAPHENEDIR ?= ../..
SGX_SIGNER_KEY ?= $(GRAPHENEDIR)/Pal/src/host/Linux-SGX/signer/enclave-key.pem
PYTHON3 ?= /usr/bin/python3

ifeq ($(DEBUG),1)
GRAPHENE_LOG_LEVEL = debug
else
GRAPHENE_LOG_LEVEL = error
endif

DISTRIB_ID ?= $(shell lsb_release --short --id)
DISTRIB_RELEASE ?= $(shell lsb_release --short --release)

ifeq ($(SGX), 1)
ifneq ($(DISTRIB_ID),Ubuntu)
$(error This example requires Ubuntu when building for SGX.)
endif
endif

UBUNTU_VERSION = $(DISTRIB_ID)$(DISTRIB_RELEASE)

.PHONY: all
all: sklearn.manifest | pal_loader
ifeq ($(SGX),1)
all: sklearn.manifest.sgx sklearn.sig sklearn.token
endif

include ../../Scripts/Makefile.configs

# .manifest.template contains stanzas for both Ubuntu 16 and 18. The last rule selectively enables
# those lines based on the Ubuntu version detected.
%.manifest: %.manifest.template
	sed -e 's|$$(GRAPHENEDIR)|'"$(GRAPHENEDIR)"'|g' \
		-e 's|$$(GRAPHENE_LOG_LEVEL)|'"$(GRAPHENE_LOG_LEVEL)"'|g' \
		-e 's|$$(HOME)|'"$(HOME)"'|g' \
		-e 's|$$(PYTHON3)|'"$(PYTHON3)"'|g' \
		-e 's|# '"$(UBUNTU_VERSION)"' ||g' \
		-e 's|$$(ARCH_LIBDIR)|'"$(ARCH_LIBDIR)"'|g' \
		$< > $@

# Make on Ubuntu <= 20.04 doesn't support "Rules with Grouped Targets" (`&:`),
# we need to hack around.
sklearn.sig sklearn.manifest.sgx: sgx_outputs

.INTERMEDIATE: sgx_outputs
sgx_outputs: sklearn.manifest
	$(GRAPHENEDIR)/Pal/src/host/Linux-SGX/signer/pal-sgx-sign \
		-libpal $(GRAPHENEDIR)/Runtime/libpal-Linux-SGX.so \
		-key $(SGX_SIGNER_KEY) \
		-output sklearn.manifest.sgx \
		-manifest sklearn.manifest

%.token: %.sig
	$(GRAPHENEDIR)/Pal/src/host/Linux-SGX/signer/pal-sgx-get-token -output $@ -sig $<

pal_loader:
	ln -s $(GRAPHENEDIR)/Runtime/pal_loader $@

.PHONY: clean
clean:
	$(RM) *.token *.sig *.manifest.sgx *.manifest pal_loader

.PHONY: distclean
distclean: clean
	$(RM) *.pt
