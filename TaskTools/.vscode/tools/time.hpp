#pragma once

#include "../task.hpp"

namespace tools
{
    struct TimeData
    {
        size_t tm;
    };

    class Time
    {
    private:
        TimeData data_;
    public:
        explicit Time() noexcept;
        explicit Time(const TimeData &data) noexcept;
        explicit Time(TimeData &&data) noexcept;

        Time(const Time &other) noexcept;
        Time(Time &&other) noexcept;
        Time &operator=(const Time &other) noexcept;
        Time &operator=( Time &&other) noexcept;
        ~Time();

        static size_t ParseToNumber(std::string time); 
        static std::string ParseToNormalFormat(size_t time);
        static std::string ParseToFloating(size_t time);

        std::string GetTime() const;
        const TimeData &GetData() const noexcept;
        TimeData &GetData() noexcept;
        Time &SetData(const TimeData &data) noexcept;
        Time &SetData(TimeData &&data) noexcept;

        bool operator==(const Time &other) const noexcept;
        bool operator<(const Time &other) const noexcept;
    };
}
