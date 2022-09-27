package Atelier1_ex1;

public class DeMemoire extends De {
	
	int valeur;
	
      public DeMemoire(String nom,int nbFaces) {
		if (nbFaces >= 3 && nbFaces <= 120) {
			this.nbFaces = nbFaces;
		}
		else {
			//System.out.println("Nombre de faces impossible, nombre de faces établi a 6");
			this.nbFaces = defaultValue;
		}
		this.nom=nom;
		nbDes++;
}
	public DeMemoire(String nom) {
		this(nom,defaultValue);
		
	}
	public DeMemoire(int nbFaces) {
		this("de"+nbDes,nbFaces)
}
	public DeMemoire() {
	this("de"+defaultValue);
	}
	
	public int lancer() {
		int newValeur;
		while(true) {
			newValeur =r.nextInt(1,this.nbFaces + 1);
			if(newValeur==nbFaces){
				return newValeur;//Cas ou la valeur tirée est le max
			if (newValeur != valeur) {
				valeur = newValeur; 
				break;
			}
		}
		return valeur;
		
	}
}
