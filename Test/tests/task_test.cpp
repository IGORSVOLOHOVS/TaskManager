
#include "gtest/gtest.h"
#include <task.hpp>

class TaskTest : public ::testing::Test {
protected:
    void SetUp() override { SPDLOG_INFO("-----------------------------------------------------"); }
    void TearDown() override { SPDLOG_INFO("-----------------------------------------------------"); }
};

TEST_F(TaskTest, TaskTest_True) {
    ASSERT_TRUE(true);

    SPDLOG_INFO("OK");
}
