package Atelier1_ex1;

public class DéPipe extends Dé {
	private int vMin;
	private int valeur;
	
	public DéPipe(String nom,int nbFaces, int vMin) {
		super(nom,nbFaces);
		
		if (vMin < nbFaces && vMin > 3) {
			this.vMin = vMin;
		}
		else {
			this.vMin = 3;
		}
		nbDés++;
	}
	public DéPipe(int vMin) {
		this.nbFaces = 6;
		this.nom = "Dé"+nbDés;
		nbDés++;
		if (vMin < nbFaces && vMin > 3) {
			this.vMin = vMin;
		}
		else {
			this.vMin = 3;
		}
		
	}
	public DéPipe(int nbFaces,int vMin) {
		this.nbFaces = nbFaces;
		this.nom = "Dé"+nbDés;
		nbDés++;
		if (vMin < nbFaces && vMin > 3) {
			this.vMin = vMin;
		}
		else {
			this.vMin = 3;
		}
		
	}
	public DéPipe(String nom,int vMin) {
		this.nbFaces = 6;
		this.nom = nom;
		nbDés++;
		if (vMin < nbFaces && vMin > 3) {
			this.vMin = vMin;
		}
		else {
			this.vMin = 3;
		}
		
	}
	// GET SET
	public int getVMin() {
		return this.vMin;
	}
	public String toString(){
		return super.toString() + " valeur minimale : " + vMin;
	}
	public int lancer() {
		return r.nextInt(vMin,this.nbFaces + 1);
		}
	
	public int lancer(int nbLancer) {
		int meilleur = 0;
		for (int i=0;i < nbLancer; i++) {
			int valeur = r.nextInt(vMin,this.nbFaces + 1);
			if (valeur > meilleur) {
				meilleur = valeur;
			}
		}
		return meilleur;
	}
}
