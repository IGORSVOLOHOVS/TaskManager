#include "logger.hpp"

namespace tools {

    Logger::Logger(): data_()
    {
        // create log directory
        if(!std::filesystem::exists("log")){
            std::filesystem::create_directory("log");
        }

        data_.file.open("log/" + std::to_string(Time().GetData().tm) + ".log", std::ios::out | std::ios::app);
        if (!data_.file.is_open())
        {
            throw std::runtime_error("Logger: Failed to open log file");
        }

        // Initialize Winsock
        data_.iResult = WSAStartup(MAKEWORD(2,2), &data_.wsaData);
        if (data_.iResult != 0) {
            throw std::runtime_error("Logger: WSAStartup failed with error: " + std::to_string(data_.iResult));
        }

        data_.recvAddr.sin_family = AF_INET;
        data_.recvAddr.sin_port = htons(514); // Стандартный порт для syslog
        inet_pton(AF_INET, "127.0.0.1", &data_.recvAddr.sin_addr.S_un.S_addr); // Локальный адрес

        data_.sendSocket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
        if (data_.sendSocket == INVALID_SOCKET) {
            WSACleanup();
            throw std::runtime_error("Logger: socket failed with error: " + std::to_string(WSAGetLastError()));
        }
    }
    Logger::~Logger()
    {
        data_.file.close();

        closesocket(data_.sendSocket);
        WSACleanup();
    }

    /**
     * @brief    Log messages    
     * 
     * @details  This function is used to log messages. It writes messages to a 
     *           file and sends them to the syslog server.  
     *
     * @param[in]  level - Level of the message: INF, WARN, ERR
     * @param[in]  message - Message to log
     *
     * @return
     * 
     * @warning  This function is not thread-safe.
     *  
     * @todo     use console output
     * 
     * @see      LoggerData
    */
    void Logger::Log(Level level, const std::string& message)
    {
        std::string level_str = "ID (" + std::to_string(data_.big_count * 100000 + data_.count) + ") [ " + Time().GetTime() + " ]: ";

        switch (level)
        {
        case Level::INF:
            level_str += "INFO";
            break;
        case Level::WARN:
            level_str += "WARNING";
            break;
        case Level::ERR:
            level_str += "ERROR";
            std::cout << std::endl << level_str << " - " << message << std::endl;
            break;
        default:
            level_str += "UNKNOWN";
            break;
        }

        level_str = level_str + " - " + message;
        data_.mutex.lock();
        // Запись в файл
        data_.file << level_str  << std::endl;

        // Отправка данных
        data_.iResult = sendto(data_.sendSocket, level_str.c_str(), (int)level_str.length(), 0, (SOCKADDR*)&data_.recvAddr, sizeof(data_.recvAddr));
        if (data_.iResult == SOCKET_ERROR) {
            closesocket(data_.sendSocket);
            WSACleanup();
            throw std::runtime_error("Loggerger: sendto failed with error: " + std::to_string(WSAGetLastError()));
        }
        data_.count++;

        if (data_.count >= 100000)
        {
            data_.file.close();
            data_.file.open("log/" + std::to_string(Time().GetData().tm) + ".log", std::ios::out | std::ios::app);
            data_.count = 0;
            data_.big_count++;
        }
        data_.mutex.unlock();
    }

    Logger& Logger::GetLogger()
    {
        static Logger logger;
        return logger;
    }

    const LoggerData &Logger::GetData() const noexcept 
    {
        return this->data_;
    }
   
    LoggerData &Logger::GetData() noexcept 
    {
        return this->data_;
    }
} 
