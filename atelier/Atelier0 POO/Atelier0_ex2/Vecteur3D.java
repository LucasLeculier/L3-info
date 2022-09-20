package Atelier0_ex2;

public class Vecteur3D {
	private double x;
	private double y;
	private double z;
	
	public Vecteur3D(double x, double y, double z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}
	public Vecteur3D() {
		this.x = 0;
		this.y = 0;
		this.z = 0;
	}
	public void afficher() {
		System.out.println("< "+ this.x +", "+ this.y +", "+ this.z+" >");
	}
	public double norme() {
		return Math.sqrt(x*x + y*y + z*z);
	}
	public double produitScalaire(Vecteur3D vecteur) {
		return this.x*vecteur.x + this.y*vecteur.y +this.z*vecteur.z;
		
	}
	
	public static double produitScalaire(Vecteur3D v1,Vecteur3D v2) {
		return v1.x*v2.x + v1.y*v2.y +v1.z*v2.z;
		
	}
	public Vecteur3D sommeVecteurs(Vecteur3D vecteur) {
		return new Vecteur3D(this.x + vecteur.x, this.y + vecteur.y, this.z + vecteur.z);
	}
	public static Vecteur3D sommeVecteurs(Vecteur3D v1,Vecteur3D v2) {
		return new Vecteur3D(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z);
	}
}
