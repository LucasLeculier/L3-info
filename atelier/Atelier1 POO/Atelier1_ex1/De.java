package Atelier1_ex1;

import java.util.*;

//Question 9 : on utilise un arrayList que l'on prend en parametre et nbfaces = len(array)

public class De {
		protected int nbFaces;
		protected String nom;
		protected static Random r = new Random();
		protected static int nbDes = 0;
	        protected final int defaultValue = 6;
		

		public De(String nom, int nbFaces) {
			this.nom = nom;
			nbDes++;
			if (nbFaces >= 3 && nbFaces <= 120) {
				this.nbFaces = nbFaces;
			}
			else {
				//System.out.println("Nombre de faces impossible, nombre de faces établi a 6");
				this.nbFaces = defaultValue;
			}
		}	
		
	public De() {
		this("De"+nbDes,defaultValue);
		
	}
	public De(int nbFaces) {
		this("De"+nbDes,nbFaces);
	}
	
	
	public De(String nom) {
		this(nom,defaultValue);
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
	
	
	//METHODES 
	
	public int lancer() {
			return  r.nextInt(1,this.nbFaces + 1);}
	
	public int lancer(int nbLancer) {
		int meilleur = 0;
		for (int i=0;i < nbLancer; i++) {
			int valeur = r.nextInt(1,this.nbFaces + 1);
			if (valeur== nbFaces) {
				return valeur;
			}
			if (valeur > meilleur) {
				meilleur = valeur;
			}
		}
		return meilleur;
	}
	public String toString() {
		return "nom : "+this.nom + " nombre de faces : "+nbFaces;
	}
	public boolean equal(Object de1) {
		boolean result = false;
		if(de1 != null && de1 instanceof Des) {
			Des de =(Des) de1; 
			result = (this.name.equals(de.name) && this.nbFaces==de.nbFaces);
		}
		return result;
		
		
	}
}
