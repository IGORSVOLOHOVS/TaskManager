#pragma once

#define SPDLOG_ACTIVE_LEVEL SPDLOG_LEVEL_TRACE

#include "spdlog/sinks/basic_file_sink.h"
#include "spdlog/sinks/stdout_color_sinks.h"
#include "spdlog/spdlog.h"

#include <array>       // для std::array
#include <atomic>      // для std::atomic
#include <chrono>      // для std::chrono
#include <filesystem>  // для std::filesystem
#include <format>      // для std::format (C++20)
#include <fstream>     // для std::ofstream
#include <iostream>    // для std::cerr
#include <map>
#include <memory>           // для std::unique_ptr, std::shared_ptr
#include <print>            // для std::print (C++23)
#include <queue>            // для std::queue
#include <source_location>  // для std::source_location (C++20)
#include <stdexcept>        // для std::runtime_error
#include <string>           // для std::string
#include <thread>           // для std::thread
#include <utility>          // для std::pair
#include <utility>          // для std::move
#include <vector>           // для std::vector
