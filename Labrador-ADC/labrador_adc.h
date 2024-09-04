/*
@File name: adc.h
@Author Igor Ruschi Andrade E Lima <igor.lima@lsitec.org.br>
@LSITEC
*/

#ifndef __LABRADOR_ADC_H

#define __LABRADOR_ADC_H

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdint.h>
#include <fcntl.h>

#endif


#define ADC_BUFFER_SIZE 500 //size of adc buffer in bytes


int adc_open(char *adc_file);
int adc_close(int fd);
int adc_read(int fd);
