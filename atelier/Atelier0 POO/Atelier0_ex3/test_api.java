package Atelier0_ex3;

public class test_api {

    public static void main(String[] args) {
        double pi = Math.PI;
        System.out.println(pi);
        double r1 = Math.random();
        System.out.println(r1);
        double r2 = Math.random();
        double r3 = Math.random();
        double r4 = Math.random();
        double sum = r2+r3+r4+1;
        int convr2 = (int) sum;
        System.out.println(convr2);
        int x1 = 5;
        int x2 = 7;
        int max = Math.max(x1, x2);
        System.out.println(max);
        String n1 = "bonjour";
        String n2 = "Ciao";
        int comparaison = n1.compareTo(n2);
        if (comparaison>0) {
            System.out.println("Le plus grand est "+n1);
        }else {
            System.out.println("Le plus grand est "+n2);
        }
    }

}
