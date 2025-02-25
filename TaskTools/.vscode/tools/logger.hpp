#pragma once

#include "../task.hpp"

namespace tools
{
    enum class Level : uint8_t
    {
        INF = 0,
        WARN,
        ERR
    };

    struct LoggerData
    {
        std::fstream file = {};
        std::mutex mutex = {};
        int count = {};
        int big_count = {};

        SOCKET sendSocket = {};
        sockaddr_in sendAddr = {};
        sockaddr_in recvAddr = {};
        int iResult = {};
        WSADATA wsaData = {};
    };

    class Logger
    {
    private:
        LoggerData data_;
    public:
        void Log(Level level = Level::INF, const std::string& message = "");
        static Logger& GetLogger();

        const LoggerData &GetData() const noexcept;
        LoggerData &GetData() noexcept;
    private:
        Logger();
        ~Logger();
    };
}
