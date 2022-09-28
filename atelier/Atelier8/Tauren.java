package Atelier8;

import java.util.Random;

public class Tauren extends Personnage {

	private int taille;
	
	public Tauren(String nom,int age,int taille) {
		super(nom,age);
		this.taille=taille;
	}

	@Override
	public int positionSouhaitee() {
		Random r = new Random();
		return this.position +r.nextInt(1, taille+1);
	}
	public String toString() {
		return "Tauren "+this.nom;
	}

	@Override
	public String typePerso() {
		// TODO Auto-generated method stub
		return "T";
	}
	
	
}
