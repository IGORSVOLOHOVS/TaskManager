#include "task/task.hpp"

int main(int argc, char** argv) {
    tools::Time tm;
    std::println(std::cout, "The time is {}", tm.GetTime());

    tools::Parser::Save("TEST_KEY", "TEST_VALUE");
    std::println(std::cout, "The parse value is {}", tools::Parser::Parse("TEST_KEY"));

    static auto& it = tools::Logger::GetLogger();
    it.Log(tools::Level::INF, "All is work!");
    std::println(std::cout, "All is works!");
    return 0;
}
