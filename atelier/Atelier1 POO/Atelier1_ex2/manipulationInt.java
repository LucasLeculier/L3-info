package Atelier1_ex2;

import java.util.Objects;
import java.util.*;

public class manipulationInt {
	protected
	 int bornInf;
	 int bornSup;
	 int entier;
	
	public manipulationInt(int bornInf,int bornSup) {
		this.entier=0;
		this.bornInf=bornInf;
		this.bornSup=bornSup;
	}
	public manipulationInt(int bornInf,int bornSup,int entier) {
		if (entier>=bornInf && entier<=bornSup) {
			this.entier=entier;
		}
		else {
			this.entier=0;
		}
		this.bornInf=bornInf;
		this.bornSup=bornSup;
	}
	//GET SET
	public int getBInf() {
		return this.bornInf;
	}
	public int getBup() {
		return this.bornSup;
	}
	public int getEntier() {
		return this.entier;
	}
	public void setEntier(int entier) {
		if (entier>=this.bornInf && entier<=this.bornSup) {
			this.entier=entier;
		}
		else {
			this.entier=0;
		}
	}
	public void incrementerEntier() {
		if (this.entier<bornSup) {
			this.entier ++;
		}
		else {
			System.out.println("impossible d'incrémenter valeur de l'entier déja au maximum");
		}
	}
	public void incrementerEntier(int n) {
		if (this.entier+n <=bornSup) {
			this.entier+=n;
		}
		else {
			System.out.println("valeur finale trop grande, incrémentation impossible");
		}
	}
	public String toString() {
		return "manipulationInt [bornInf=" + bornInf + ", bornSup=" + bornSup + ", entier=" + entier + "]";
	}
	public boolean equals(manipulationInt entier) {
		return this.bornInf == entier.bornInf && this.bornSup==entier.bornSup && this.entier == entier.entier;
	}
	
}
