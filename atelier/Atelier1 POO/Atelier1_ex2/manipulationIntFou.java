package Atelier1_ex2;
import java.util.*;

public class manipulationIntFou extends manipulationInt {
	private int niveauFolie;
	private static Random r = new Random();
	
	public manipulationIntFou(int bornInf,int bornSup,int niveauFolie) {
		super(bornInf,bornSup);
		this.niveauFolie=niveauFolie;
	}
	public manipulationIntFou(int bornInf,int bornSup,int entier,int niveauFolie) {
		super(bornInf,bornSup,entier);
		this.niveauFolie=niveauFolie;
	}
	public void incrementerEntier() {
		super.incrementerEntier(r.nextInt(1,this.niveauFolie+1));
}}
