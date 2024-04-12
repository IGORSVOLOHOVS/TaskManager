#include <iostream>
#include <mqueue.h>
#include <fcntl.h>
#include <cstring>
#include <unistd.h>

#include <chrono>
#include <thread>

#include "log.hpp"
#include "parralel.hpp"

constexpr size_t BUFFER_SIZE = 8192;

struct ConnectorData
{
    ConnectorData(int argc, char **argv) : log(argc, argv) {}

    Log log;
};

class Connector
{
public:
    enum class Command : unsigned int
    {
        SIMPLE = 0,
        VERSION,
        HELP
    };

    struct ParsedResponse
    {
        Command command;
        char *data;
    };

private:
    void send(const char *data)
    {
        if (mq_send(sender, data, strlen(data), 0) == -1)
        {
            perror("mq_send");
            throw std::runtime_error("Failed to send message");
        }
    }

    char *receive()
    {
        static char buffer[BUFFER_SIZE];
        unsigned int priority;
        ssize_t bytes_received = mq_receive(receiver, buffer, sizeof(buffer), &priority);
        if (bytes_received == -1)
        {
            perror("mq_receive");
            throw std::runtime_error("Failed to receive message");
        }
        buffer[bytes_received] = '\0'; // Null-terminate
        return buffer;
    }

    ParsedResponse parse(char *response)
    {
        ParsedResponse parsed_response;
        parsed_response.command = static_cast<Command>(response[0] - '0');
        parsed_response.data = response + 1;
        return parsed_response;
    }

    char *execute(ParsedResponse response)
    {
        switch (response.command)
        {
        case Command::SIMPLE:
        {
            std::cout << response.data << '\n';
            break;
        }
        case Command::VERSION:
        {
            std::cout << "Version 1.0.0\n";
            break;
        }
        case Command::HELP:
        {
            std::cout << "Usage: ./main [OPTION]...\n";
            std::cout << "1 Options:\n";
            std::cout << "2   -h, --help\t\t\tDisplay this information\n";
            std::cout << "3   -v, --version\t\t\tDisplay the version\n";
            break;
        }
        default:
            std::cerr << "Unknown command: " << static_cast<unsigned int>(response.command) << '\n';
            return nullptr;
        }

        return nullptr;
    }

public:
    Connector(const char *this_exe_name, const char *other_exe_name, ConnectorData data = {0, nullptr}) : data(data)
    {
        sender = mq_open(this_exe_name, O_CREAT | O_RDWR, 0666, nullptr);
        if (sender == -1)
        {
            perror("mq_open_receiver");
            throw std::runtime_error("Failed to open message queue: mq_open_receiver = " + std::to_string(sender));
        }

        receiver = mq_open(other_exe_name, O_CREAT | O_RDWR, 0666, nullptr);
        if (receiver == -1)
        {
            perror("mq_open_receiver");
            throw std::runtime_error("Failed to open message queue: mq_open_receiver = " + std::to_string(receiver));
        }
    }

    ~Connector()
    {
        mq_close(sender);
        mq_close(receiver);
    }

    void listen(size_t period_ms = 1000)
    {
        ParsedResponse response;
        char *result = nullptr;
        while (true)
        {
            response = parse(receive());
            result = execute(response);

            if (result)
            {
                send(result);
                free(result);
            }

            std::this_thread::sleep_for(std::chrono::milliseconds(period_ms));
        }
    }

    void speak(Command command, const char *data = "")
    {
        char *request = new char[strlen(data) + 2];
        request[0] = static_cast<unsigned int>(command) + '0';
        strcpy(request + 1, data);
        send(request);
    }
    void speak()
    {
        std::string message;
        while (true)
        {
            message = read("Enter a word: ");
            if (message == "!q")
            {
                break;
            }
            speak(Connector::Command::SIMPLE, message.c_str());
        }
    }

    AsyncFunction(listen, void)
        AsyncFunction(speak, void) private : mqd_t sender;
    mqd_t receiver;

    ConnectorData data;
};
