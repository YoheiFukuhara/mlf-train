# import tensorflow as tf
from pip._internal.operations import freeze
import sys

print('python version:', sys.version)

x = freeze.freeze()
for p in x:
    print(p)
