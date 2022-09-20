package Atelier0_ex1;

public class Robot {

	private String ref;
	private String nom;
	private int x;
	private int y;
	private int orientation;
	private static int nbRobots;
	
	public Robot(String nom, int x,int y, int orientation) {
		this.nom = nom;
		this.x = x;
		this.y = y;
		this.orientation = orientation;
		this.ref = "rob"+nbRobots;
		nbRobots ++;
	}
	
	public Robot(String nom) {
		this.nom = nom;
		this.x = 0;
		this.y = 0;
		this.orientation = 1;
		this.ref = "rob"+nbRobots;
		nbRobots ++;
	}
	
	public void setOrientation(int choix) {
		this.orientation=choix;
	}
	public void deplacer() {
		switch(this.orientation) {
		case(1):
			this.y ++;
			break;
		
		case(2):
			this.x ++;
			break;
		
		case(3):
			if (this.y==0) {
				System.out.println("Le robot ne peut pas aller au sud (déja au bord");
			}
			this.y --;
			break;
		
		case(4):
			if (this.x==0) {
				System.out.println("Le robot ne peut pas aller à l'ouest (déja au bord");
				break;
			}
			this.x --;
			break;
		default:
			System.out.println("Valeur incorrecte");
			
	}
	}
	public void afficheToi() {
		String direction ="";
		
		switch(this.orientation) {
		case(1):
			direction += "nord";
			break;
		case(2):
			direction += "est";
			break;
		case(3):
			direction += "sud";
			break;
		case(4):
			direction += "ouest";
			break;
			
		}
		
		System.out.println("Robot " + this.nom +" "+ this.ref + " coordonées : " + this.x +" " + this.y + " orienté vers : " + direction);
	}
	public String toString() {
String direction ="";
		
		switch(this.orientation) {
		case(1):
			direction += "nord";
			break;
		case(2):
			direction += "est";
			break;
		case(3):
			direction += "sud";
			break;
		case(4):
			direction += "ouest";
			break;
			
		}
		return "Robot " + this.nom +" "+ this.ref + " coordonées : " + this.x +" " + this.y + " orienté vers : " + direction;
	}
}


