package Atelier1_ex1;

import java.util.*;

//Question 9 : on utilise un arrayList que l'on prend en parametre et nbfaces = len(array)

public class Dé {
	protected
		int nbFaces;
		String nom;
		static Random r = new Random();
		static int nbDés = 0;
		

	public Dé() {
		this.nbFaces = 6;
		this.nom = "De"+nbDés;
		nbDés ++;
	}
	public Dé(int nbFaces) {
		if (nbFaces >= 3 && nbFaces <= 120) {
			this.nbFaces = nbFaces;
		}
		else {
			//System.out.println("Nombre de faces impossible, nombre de faces établi a 6");
			this.nbFaces = 6;
		}
		this.nom="De"+nbDés;
		nbDés++;
	}
	
	
	public Dé(String nom) {
		this.nom = nom;
		this.nbFaces = 6;
		nbDés++;
	}
	
	
	public Dé(String nom, int nbFaces) {
		this.nom = nom;
		nbDés++;
		if (nbFaces >= 3 && nbFaces <= 120) {
			this.nbFaces = nbFaces;
		}
		else {
			//System.out.println("Nombre de faces impossible, nombre de faces établi a 6");
			this.nbFaces = 6;
		}
	}
	
	//GET SET
	
	
	
	public int getNbFaces() {
		return this.nbFaces;
	}
	public void setNbFaces(int choix) {
		this.nbFaces = choix;
	}
	public String getNom() {
		return this.nom;
	}
	
	
	
	public int lancer() {
			return  r.nextInt(1,this.nbFaces + 1);}
	
	public int lancer(int nbLancer) {
		int meilleur = 0;
		for (int i=0;i < nbLancer; i++) {
			int valeur = r.nextInt(1,this.nbFaces + 1);
			if (valeur > meilleur) {
				meilleur = valeur;
			}
		}
		return meilleur;
	}
	public String toString() {
		return "nom : "+this.nom + " nombre de faces : "+nbFaces;
	}
	public Boolean equals(Dé de1) {
		return this.nom == de1.nom && this.nbFaces == de1.nbFaces;
	}
}
