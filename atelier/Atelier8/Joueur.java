package Atelier8;

import java.util.ArrayList;

public class Joueur {

	private String nom;
	private String code;
	private static int nbJoueurs = 1;
	private int nbPoints = 0;
	protected ArrayList<Personnage> listePersos = new ArrayList<Personnage>();
	
	public Joueur(String nom){
		this.code= "j"+nbJoueurs;
		this.nom=nom;
		nbJoueurs ++;
	}
	public int getNbPoints() {
		return this.nbPoints;
	}
	
	public void ajouterPersonnage(Personnage p) {
		listePersos.add(p);
		p.ajouterProprietataire(this); 
	}
	public void modifierPoints(int nb) {
		if (this.nbPoints+ nb >=0) {
			this.nbPoints+= nb;
		}
	}
	public boolean peutJouer() {
		return (this.listePersos.size()>0);
	}
	public String toString() {
		if (this.peutJouer()) {
			return code +" "+this.nom+" ("+nbPoints +" points) avec "+listePersos.size()+" personnage(s)";
		}
		else{
			return code +" "+this.nom+" ("+nbPoints +" points) avec 0 personnage";
		}
		
	}
}
