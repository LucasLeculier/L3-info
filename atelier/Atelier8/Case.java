package Atelier8;

public class Case {

	private int gain;
	protected Personnage perso=null;
	private Obstacle obs=null;
	
	public Case(Obstacle obs,int gain) {
		this.obs = obs;
		this.gain = gain;
	}
	public Case(int gain) {
		this(null,gain);
	}
	public int getPenalite() {
		if (obs==null) {
			return 0;
		}
		else {
			return obs.getPenalite();
		}
	}
	public int getGain() {
		return this.gain;
	}
	public void placerPersonnage(Personnage p) {
		this.perso=p;
	}
	public void placerObstacle(Obstacle obstacle) {
		this.obs=obstacle;
	}
	public void enleverPerosnnage() {
		this.perso=null;
	}
	public boolean sansObstacle() {
		return this.obs==null;
	}
	public boolean sansPerso() {
		return this.perso==null;
	}
	public boolean estLibre() {
		return sansPerso()&& sansObstacle();
	}
	
	
	public String toString() {
        if(this.estLibre()) {
            return "Libre (gain ="+this.gain+")";
        }else if(this.sansPerso()){
            return "Obstacle (pénalité -"+this.getPenalite()+")";
        }else {
            return this.perso.toString()+"pénalité = -"+this.getPenalite();
        }
    }
	
	
}
