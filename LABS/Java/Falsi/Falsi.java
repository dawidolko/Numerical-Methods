
package Falsi;


public class Falsi {

    public static double wartosc(double x)
    {
        return (x+1)*Math.pow((x-1),4); //wzór funkcji
    }

    
    public static void main(String[] args) {
        double epsilon = Math.pow(10, -7); //margines błędu
        double a = -1.5; // lewy koniec przedziału
        double b = -0.75; // prawy koniec przedziału
        int iteracje = 0;
        double x2=0;
        
        double x1 = a - (wartosc(a)/(wartosc(b)-wartosc(a))) * (b-a);
        
        if(wartosc(x1) * wartosc(a) < 0)
        {
            while (true)
            {
                x2 = x1 - (wartosc(x1)/(wartosc(a)-wartosc(x1)) * (a-x1));
                iteracje++;
                
                if(Math.abs(wartosc(x2)) <= epsilon) break;
                else x1 = x2;
            }
            
        }
        else if(wartosc(x1) * wartosc(b) < 0)
        {
            while (true)
            {
                x2 = x1 - (wartosc(x1)/(wartosc(b)-wartosc(x1)) * (b-x1));
                iteracje++;
                
                if(Math.abs(wartosc(x2)) <= epsilon) break;
                else x1 = x2;
            }
        }
        
        System.out.println("liczba iteracji: "+iteracje);
        System.out.println("wynik: "+x2);
        
    }
    
}
