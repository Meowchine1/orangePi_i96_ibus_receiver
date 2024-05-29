#include <wiringPi.h>

// 8, PA13 -- TX; 10, PA14 -- RX

int main (void)
{
	int i = 0;
	unsigned char gpio_num = 0;

	wiringPiSetup();

	gpio_num = getGpioNum();
	if (-1 == gpio_num)
		printf("Failed to get the number of GPIO!\n");

	for (i = 0; i < gpio_num; i++)
		pinMode (i, OUTPUT) ;

	for ( ;; )
	{
		for (i = 0; i < gpio_num; i++)
			digitalWrite (i, HIGH);	// On
		delay (2000);

		for (i = 0; i < gpio_num; i++)
			digitalWrite (i, LOW);	// Off
		delay (2000);
	}

	return 0;
}