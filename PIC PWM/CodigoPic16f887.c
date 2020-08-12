//Vladimir Alfaro - Universidad Sim�n Bol�var - 09/08/2020 
// Con este c�digo se pretende dise�ar el algoritmo de control MMPT para un microcontrolador PIC16F887
//-----------------------------------------------------------------------------------------------------

#include <16f887.h>
#device ADC = 10     // Conversor Anal�gico Digital con  10 bits de resoluci�n
#fuses XT, NOWDT, NOPROTECT, NOLVP, PUT, BROWNOUT, INTRC_IO
#use delay(clock=4000000)
#include <LCD.C>
#byte PORTA = 5
#byte PORTD = 8

int Timer2=9, PostCaler=1, duty = 20; // Preescaler;
//Para 25KHz, el valor para modular el DutyCycle ser� 40 = 100%
//Por lo tanto duty = 20 implica un DutyCycle de 50%
float V1, V2=0, I1, I2=0, P1, P2;

void main(){
    
    //Para la PWM de 1Khz es necesario un Timer2=249, cuando la frecuencia del cristal es de 4Mhz,
    //el PostCaler=1 y Preescaler=4, en base a la siguiente f�rmula:
    // Timer2 = (Td*fxtal/(4*Preescaler-PostCaler)) - 1
    //Timer2 = 10;                                    //Para este valor del Timer se puede alcanzar una f=25KHz
    //PostCaler = 1;                                  // S�lo puede tomar valores de 1, 4 o 16, igual que el preescaler
    //Preescaler = 4;
    set_tris_a(0b00000011);                           //Configuro los pines RA0 y RA1 como entradas
    setup_timer_2(t2_div_by_4, Timer2, PostCaler);    //Configuraci�n del timer 2, preescaler=4, timer2=9, postcaler=1
    setup_ccp1(ccp_pwm);                              //Con esto estamos configurando el modo PWM en la salida ccp1 (pin RC2)
    setup_adc_ports(all_analog);                      //Todos los puertos analogicos quedaran como analogicos
    setup_adc(adc_clock_internal);                    //Configuramos la velocidad del ADC
    lcd_init();
    lcd_putc("\f");
    
    while(1){
    
       set_pwm1_duty(duty);         //Se confiugura el dutycycle de la PWM
       
       set_adc_channel(0);          //Selecciono el canal 0 (RA0)
       delay_us(50);                //Retardo de 50 us para leer la data
       V1=read_adc();               //Guardo en bits el voltaje leido por el canal 0
       V1 = V1*0.0048828125;        //Valor real del voltaje medido
       
       set_adc_channel(1);          //Selecciono el canal 1 (RA1)
       delay_us(50);                //Retardo de 50 us para leer la data
       I1=read_adc();               //Guardo en bits la corriente leida por el canal 1
       I1= I1*0.0048828125;         //Valor real del voltaje medido
   /*-----------Algoritmo MPPT----------*/
       P1 = V1*I1;
       P2 = V2*I2;
       
       if(P1 == P2){
         return;
       }
       else{
         if(P1 - P2 > 0){
            if(V1 - V2 > 0){
               duty = duty + 1;
            }
            else{
               duty = duty - 1;
            }
         }
         else{
            if(V1 - V2 > 0){
               duty = duty - 1;
            }
            else{
               duty = duty + 1;
            }
         }
       }  
       V2 = V1;
       I2 = I1;
       
       lcd_gotoxy(1,1);                  //Ubiquese en la posicion 1,1
       lcd_putc("El Duty Cycle es:");
       lcd_gotoxy(2,2);                  //Ubiquese en la posicion 2,2
       printf(lcd_putc,"D = %i",duty);   //Muestra el valor numerico de la conversionconversion
       delay_ms(500);
       lcd_putc("\f");                   // Borramos LCD
    }
}
