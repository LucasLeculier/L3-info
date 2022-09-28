package Atelier8;

public class TestJeu {

	public static void main(String[] args) {
		
		Jeu jeu1 = new Jeu("AtelierPOO",4,10);
		Joueur paul = new Joueur("Paul");
		
		Personnage hector = new Tauren("Hector",15,10);
		Personnage jean = new Humain("Jean",10);
		
		paul.ajouterPersonnage(jean);
		paul.ajouterPersonnage(hector);
		
		Joueur lucien = new Joueur("Lucien");
		
		Personnage hercule = new Tauren("Hercule",20,5);
		Personnage marie = new Humain("Marie",10);
		
		lucien.ajouterPersonnage(hercule);
		lucien.ajouterPersonnage(marie);
		
		jeu1.ajouterJoueur(lucien);
		jeu1.ajouterJoueur(paul);
		
		for (int i=0;i<5;i++) {			
			jeu1.lancerJeu();
		}
		
	}

}
