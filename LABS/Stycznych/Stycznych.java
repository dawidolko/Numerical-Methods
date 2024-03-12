package Stycznych;

import java.util.function.DoubleFunction;

public class Stycznych {

    public static int iteracje = 0;
    public static final double dx = Math.pow(10, -8);

    public static DoubleFunction<Double> pochodna(DoubleFunction<Double> f) {
        return (x) -> (f.apply(x + dx) - f.apply(x)) / dx;
    }

    public static double newton(DoubleFunction<Double> f, double epsilon, double a, double b) {
        if (f.apply(a) * f.apply(b) < 0 && f.apply(a) * pochodna(pochodna(f)).apply(a) > 0) {
            return newton(f, epsilon, a);
        } else {
            throw new IllegalArgumentException();
        }
    }

    private static double newton(DoubleFunction<Double> f, double epsilon, double xminus1) {
        iteracje++;
        double xk = xminus1 - (f.apply(xminus1) / pochodna(f).apply(xminus1));
        double yk = f.apply(xk);
        if (Math.abs(yk) < epsilon) {
            return xk;
        }
        return newton(f, epsilon, xk);
    }

    public static void main(String[] args) {
        DoubleFunction<Double> funkcja = (x) -> (x + 1) * Math.pow(x - 1, 4); //wzór funkcji
        
        //newton(funkcja, epsilon, lewy koniec przedziału, prawy koniec przedziału)
        System.out.println("wynik: " + newton(funkcja, Math.pow(10, -8), -1.5, -0.75)); 
        System.out.println("iteracje: " + iteracje);
    }


}
