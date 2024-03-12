
package Prostokaty;


public class Prostokaty {

    public static double wartosc(double x)
    {
        return Math.pow(x,2); //wzór funkcji
    }  
    
    public static void main(String[] args) {
        double a = -1; //lewy koniec przedziału
        double b = 1; //prawy koniec przedziału
        double iteracje = 50; //liczba możliwych iteracji
        
        double x = (b-a) / iteracje;
        
        double suma = 0;
   
        for(int i=0; i<iteracje; i++)
        {
            suma += x* wartosc(a+i*x);
        }
        
        System.out.println("Pole: "+suma);
        
    }
    
}
