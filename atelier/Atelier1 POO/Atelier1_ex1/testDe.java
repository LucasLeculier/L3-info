package Atelier1_ex1;

public class testDe {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		De maurice = new De("maurice");
		De jacques = new De(130);
		De flavien = new De("Flavien", 110);
		De robert = new De(4);
		De flav = new De("Flavien",110);
		DePipe harry = new DePipe("Harry",20,15);
		/*
		Question 2
		System.out.println(maurice.getNom());
		System.out.println(maurice.getNbFaces());
				
		System.out.println(jacques.getNom());
		System.out.println(jacques.getNbFaces());
				
		System.out.println(flavien.getNom());
		System.out.println(flavien.getNbFaces());
				
		System.out.println(robert.getNom());
		System.out.println(robert.getNbFaces());*/
		
		/*
		Question 3
		System.out.println(maurice.lancer());
		System.out.println(jacques.lancer());
		System.out.println(flavien.lancer());
		System.out.println(robert.lancer());*/

		//Question 5
		/*System.out.println(maurice.lancer(4));
		System.out.println(flavien.lancer(20));*/
		
		//Question 6
		/*System.out.println(jacques);
		System.out.println(flavien.equals(flav));
		System.out.println(flavien.equals(robert));*/
		
		//Question 7
		/*for (int i=0; i<20;i++) {
			System.out.println(harry.lancer());
		}
		System.out.println(harry.toString());*/
		
		//Question 8
		for (int i=0; i<20;i++) {
			System.out.println(robert.lancer());}
		
	}

}
