package Atelier0_ex2;

public class test_Vecteur3D {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Vecteur3D v1 = new Vecteur3D(3,2,5);
		Vecteur3D v2 = new Vecteur3D(1,2,3);
		v1.afficher();
		System.out.println("Norme de v1 = "+v1.norme());
		v2.afficher();
		System.out.println("Norme de v2 = "+v2.norme());
		Vecteur3D v3 = Vecteur3D.sommeVecteurs(v1,v2);
		System.out.print("v1 + v2 = ");
		v3.afficher();
		System.out.print("v1.v2 = " + v1.produitScalaire(v2));
		
	}

}
