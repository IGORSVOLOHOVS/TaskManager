#pragma once

#include <iostream>

#include <fcntl.h>
#include <cstring>
#include <unistd.h>



#include <chrono>
#include <thread>

#include "log.hpp"
#include "parralel.hpp"
#include "io.hpp"

#ifdef _WIN64
    #include <winsock2.h>
    #include <ws2tcpip.h>
    #pragma comment(lib, "ws2_32.lib")
#else
    #include <mqueue.h>
    
    #include <netinet/in.h>
    #include <sys/socket.h>
    #include <sys/types.h>
    #include <arpa/inet.h>
    #include <unistd.h>
#endif


constexpr size_t BUFFER_SIZE = 8192;

struct ConnectorData
{
    ConnectorData(int argc, char **argv) : log(argc, argv) {}

    Log log;
};

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

#ifdef __linux__ 
    class Connector
    {
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
                speak(Command::SIMPLE, message.c_str());
            }
        }

        AsyncFunction(listen, void)
            AsyncFunction(speak, void) private : mqd_t sender;
        mqd_t receiver;

        ConnectorData data;
    };
#endif

struct Network
{
    std::string ip;
    int port;
};

class ServerTCP
{
public:
    ServerTCP(Network network, ConnectorData data = {0, nullptr}) : data(data), network(network)
    {
        #ifdef _WIN64
            WSADATA wsaData;
            int iResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
            if (iResult != 0)
            {
                printf("WSAStartup failed: %d\n", iResult);
                throw std::runtime_error("Failed to start WSA");
            }
        #endif

        // Creating socket file descriptor
        if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
        {
            perror("socket failed");
            exit(EXIT_FAILURE);
        }

        // Forcefully attaching socket to the port 8080
        #ifdef _WIN64
            if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, (char *)&opt, sizeof(opt)) < 0)
            {
                perror("setsockopt");
                exit(EXIT_FAILURE);
            }
        #else
            if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt)))
            {
                perror("setsockopt");
                exit(EXIT_FAILURE);
            }
        #endif

        address.sin_family = AF_INET;
        address.sin_port = htons(network.port);
        address.sin_addr.s_addr = inet_addr(network.ip.c_str());

        // Forcefully attaching socket to the port 8080
        if (bind(server_fd, (struct sockaddr *)&address,
                 sizeof(address)) < 0)
        {
            perror("bind failed");
            exit(EXIT_FAILURE);
        }
        if (::listen(server_fd, 3) < 0)
        {
            perror("listen");
            exit(EXIT_FAILURE);
        }
    }

    ~ServerTCP()
    {
        #ifdef _WIN64
            closesocket(server_fd);
            WSACleanup();
        #else
            close(server_fd);
        #endif
    }

    void listen(size_t period_ms = 1000)
    {
        #ifdef _WIN64
            SOCKET new_socket;
        #else
            int new_socket;
        #endif

        if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t *)&addrlen)) < 0)
        {
            perror("accept");
            exit(EXIT_FAILURE);
        }
        while(true) {
            #ifdef _WIN64
                if((valread = recv(new_socket, buffer, 1024 - 1, 0)) == 0) {
                    throw std::runtime_error("Failed to read message");
                }
            #else
                if((valread = read(new_socket, buffer, 1024 - 1)) == 0) {
                    throw std::runtime_error("Failed to read message");
                }
            #endif

            buffer[valread] = '\0';

            ParsedResponse response = parse(buffer);

            char *result = execute(response);
            if (result)
            {
                if(send(new_socket, result, strlen(result), 0) == -1) {
                    throw std::runtime_error("Failed to send message");
                }
            }

            std::this_thread::sleep_for(std::chrono::milliseconds(period_ms));
        }    
        close(new_socket);
    }

private:
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
            return "OK";
        }
        case Command::VERSION:
        {
            std::cout << "Version 1.0.0\n";
            return "OK";
        }
        case Command::HELP:
        {
            std::cout << "Usage: ./main [OPTION]...\n";
            std::cout << "1 Options:\n";
            std::cout << "2   -h, --help\t\t\tDisplay this information\n";
            std::cout << "3   -v, --version\t\t\tDisplay the version\n";
            return "OK";
        }
        default:
            std::cerr << "Unknown command: " << static_cast<unsigned int>(response.command) << '\n';
            return nullptr;
        }

        return nullptr;
    }

#ifdef _WIN64
    SOCKET server_fd;
#else
    int server_fd;
#endif

    long valread;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buffer[1024] = {0};

    Network network;
    ConnectorData data;
};

class ClientTCP
{
public:
    ClientTCP(Network network, ConnectorData data = {0, nullptr}) : data(data), network(network)
    {
        #ifdef _WIN64
            WSADATA wsaData;
            int iResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
            if (iResult != 0)
            {
                printf("WSAStartup failed: %d\n", iResult);
                throw std::runtime_error("Failed to start WSA");
            }
        #endif

        if ((client_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
            printf("\n Socket creation error \n");
            throw std::runtime_error("Failed to create socket");
        }
    
        serv_addr.sin_family = AF_INET;
        serv_addr.sin_port = htons(network.port);
    
        // Convert IPv4 and IPv6 addresses from text to binary
        // form
        #ifdef _WIN64
            if (inet_pton(AF_INET, network.ip.c_str(), &serv_addr.sin_addr) <= 0) {
                throw std::runtime_error("Invalid address/ Address not supported");
            }
        #else
            if (inet_pton(AF_INET, network.ip.c_str(), &serv_addr.sin_addr) != 0) {
                throw std::runtime_error("Invalid address/ Address not supported");
            }
        #endif

        if ((status = connect(client_fd, (struct sockaddr*)&serv_addr, sizeof(serv_addr))) < 0) {
            throw std::runtime_error("Connection Failed");
        }
    }

    ~ClientTCP()
    {
        #ifdef _WIN64
            closesocket(client_fd);
            WSACleanup();
        #else
            close(client_fd);
        #endif
    }

    std::string speak(Command command, const char *data = "")
    {
        char *request = new char[strlen(data) + 2];
        request[0] = static_cast<unsigned int>(command) + '0';
        strcpy(request + 1, data);
        
        if(send(client_fd, request, strlen(request), 0) == -1) {
            throw std::runtime_error("Failed to send message");
        }

        if((valread = read(client_fd, buffer, 1024 - 1) == 0)) {
            throw std::runtime_error("Failed to read message");
        }  

        return buffer;
    }

    std::string speak()
    {
        std::string message;
        while (true)
        {
            message = read("Enter a word: ");
            if (message == "!q")
            {
                break;
            }
            std::cout << speak(Command::SIMPLE, message.c_str()) << '\n';
        }
    }

private:
    int client_fd;
    long valread;
    struct sockaddr_in serv_addr;
    char buffer[1024] = {0};
    int status;

    Network network;
    ConnectorData data;
};
