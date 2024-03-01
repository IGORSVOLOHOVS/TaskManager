#pragma once
#include <config.hpp>
#include <benchmark/benchmark.h>

static void BM_StringCreation(benchmark::State& state) {
  for (auto _ : state)
    std::string empty_string;
}
BENCHMARK(BM_StringCreation);
BM_StringCreation->Arg(ARG["test1"][3].as<int>())->Arg(ARG["test1"][4].as<int>())->Arg(ARG["test1"][5].as<int>());



static void BM_StringCopy(benchmark::State& state) {
  std::string x = "hello";
  for (auto _ : state)
    std::string copy(x);
}
BENCHMARK(BM_StringCopy);

namespace benchmark
{
  void run(int argc = 1, std::vector<char*> argv = {(char*)""})
  {
    ::benchmark::Initialize(&argc, argv.data());
    ::benchmark::RunSpecifiedBenchmarks();
  }
} // export namespace benchmark
