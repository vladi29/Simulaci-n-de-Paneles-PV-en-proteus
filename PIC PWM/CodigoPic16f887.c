//Vladimir Alfaro - Universidad Sim�n Bol�var - 09/08/2020 
// Con este c�digo se pretende dise�ar el algoritmo de control MMPT para un microcontrolador PIC16F887
//-----------------------------------------------------------------------------------------------------

#include <16f887.h>
#device ADC = 10     // Conversor Anal�gico Digital con  10 bits de resoluci�n
#fuses XT, NOWDT, NOPROTECT, NOLVP, PUT, BROWNOUT, INTRC_IO
#use delay(clock=4000000)

int16 duty = 0;
int Timer2, PostCaler;// Preescaler;
int V1, V2=140, I1=10, I2, P1, P2;

void main(){
    
    //Para la PWM de 1Khz es necesario un Timer2=249, cuando la frecuencia del cristal es de 4Mhz,
    //el PostCaler=1 y Preescaler=4, en base a la siguiente f�rmula:
    // Timer2 = (Td*fxtal/(4*Preescaler-PostCaler)) - 1
    Timer2 = 24;                                     //Para este valor del Timer se puede alcanzar una f=10KHz
    PostCaler = 1;                                  // S�lo puede tomar valores de 1, 4 o 16, igual que el preescaler
    //Preescaler = 4;
    
    setup_timer_2(t2_div_by_4, Timer2, PostCaler);   // Configuraci�n del timer 2 
    setup_ccp1(ccp_pwm);                            // Con esto estamos configurando el modo PWM en la salida ccp1
    setup_adc_ports(all_analog);                    // Todos los puertos analógicos quedarán como analógicos
    setup_adc(adc_clock_internal);                  //Configuramos la velocidad del ADC
    while(1){
        set_adc_channel(0);                         //Configuro RA0 como un canal anal�gico de entrada que leer� constantemente
        delay_us(100);
        duty = read_adc();                          //Se guarda el valor le�do en Duty (va de 0 a 1024)
        set_pwm1_duty(duty);                         //Se confiugura el dutycycle de la PWM 
    }
    //*-------------------------Algoritmo MPPT P&O-------------------------*//
    /*
    set_adc_channel(1);
    delay_us(100);
    V1 = read_adc();
    
    set_adc_channel(2);
    delay_us(100);
    I1 = read_adc();
    
    P1 = V1*I1;
    P2 = V2*I2;
    
    if(P1 == P2){
      return;
    }
    else{
      if(P1 - P2 > 0){
         if(V1 - V2 > 0){
            //No estoy seguro de que poner aqui
         }
         else{
            //No estoy seguro de que poner aqui
         }
      }
      else{
         if(V1 - V2 > 0){
            //*No estoy seguro de que poner aqui
         }
         else{
            //No estoy seguro de que poner aqui
         }
      }
    }
*/    
}