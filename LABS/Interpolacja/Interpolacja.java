
package Interpolacja;


public class Interpolacja {

    public static String lagrange(double x1, double y1, double x2, double y2, double x3, double y3) {
        String w1 = y1+"(x-"+x2+")(x-"+x3+")/("+((x1-x2)*(x1-x3))+")";
        String w2 = y2+"(x-"+x1+")(x-"+x3+")/("+((x2-x1)*(x2-x3))+")";
        String w3 = y3+"(x-"+x1+")(x-"+x2+")/("+((x3-x1)*(x3-x2))+")";

        String langrange = w1+" + "+w2+" + "+w3;
        return langrange;
    }

    public static void main(String[] args) {
        System.out.println(lagrange(1, 5, 2, 7, 3, 6));
    }
    
}
