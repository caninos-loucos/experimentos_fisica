/*
é preciso da biblioteca alsa/asound 
sudo apt install libasound2-dev
*/

#include <math.h>
#include <stdlib.h>
#include <stdio.h>

#include "Labrador-ADC/labrador_adc.h"
#include "Labrador-ADC/caninos_time.h"

#include <time.h>
#include <signal.h>
#include <alsa/asoundlib.h>


#define SAMPLE_RATE 48000
#define PI 3.14159265

volatile int keep_playing = 1;

void handle_signal(int signal){
	keep_playing = 0;
}

int adc_get_rms_value(int fd, int n){
	int i = 0;
	int ret;
	int aux_i;
	double aux_d;
	while(i<n){
		aux_i = adc_read(fd);
		aux_d += pow(aux_i, 2);
		i++;
	}
	aux_d = aux_d / i;
	aux_d = sqrt(aux_d);
	aux_i = (int)(aux_d);
	return aux_i;
}

void generate_tone(snd_pcm_t *handle, int freq) {
        int16_t buffer[SAMPLE_RATE];

        for (int i = 0; i < SAMPLE_RATE; i++) {
                buffer[i] = 32767 * sin(2.0 * PI * freq * i / SAMPLE_RATE);
        }
	snd_pcm_writei(handle, buffer, SAMPLE_RATE);
}

int main(){
	//set default location for adc0
        char adc_file_path[25] = "/sys/kernel/auxadc/adc0";
        //create the file descriptor for adc
        int adc_fd;
        //create a variable to store the adc data
        int data;
        //open adc file descriptor
        adc_fd = adc_open(adc_file_path);

	signal(SIGINT, handle_signal);
	snd_pcm_t *handle;
        snd_pcm_open(&handle, "default", SND_PCM_STREAM_PLAYBACK, 0);
        snd_pcm_set_params(handle, SND_PCM_FORMAT_S16_LE, SND_PCM_ACCESS_RW_INTERLEAVED, 1, SAMPLE_RATE, 1, 500000);
        int freq;


	if(adc_fd < 0){
		printf("[ERROR]: Fail to open ADC FILE ret = %d\n", adc_fd);
		return -1;
	}
	int freq_a = 0;
	while(keep_playing){
		data = adc_get_rms_value(adc_fd, 5);
		// variar aqui para obter maiores valores de freq, +100, +200
		freq = ((data) * 200 / 1023);
		printf("Frequencia(Hz): %d, ADC_DATA: %d\n", freq, data);
		generate_tone(handle, freq);
		sleep(0.1);
	}
	snd_pcm_close(handle);
	adc_close(adc_fd);

	return 0;
}
