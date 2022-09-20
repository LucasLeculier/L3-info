package Atelier1_ex2;

public class testIncrementation {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	
	manipulationInt entier1 = new manipulationIntFou(3,10,3);
	manipulationInt entier2 = new manipulationIntFou(3,10,1,4);
	System.out.println(entier1.getEntier());
	System.out.println(entier2.getEntier());
	System.out.println(entier2);
	entier2.incrementerEntier();
	System.out.println(entier2.getEntier());
	}
}