package Atelier8;

import java.util.ArrayList;
import java.util.Random;

public class Jeu {

	private String titre;
	final int NB_JOUEUR_MAX = 6;
	final int NB_CASES = 50;
	private ArrayList<Joueur> listeJoueurs = new ArrayList<Joueur>();
	private Case[] cases = new Case[NB_CASES];
	private int nbEtapes;
	private int nbObstacles;
	private int scoreMax=0;
	private static int compteurObstacles=0;
	private static int compteurEtapes=0;
	private static int compteurJeu =1;
	
	//Constructeur avec titre nb etapes nb Obstacles max
	public Jeu(String titre,int nbEtapes,int nbObstacles) {
		this.titre=titre;
		this.nbEtapes=nbEtapes;
		this.nbObstacles=nbObstacles;
	}
	
	public void ajouterJoueur(Joueur j) {//Ajouter Joueur
		listeJoueurs.add(j);
	}
	public ArrayList<Personnage> tousLesPerso(){ //Récupération liste persos
		ArrayList<Personnage> liste = new ArrayList<Personnage>(); 
		for (int i=0;i<listeJoueurs.size();i++){
			liste.addAll(listeJoueurs.get(i).listePersos);
					
		}
		return liste;
	}
	public void initialiserCases() { //initialisaiton des cases
		Random r = new Random();
		for (int i =0; i<50;i++) {
			int gain = r.nextInt(1, NB_CASES+1);
			
			
			if(nbObstacles>compteurObstacles && gain%5==0){
				Obstacle obs = new Obstacle(gain*2);
				Case casee = new Case(obs,gain);
				cases[i]=casee;
				compteurObstacles++;
		}
					
			else {
				Case casee= new Case(gain);
				cases[i]=casee;
			}
			
		}
	}
	
	
	public void afficherCases() { //affichage de la valeur des cases
		for (int i=0; i<cases.length;i++) {
			
			System.out.println("case numéro "+i+" "+cases[i]);
		}
	}
	
	public void afficherParticipants() { //affichage liste participants
		String str = "LISTE DES JOUEURS";
		for (int i=0;i<listeJoueurs.size();i++) {
			str += "\n ------------------------- \n";
			str += listeJoueurs.get(i).toString();
		}
		System.out.println(str);
	}
	public void afficherResultats() {
		afficherParticipants();
		String str = "Jeu Atelier POO \n ---------------------------- \n RESULTATS \n";
		Joueur gagnant = trouverGagnant();
		str += "Le gagnant est "+gagnant.toString();
		if (gagnant.getNbPoints()>scoreMax) { //Si le gagnant a battu le record
			str+= "\nRecord battu : Ancien score maximum "+scoreMax;
			scoreMax=gagnant.getNbPoints();
		}
		System.out.println(str);
		
	}
	public Joueur trouverGagnant() { //Parcours les joueurs et récupere celui qui a le max de points
		Joueur gagnant = listeJoueurs.get(0);//initialisation du premier joueur comme gagnant
		for (int i=1;i<listeJoueurs.size();i++) {//PArcours les joueurs 
			if (listeJoueurs.get(i).getNbPoints()>gagnant.getNbPoints()) {//Compare le gagnant a chaque joueur
				gagnant = listeJoueurs.get(i);
			}
		}
		return gagnant;
	}
	
	public void lancerJeu() { //Lancement du jeu
		
		System.out.println("JEU NUMERO "+compteurJeu);
		initialiserCases();
		ArrayList<Personnage> listePersos = tousLesPerso();
		int num_case = 0;
		//Placements des joueurs
		for (int i=0;i<listePersos.size();i++) {
			Personnage personnage = listePersos.get(i); //Récupere le personnage a la position i
			while(true) {
				if (cases[num_case].estLibre()) {
					cases[num_case].placerPersonnage(personnage);
					break;
				}
				num_case ++;
			}
		}
		//Lancement du jeu
		afficherParticipants();
		afficherCases();
		while(compteurEtapes<nbEtapes) {
			for (int i=0;i<listePersos.size();i++) {
				Personnage personnage = listePersos.get(i); //Récupere le personnage a la position i
				int numCaseSouhait = personnage.positionSouhaitee();
				
				if (numCaseSouhait>NB_CASES) {
					numCaseSouhait=NB_CASES;
				}
				
				if(cases[numCaseSouhait].estLibre()) {
					personnage.deplacer(numCaseSouhait, cases[numCaseSouhait].getGain());
				}
				else {
					personnage.penaliser(cases[numCaseSouhait].getGain());
				}
		}
			compteurEtapes++;
			
		}
		afficherResultats();
		
		//Réinitialisation de tous a 0
		for (int i=0;i<listeJoueurs.size();i++) {
			listeJoueurs.get(i).modifierPoints(0);
			for (int j=0;j<listeJoueurs.get(i).listePersos.size();j++) {
				listeJoueurs.get(j).listePersos.get(i).position=0;
			}
		}
		this.compteurEtapes=0;
		this.compteurObstacles=0;
		Case[] cases = new Case[NB_CASES];
		compteurJeu++;
		
	}
}