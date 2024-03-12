
package Bisekcja;


public class Bisekcja {

    
    static int licznik = 0;
    
    static double bisekcja(double a, double b) {
        double x = (a+b)/2;

        double fx = (x+1)*Math.pow((x-1),4); //wzór funkcji

        if(Math.abs(a-b) > Math.pow(10,-8)) { //Math.pow(10,-8) dokładność do jakiej liczymy
            if (fx == 0)
                return x;
            else {
                licznik++;

                double fa = (a + 1) * Math.pow((a - 1), 4);
                double fb = (a + 1) * Math.pow((a - 1), 4);

                if (fa * fx < 0) {
                    b = x;
                    return bisekcja(a, b);
                } else {
                    a = x;
                    return bisekcja(a, b);
                }
            }
        } else {
            return x;
        }
    }

    
    public static void main(String[] args) {
        System.out.println(bisekcja(-1.5, -0.75)); //przedział gdzie znajduje się pierwiastek
        System.out.println("Licznik iteracji: " + licznik);
    }
    
}
