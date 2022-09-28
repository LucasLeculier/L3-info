package Atelier8;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.UnsupportedEncodingException;

public class TestJeu {

	public static void main(String[] args) throws IOException {
		
		Jeu jeu1 = new Jeu("AtelierPOO",20,10);
		Joueur paul = new Joueur("Paul");
		
		Personnage hector = new Tauren("Hector",15,10);
		Personnage jean = new Humain("Jean",10);
		
		paul.ajouterPersonnage(jean);
		paul.ajouterPersonnage(hector);
		
		Joueur lucien = new Joueur("Lucien");
		
		Personnage hercule = new Tauren("Hercule",20,20);
		Personnage marie = new Humain("Marie",10);
		
		lucien.ajouterPersonnage(hercule);
		lucien.ajouterPersonnage(marie);
		
		jeu1.ajouterJoueur(lucien);
		jeu1.ajouterJoueur(paul);
		
//		for (int i=0;i<5;i++) {			
			jeu1.lancerJeu();
		//}
		
	}

}
