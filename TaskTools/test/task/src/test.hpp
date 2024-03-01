#pragma once
#include <gtest/gtest.h>

TEST(Test1, TestName) {
    if(!TEST1)
        GTEST_SKIP();

    EXPECT_STRNE(ARG["test1"][0].as<std::string>().c_str(), "test1");
    EXPECT_EQ(ARG["test1"][1].as<int>(), 1);
}
TEST(Test2, TestName) {
    if(!TEST2)
        GTEST_SKIP();

    EXPECT_STRNE(ARG["test2"][0].as<std::string>().c_str(), ARG["test2"][1].as<std::string>().c_str());
}

namespace test
{
    inline int run(int argc = 1, std::vector<char*> argv = {(char*)""}){
        ::testing::InitGoogleTest(&argc, argv.data());
        return RUN_ALL_TESTS();
    }
} // namespace test
