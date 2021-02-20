# Graphene SGX

from commit: 2cfdd510dcd95fde4e6442eafaf9549dbc8f97b4

# Usage

## sklearn docker mode
```bash
cd Tools/gsc/test
make DISTRIBUTION=ubuntu18.04 SGXDRIVER_BRANCH=sgx_driver_2.6 TESTCASES=sklearn
docker run --device=/dev/isgx -v /var/run/aesmd/aesm.socket:/var/run/aesmd/aesm.socket gsc-ubuntu18.04-sklearn /graphene/Examples/kmeans.py
```