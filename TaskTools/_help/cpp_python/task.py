import pytask as t
import sys

t.parser("config.yaml")

t.run_benchmark(sys.argv[1:])

t.run_test(sys.argv[1:])