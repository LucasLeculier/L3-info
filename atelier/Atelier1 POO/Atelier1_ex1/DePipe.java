package Atelier1_ex1;

public class DePipe extends De {
	private int vMin;
	
	
	public DePipe(String nom,int nbFaces, int vMin) {
		super(nom,nbFaces);
		
		if (vMin < nbFaces && vMin > 3) {
			this.vMin = vMin;
		}
		else {
			this.vMin = 3;
		}
	}
	public DePipe(int vMin) {
		this("De"+nbDes,defaultValue,vMin);
		
	}
	public DePipe(int nbFaces,int vMin) {
		this("De"+nbDes,nbFaces,vMin);
		
	}
	public DePipe(String nom,int vMin) {
		this(nom,defaultValue,vMin);
		
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
