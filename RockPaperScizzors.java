import java.util.Scanner;
import java.util.Random;


public class RockPaperScizzors {
	
	
	private static int Value; 
	private static boolean PlayGame = true;
	
	
	//main method
	public static void main(String [] args) {
		
	 	
	
	while (PlayGame) {	
		int ComputerValue[] = {1, 2, 3};
		
		Scanner scan = new Scanner(System.in); //dont close scanner, it will stop game
		Scanner s = new Scanner(System.in); // dont close scanner, it will stop game
		
		Random r = new Random();
		
		
		System.out.println("Rock, Paper, Scizzors?");
		String UserInput = scan.next();
		
		
		int RandomNumber = r.nextInt(ComputerValue.length +1);
		
		
	gameLogic(UserInput, RandomNumber);	
		
		System.out.println("play Again(y/n)?? ");
		PlayGame = s.nextLine().trim().equalsIgnoreCase("y");
		
		
	
	}	
	}
	
	
//game logic method (using Inheritance).	
	public  static void gameLogic(String UserInput, int RandomNumber) {
		
		//if statement to assign values;
		if(UserInput.equalsIgnoreCase("Rock")) {
			Value = 1;
			
		} else if (UserInput.equalsIgnoreCase("Paper")) {
			Value = 2;
			
		} else if(UserInput.equalsIgnoreCase("Scizzors")) {
			Value = 3;
			
		}
		
		
		
		
		
		//if method to compare userinput value to computer value
		if(Value == RandomNumber) {
			System.out.println("Draw");
		} else if ((Value == 1) && (RandomNumber == 2)) {
			System.out.println("You chose Rock, the computer chose paper, Computer Wins!!");
		} else if ((Value == 1) && (RandomNumber == 3)) {
			System.out.println("You chose Rock, the computer chose scizzors, You Wins!!");
		} else if ((Value == 2) && (RandomNumber == 1)) {
			System.out.println("You chose papper, the computer chose rock, You Win!!");
		} else if ((Value == 2) && (RandomNumber == 3)) {
			System.out.println("You chose paper, the computer chose scizzors, computer Wins!!");
		} else if ((Value == 3) && (RandomNumber == 1)) {
			System.out.println("You chose Scizzors, the computer chose Rock, Computer Wins!!");
		} else if ((Value == 3) && (RandomNumber == 2)) {
			System.out.println("You chose Scizzors, the computer chose paper, You Wins!!");
		}
		
		
		
	}
	
	
	
	
	
	
	
	
	
}
