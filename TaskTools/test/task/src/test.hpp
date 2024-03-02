#pragma once
#include "config.hpp"

#include <gtest/gtest.h>

TEST(Test1, TestName) {
    if(!RUNTEST1)
        GTEST_SKIP();

    std::string ARG1 = ARG["test1"][0].as<std::string>();
    int ARG2 = ARG["test1"][1].as<int>();

    EXPECT_STRNE(ARG1.c_str(), "test");
    EXPECT_EQ(ARG2, 1);
}
TEST(Test2, TestName) {
    if(!RUNTEST2)
        GTEST_SKIP();

    std::string ARG1 = ARG["test2"][0].as<std::string>();
    std::string ARG2 = ARG["test2"][1].as<std::string>();
    
    EXPECT_STRNE(ARG1.c_str(), ARG2.c_str());
}

namespace test
{
    inline int run(int argc = 1, std::vector<char*> argv = {(char*)""}){
        ::testing::InitGoogleTest(&argc, argv.data());
        return RUN_ALL_TESTS();
    }
} // namespace test
