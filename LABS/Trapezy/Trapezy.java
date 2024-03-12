
package Trapezy;


public class Trapezy {

    public static double wartosc(double x)
    {
        return Math.pow(x,2);  //wzór funkcji
    }
    
    public static void main(String[] args) {
        double a = -1;  //lewy koniec przedziału
        double b = 1; //prawy koniec przediału
        double iteracje = 50; //liczba iteracji
        
        double x = (b-a) / iteracje;
        
        double suma = 0;
        
        for(int i=0; i<iteracje; i++)
        {
            suma += x* (wartosc(a+i*x) + wartosc(a+((i+1)*x))) / 2;
        }
        
        System.out.println("Pole: "+suma);
    }
    
}
