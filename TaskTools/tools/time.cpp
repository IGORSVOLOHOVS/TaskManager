#include "time.hpp"

namespace tools {
    Time::Time() noexcept
    {
        data_.tm = std::chrono::duration_cast<std::chrono::milliseconds>(
            std::chrono::system_clock::now().time_since_epoch()
        ).count();
    }

    Time::Time(const TimeData &data) noexcept : data_(data) {}
    Time::Time(TimeData &&data) noexcept : data_(std::move(data)) {}

    Time::Time(const Time &other) noexcept : data_(other.data_) {}
    Time::Time(Time &&other) noexcept : data_(std::move(other.data_)) {}

    Time &Time::operator=(const Time &other) noexcept 
    {
        if (this != &other) 
        {
            this->data_ = other.data_;
        }
        return *this;
    }

    Time &Time::operator=(Time &&other) noexcept 
    {
        if (this != &other) 
        {
            this->data_ = std::move(other.data_);
        }
        return *this;
    }

    Time::~Time()
    {
    }

    std::string Time::GetTime() const
    {
        return ParseToNormalFormat(data_.tm);
    }

    size_t Time::ParseToNumber(std::string time) {
        std::istringstream ss(time);
        std::tm tm = {};
        ss >> std::get_time(&tm, "%Y-%m-%d %H:%M:%S");
        
        // Correct for time zone offset
        std::time_t timeT = std::mktime(&tm); // Time in local timezone
        gmtime_s(&tm, &timeT); // Convert to UTC (Windows

        size_t timestamp = std::mktime(&tm) * 1000.0; 

        std::string millisecondsStr;
        if (ss.peek() == '.') {
            ss.ignore(); // Skip '.'
            std::getline(ss, millisecondsStr); 
            timestamp += std::stoi(millisecondsStr); 
        }

        return timestamp;
    }

    std::string Time::ParseToFloating(size_t time) {
        std::size_t high_tm = time / 1000;
        std::size_t low_tm = time % 1000;

        std::stringstream ss;
        ss << high_tm << '.' << std::setfill('0') << std::setw(3) << low_tm;

        return ss.str();
    }

    std::string Time::ParseToNormalFormat(size_t time) {
        std::time_t timeT = time / 1000; // Convert to seconds

        // Local time
        std::tm localTime;
        localtime_s(&localTime, &timeT);

        // Format into string
        std::stringstream ss;
        ss << std::put_time(&localTime, "%Y-%m-%d %H:%M:%S"); 
        ss << '.' << std::setfill('0') << std::setw(3) << time % 1000;

        return ss.str();
    }

    const TimeData &Time::GetData() const noexcept 
    {
        return this->data_;
    }
   
    TimeData &Time::GetData() noexcept 
    {
        return this->data_;
    }
    
    Time &Time::SetData(const TimeData &data) noexcept 
    {
        this->data_ = data;
        return *this;
    }

    Time &Time::SetData(TimeData &&data) noexcept 
    {
        this->data_ = std::move(data);
        return *this;
    }
} 
