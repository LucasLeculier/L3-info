package Atelier1_ex1;

public class DéMemoire extends Dé {
	
	int valeur;
	
	public DéMemoire() {
	this.nbFaces=6;
	this.nom="Dé"+nbDés;
	nbDés++;
	}
	public DéMemoire(String nom) {
		this.nbFaces=6;
		this.nom=nom;
		nbDés++;
		
	}
	public DéMemoire(int nbFaces) {
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
	public DéMemoire(String nom,int nbFaces) {
		if (nbFaces >= 3 && nbFaces <= 120) {
			this.nbFaces = nbFaces;
		}
		else {
			//System.out.println("Nombre de faces impossible, nombre de faces établi a 6");
			this.nbFaces = 6;
		}
		this.nom=nom;
		nbDés++;
}
	public int lancer() {
		int newValeur;
		while(true) {
			newValeur =r.nextInt(1,this.nbFaces + 1);
			if (newValeur != valeur) {
				valeur = newValeur;
				break;
			}
		}
		return valeur;
		
	}
}
