
/*
@File name: labrador_adc.c
@Author Igor Ruschi Andrade E Lima <igor.lima@lsitec.org.br>
@LSITEC
*/

#ifndef __LABRADOR_ADC_H

#include "labrador_adc.h"

#endif

/*
return 10bits adc value [0 - 1023] 
*/

int adc_open(char *adc_file){
	return open(adc_file, O_RDONLY);
}

int adc_close(int fd){
	close(fd);
}

int adc_read(int fd){
	int bytes = 0, i = 0, j = 0;
	char buffer[ADC_BUFFER_SIZE];
	char adc_val[5];
	int ret;
	
	if(fd < 0){
		printf("ERROR: adc file descriptor is invalid\n");
	}
	else{
		bytes = read(fd, buffer, sizeof(buffer));
		lseek(fd,0,SEEK_SET);
		if(bytes <= 0){
			printf("WARNING: adc bytes read = %d\n", bytes);
		}
	}
	
	while(buffer[i] != ' ') i++;//discart timestamp for while
	i++;
	
	while(buffer[i] != '\0'){
		adc_val[j] = buffer[i];
		i++;
		j++;
	}
	
	adc_val[4]='\0';

	//printf("adc_read = %d\n", atoi(adc_val));
	ret = atoi(adc_val);
	return ret;
}


