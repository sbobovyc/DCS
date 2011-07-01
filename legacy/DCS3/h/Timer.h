// Timer.h - simple wrapper around gettimeofday
//
// Seth Warn

#ifndef TIMER_H
#define TIMER_H

#include <sys/time.h>

namespace DCS {

class Timer
{
public:
    Timer() : running(false), start_time(0), total_time(0) { }
    void start();
    void stop();
    void reset();
    double read() const;

private:
    double now() const;
    bool running;
    double start_time;
    double total_time;
};

inline void Timer::reset()
{
    total_time = 0;
}

inline void Timer::start()
{
    if (running) return;

    running = true;
    start_time = now();
}

inline void Timer::stop()
{
    if (running)
        total_time += now() - start_time;

    running = false;
}

inline double Timer::read() const
{
    return ( running ? total_time + (now() - start_time) : total_time);
}

inline double Timer::now() const
{
    timeval t;
    gettimeofday(&t, 0);
    return t.tv_sec + t.tv_usec/1000000.0;
}

}
#endif

