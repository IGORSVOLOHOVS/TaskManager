---
trigger: model_decision
description: Create .clangd file
---

Example:
CompileFlags:
  Add:
    - -std=c++23
    - -Wall
    - -Wextra
    - -Wpedantic
    - -Wconversion
    - -Wsign-conversion
    - -Wshadow
    - -Wnon-virtual-dtor
    - -Wold-style-cast
    - -Wcast-align
    - -Wunused
    - -Woverloaded-virtual
    - -Wmisleading-indentation
    - -Wnull-dereference
    - -Wdouble-promotion
    - -Wformat=2
    - -Wimplicit-fallthrough
    - -I.
    # Ensure we use standard C++ library that supports C++23 (like libc++ or libstdc++)
    # - -stdlib=libc++ # Optional, depends on system

Diagnostics:
  ClangTidy:
    Add:
      - bugprone-*
      - cert-*
      - cppcoreguidelines-*
      - misc-*
      - modernize-*
      - performance-*
      - readability-*
      - portablity-*
    Remove:
      - modernize-use-trailing-return-type
      - cppcoreguidelines-avoid-magic-numbers
      - readability-magic-numbers
      - llvm-include-order # Conflicts with some organizations
      - google-readability-todo # We might use TODOs
    CheckOptions:
      readability-identifier-naming.NamespaceCase: lower_case
      readability-identifier-naming.ClassCase: CamelCase
      readability-identifier-naming.StructCase: CamelCase
      # FunctionCase: lower_case is standard snake_case, but user didn't specify naming convention strictly, 
      # but standard C++ often uses snake_case for functions.
      readability-identifier-naming.FunctionCase: lower_case
      readability-identifier-naming.VariableCase: lower_case
      readability-identifier-naming.GlobalConstantCase: UPPER_CASE

InlayHints:
  Designators: true
  Enabled: true
  ParameterNames: true
  DeducedTypes: true
  BlockEnd: true

Hover:
  ShowAKA: true
