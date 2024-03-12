
package Simpson;

import java.util.function.DoubleFunction;


public class Simpson {

    public static int ITERACJE = 0;
    public static final double DX = Math.pow(10, -7);
    
    public static DoubleFunction<Double> pochodna(DoubleFunction<Double> f){
        return (x) -> (f.apply(x + DX) - f.apply(x))/ DX;
    }
    
    static double cSimpson(DoubleFunction<Double> f, double start, double stop, int divs) {
        double h, i, s, x, ans = 0;
        h = (stop - start) / divs;
        
        s = 0;
        for (i=1; i<divs; i++) {
            x = start + i*h;
            s += f.apply(x - h / 2);
            ans += f.apply(x);
        }
        s += f.apply(stop - h / 2);
        ans = (h/6) * (f.apply(start) + f.apply(stop) + 2*ans + 4*s);
       
        return ans;
    }
    
    public static void main(String[] args) {
        //wzory funkcji
        DoubleFunction<Double> f1 = (x) -> Math.pow(x, 2);
        DoubleFunction<Double> f2 = (x) -> x * Math.pow(Math.E, x);
        DoubleFunction<Double> f3 = (x) -> Math.pow(Math.E, - (Math.pow(x, 2)));
        
        //przedziały
        double[][] przedzialy = new double[][]{
            {-1, 1},
            {0, 1},
            {0, 1}
        };
        
        //cSimpson(funkcja, lewy koniec przedziału, prawy koniec przedziału
        System.out.println("funkcja 1: " + cSimpson(f1, przedzialy[0][0], przedzialy[0][1], 8));
        System.out.println("funkcja 2: " + cSimpson(f2, przedzialy[1][0], przedzialy[1][1], 8));
        System.out.println("funkcja 3: " + cSimpson(f3, przedzialy[2][0], przedzialy[2][1], 8));
    }
    
}
