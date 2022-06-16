import java.util.*;

public class Fibonacci {
    public static void main(String[] args) {
        System.out.println("F(0) = " + fibonacciDyV(0));
        System.out.println("F(1) = " + fibonacciDyV(1));
        System.out.println("F(2) = " + fibonacciDyV(2));
        System.out.println("F(3) = " + fibonacciDyV(3));
        System.out.println("F(4) = " + fibonacciDyV(4));
        System.out.println("F(5) = " + fibonacciDyV(5));
        System.out.println("F(6) = " + fibonacciDyV(6));
        System.out.println("F(7) = " + fibonacciDyV(7));
    }

    //01 Algoritmo Iterativo
    public static int fibonacciIterativo(int n){
        if (n <= 1){
            return n;
        }
        int a = 0;
        int b = 1;
        int f = 0;
        for(int i = 2; i <= n; i++){
            f = a + b;
            a = b;
            b = f;
        }
        return f;
    }

    //02 Algoritmo Recurrente
    public static int fibonacciRecurrente (int n){
        if (n <= 1){
            return n;
        }
        int f = fibonacciIterativo(n-1) + fibonacciIterativo(n-2);
        return f;
    }

    //03 Algoritmo Fórmula cerrada
    public static double fibonacciCerrado (double n){
        if(n <= 1){
            return n;
        }
        return (1/Math.sqrt(5))*Math.pow((1+ Math.sqrt(5))/2,n)-(1/Math.sqrt(5))*Math.pow((1-Math.sqrt(5))/2,n);
    }

    //04 Algoritmo Divide y Vencerás
    public static int fibonacciDyV (int n){
        if(n <= 1){
            return n;
        }
        int matriz [][] = new int [2][2];
        matriz [0][0] = 1;
        matriz [0][1] = 1;
        matriz [1][0] = 1;
        matriz [1][1] = 0;

        int[][] c = new int[2][2];
        c [0][0] = 1;
        c [0][1] = 1;
        c [1][0] = 1;
        c [1][1] = 0;

        for (int i = 2; i <= n; i++){
            c = multiplicacionMatrices(matriz, c);
        }

        return c[0][1];
    }

    public static int[][] multiplicacionMatrices ( int[][] a, int[][] b) {
        int[][] c = new int[a.length][b[0].length];

        for (int i= 0; i<c.length; i++)
            for (int j=0; j<c[0].length; j++)
                for (int k=0; k<b.length; k++)
                    c[i][j] = c[i][j] + a[i][k] * b[k][j];
        return c;
    }

    public static void print2D(int mat[][])
    {
        // Loop through all rows
        for (int i = 0; i < mat.length; i++)

            // Loop through all elements of current row
            for (int j = 0; j < mat[i].length; j++)
                System.out.print(mat[i][j] + " ");
    }

    /*public static int fibonacciDyV (int n){
        if(n <= 1){
            return n;
        }
        int matriz [][] = new int [2][2];
        matriz [0][0] = 1;
        matriz [0][1] = 1;
        matriz [1][0] = 1;
        matriz [1][1] = 0;

        int[][] c = new int[2][2];
        c [0][0] = 1;
        c [0][1] = 1;
        c [1][0] = 1;
        c [1][1] = 0;

        c = multiplicacionMatrices(c,matriz);
        if(n%2 == 0){
            for(int i = 1; i <= (n/2); i++){
                c = multiplicacionMatrices(c,matriz);
            }
        } else{
            for(int i = 1; i <= ((n-1)/2); i++){
                c = multiplicacionMatrices(c,matriz);
            }
        }



    }*/
}
