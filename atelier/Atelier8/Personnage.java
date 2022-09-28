package Atelier8;

public abstract class Personnage {

	protected String nom;
	private int age;
	protected int position;
	protected Joueur proprietaire=null;
	
	public Personnage(String nom, int age) { //Constructeur personnage avec nom et age
		this.age=age;
	    this.nom=nom;
	}
	public void ajouterProprietataire(Joueur j) {
		if (proprietaire==null) {
			this.proprietaire=j;
		}
	}
	public void deplacer(int destination,int gain) {//Deplace le personnage vers destination et ajoute gains au proprietaire
		this.position = destination;
	    this.proprietaire.modifierPoints(gain);
	}
	public void penaliser(int penalite) { //Enleve penalite points au proprietaire
		this.proprietaire.modifierPoints(penalite * -1);
	}
	public String toString() {//redefintion toString
		return this.nom;
	}
	public abstract int positionSouhaitee();//Methode abstraite qui renvoie un int
	
	public abstract String typePerso();//Méthode abstraite pour récuperer le type du perso pour le .txt
}
