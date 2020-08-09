//Vladimir Alfaro - Universidad Simón Bolívar - 09/08/2020 
// Con este código se pretende diseñar el algoritmo de control MMPT para un microcontrolador PIC16F887
//-----------------------------------------------------------------------------------------------------

#include <16f887.h>
#device ADC = 10     // Conversor Analógico Digital con  10 bits de resolución
#fuses XT, NOWDT, NOPROTECT, NOLVP, PUT, BROWNOUT, INTRC_IO
#use delay(clock=4000000)

int16 duty = 0;
int Timer2, PostCaler;

void main(){
    
    //Para la PWM de 1Khz es necesario un Timer2=249, cuando la frecuencia del cristal es de 4Mhz,
    //el PostCaler=1 y Preescaler=4, en base a la siguiente fórmula:
    // Timer2 = (Td*fxtal/(4*Preescaler-PostCaler)) - 1
    Timer2 = 249;
    PostCaler = 1;                                  // Sólo puede tomar valores de 1, 4 o 16, igual que el preescaler

    setup_timer_2(t2_div_by_4, Timer2, PostCaler);  // t2_div_by_4 es nuestro Preescaler 
    setup_ccp1(ccp_pwm);                            // Con esto estamos configurando el modo PWM en la salida ccp1
    setup_adc_ports(all_analogs);                   // Todos los puertos analógicos quedarán como analógicos
    setup_adc(adc_clock_internal);                  //Configuramos la velocidad del ADC
    while(1){
        set_adc_channel(0);                         //Configuro RA0 como un canal analógioc de entrada que leeré constantemente
        delay_us(100);
        duty = read_adc();                          //Se guarda el valor leído en Duty (va de 0 a 1024)
        set_pwm1_duty(duty)                         //Se confiugura el dutycycle de la PWM 
    }

}