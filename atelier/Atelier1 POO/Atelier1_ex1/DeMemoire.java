package Atelier1_ex1;

public class DeMemoire extends De {
	
	int valeur;
	
	public DeMemoire() {
	this.nbFaces=6;
	this.nom="Dé"+nbDes;
	nbDes++;
	}
	
      public DeMemoire(String nom,int nbFaces) {
		if (nbFaces >= 3 && nbFaces <= 120) {
			this.nbFaces = nbFaces;
		}
		else {
			//System.out.println("Nombre de faces impossible, nombre de faces établi a 6");
			this.nbFaces = 6;
		}
		this.nom=nom;
		nbDes++;
}
	public DeMemoire(String nom) {
		this(nom,6);
		
	}
	public DeMemoire(int nbFaces) {
		this("de"+nbDes)
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
