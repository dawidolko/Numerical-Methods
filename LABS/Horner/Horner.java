
package Horner;

import java.util.Scanner;


public class Horner {

    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Podaj liczbę współczynników: ");
        int liczba = scan.nextInt();
        System.out.println("");
        
        
        double[] tab = new double[liczba];
        double[] tab2 = new double[liczba];
        double[] tab3 = new double[liczba];
        tab2[tab2.length-1] = 0;
        
        for(int i=tab.length-1; i>=0; i--)
        {
            if(i > 0) 
            {
                System.out.print("Podaj liczbę przy współczynniku x"+i+": ");
                tab[i] = scan.nextDouble();
            }
            else
            {
                System.out.print("Podaj wyraz wolny: ");
                tab[i] = scan.nextDouble();
            }
        }
        
        System.out.print("Podaj argument: ");
        double argument = scan.nextDouble();
        
        for(int i=tab.length-1; i>=0; i--)
        {
            tab3[i] = tab[i] + tab2[i];
            if(i>0) tab2[i-1] = argument * tab3[i];
        }
        
        System.out.println("");
        
        for(int i=tab.length-1; i>=0; i--)
        {
                System.out.print("\t"+tab[i]);
                
        }
        
        System.out.println("");
        System.out.print(argument);
        
        for(int i=tab.length-1; i>=0; i--)
        {
                System.out.print("\t"+tab2[i]);    
        }
        
        System.out.println("");
        for(int i=tab.length-1; i>=0; i--)
        {
                System.out.print("\t"+tab3[i]);    
        }
        
        System.out.println("\n");
        
        System.out.print("Wielomian Q(x): ");
        for(int i=tab.length-1; i>=1; i--)
        {
                System.out.print(tab3[i]+"x^"+(i-1));
                if(i>1) System.out.print(" + ");
        }
        
        if(tab3[0]>0) System.out.print(" + "+tab3[0]+"/x-"+argument);
        System.out.println("");
        
        System.out.println("Wartość podanej funkcji w punkcie x = "+liczba+" to: "+tab3[0]);
        System.out.println("");
    }
    
}
