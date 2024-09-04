/* Créditos: https://github.com/sergioshimura/Labrador-ADC */
#ifndef __CANINOS_TIME_H
#include "caninos_time.h"
#endif

/* msleep(): Sleep for the requested number of milliseconds. */
int msleep(long msec)
{
    struct timespec ts;
    int res;
    int i = 0;

    if (msec < 0)
    {
        errno = EINVAL;
        return -1;
    }

    ts.tv_sec = msec / 1000;
    ts.tv_nsec = (msec % 1000) * 1000000;

    do {
	if(i == 5){//try five times, otherwise break
		printf("[ERROR] Could not sleep for time requested\n");
		break;
	}
        res = nanosleep(&ts, &ts);
	i++;
    } while (res && (errno == EINTR));

    return res;
}


void delay (unsigned int howLong)
{
    struct timespec sleeper, dummy ;

    sleeper.tv_sec  = (time_t)(howLong / 1000) ;
    sleeper.tv_nsec = (long)(howLong % 1000) * 1000000 ;

    nanosleep (&sleeper, &dummy) ;
}
