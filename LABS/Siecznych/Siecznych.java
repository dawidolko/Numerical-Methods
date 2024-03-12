package Siecznych;

import java.util.function.DoubleFunction;

public class Siecznych {

    public static int iteracje = 0;
    public static final double DX = Math.pow(10, -7);

    public static DoubleFunction<Double> pochodna(DoubleFunction<Double> f) {
        return (x) -> (f.apply(x + DX) - f.apply(x)) / DX;
    }

    public static double newton(DoubleFunction<Double> f, double epsilon, double a, double b) {
        if (f.apply(a) * f.apply(b) < 0) {
            if (f.apply(a) * pochodna(pochodna(f)).apply(a) > 0) {
                return newton_rek(f, epsilon, a, b);
            } else {
                return newton_rek(f, epsilon, b, a);
            }
        } else {
            throw new IllegalArgumentException();
        }
    }

    private static double newton_rek(DoubleFunction<Double> f, double epsilon, double xminus1, double xminus2) {
        double xk2 = xminus1;
        double xk = xminus1 - (f.apply(xminus1) / (f.apply(xminus2) - f.apply(xminus1))) * (xminus2 - xminus1);
        double yk = f.apply(xk);

        while (Math.abs(yk) > epsilon) {
            iteracje++;
            return newton_rek(f, epsilon, xk, xk2);
        }

        return xk;
    }

    public static void main(String[] args) {
        DoubleFunction<Double> funkcja = (x) -> (x + 1) * Math.pow(x - 1, 4); //wzór funkcji
        
        //newton(funkcja, epsilon, lewy koniec przedziału, prawy koniec przedziału)
        System.out.println("wynik: " + newton(funkcja, Math.pow(10, -7), -1.5, -0.75));
        System.out.println("iteracje: " + iteracje);
    }

}
