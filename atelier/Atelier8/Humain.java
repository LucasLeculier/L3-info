package Atelier8;

public class Humain extends Personnage {

	private static int nbDeplacements=0;
	private int niveau=1;
	
	public Humain(String nom,int age) {
		super(nom,age);
	}
	
	public void deplacer(int destination,int gain) {
		super.deplacer(destination, gain);
		nbDeplacements++;
		if(nbDeplacements>=6) {//Vérification du niveau 3
			this.niveau = 3;
		}
		else if(nbDeplacements>=4){//Vérification du niveau 2
		    this.niveau=2;
		}
		
	}

	@Override
	public int positionSouhaitee() {
		return this.position + this.niveau*nbDeplacements;
	}
	public String toString() {
		return "Humain "+this.nom;
	}
}

