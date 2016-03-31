package examples;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Reader;
import java.io.Writer;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

import cspSolver.BTSolver;
import cspSolver.BTSolver.ConsistencyCheck;
import cspSolver.BTSolver.ValueSelectionHeuristic;
import cspSolver.BTSolver.VariableSelectionHeuristic;
import sudoku.SudokuBoardGenerator;
import sudoku.SudokuBoardReader;
import sudoku.SudokuFile;

public class SudokuFileExample {

	public static void main(String[] args)
	{
		double startTime;
		double endTime;
		Map<String, Integer> hash = Collections.synchronizedMap(new HashMap());
		hash.put("FC", 1);
		hash.put("ACP", 5);
		hash.put("MAC", 6);
		hash.put("MRV", 2);
		hash.put("DH", 3);
		hash.put("LCV", 4);
		
		startTime = System.currentTimeMillis();
		// Don't forget to check for input errors!
		
		//SudokuFile SudokuFileFromFile = SudokuBoardReader.readFile("ExampleSudokuFiles/PH5.txt");
		/*if (args.length == 1)
		{
			SudokuFile SudokuFileFromFile = SudokuBoardReader.readFile("src/examples/" + args[0]);
			//SudokuFile SudokuFileFromFile = SudokuBoardReader.readFile(args[0]);
			
			System.out.println("*****************************************");
			System.out.println("below is a SudokuFile generated from a file:");
			System.out.println("*****************************************");
			System.out.println(SudokuFileFromFile);
		}*/
		/*if (args[3].equals("gen"))
		{
			//System.out.println("ERROR invalid argument length");
			try (Reader reader = new FileReader("src/examples/" + args[0])) {
			//try (Reader reader = new FileReader(args[0])) {
				try(BufferedReader br = new BufferedReader(reader)){
					String line;
					//int lineCounter = 0;

					if((line = br.readLine()) != null)
					{	
						int N, p, q, m, timeout;
						
						
						String[] lineParts = line.split("\\s+");
						
						N = Integer.parseInt(lineParts[0]);
						p = Integer.parseInt(lineParts[1]);
						q = Integer.parseInt(lineParts[2]);
						m = Integer.parseInt(lineParts[3]);
						//timeout = Integer.parseInt(args[2]) * 1000;
						timeout = 300000;
						
						SudokuFile generatedSudokuFile = SudokuBoardGenerator.generateBoard(N, p, q, m);
						//SudokuFile generatedSudokuFile = SudokuBoardGenerator.generateBoard(9, 3, 3, 12, 999);
						
						BTSolver solver = new BTSolver(generatedSudokuFile);
						solver.setConsistencyChecks(ConsistencyCheck.ForwardChecking);
						//solver.setConsistencyChecks(ConsistencyCheck.None);
						//solver.setConsistencyChecks(ConsistencyCheck.ArcConsistency);
						solver.setValueSelectionHeuristic(ValueSelectionHeuristic.LeastConstrainingValue);
						solver.setVariableSelectionHeuristic(VariableSelectionHeuristic.Both);
						
						Thread t1 = new Thread(solver);
						try
						{
							t1.start();
							t1.join(timeout);
							if(t1.isAlive())
							{
								t1.interrupt();
							}
						}catch(InterruptedException e)
						{
						}


						if(solver.hasSolution())
						{
							System.out.println("TOTAL START TIME");
							solver.printSolverStats();
							System.out.println("*****************************************");
							System.out.println("below is a randomly generated SudokuFile:");
							System.out.println("*****************************************");
							System.out.println(solver.getSolution());	
							
							
							
							try (Writer fileWriter = new FileWriter("src/examples/" + args[1])) {
								
								String solved = solver.toString();//BTSolver(generatedSudokuFile).toString();
								//System.out.println(solved);
								fileWriter.write(solver.writeSolverStats());
								fileWriter.write(solved);
							
							}catch (IOException e1) {
									// TODO Auto-generated catch block
									System.err.print("Invalid file:"+args[0]+". Skipping to the next file.\n");
								}
						}

						else
						{
							//System.out.println("Failed to find a solution");
							System.out.println("TOTAL_START=" + startTime + " seconds");
							solver.printSolverStats();
							
							endTime = System.currentTimeMillis();
							System.out.print("SOLUTION_TIME=" + (endTime - startTime) / 1000 + " seconds\n");
							System.out.println(solver.getSolution());	
						}
						
					}
					
					else
					{
						System.out.println("Input file \""+args[0]+"\" was empty");
					}
				} 
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				System.err.print("Invalid file:"+args[0]+". Skipping to the next file.\n");
			} catch (NumberFormatException e2) {
				e2.printStackTrace();
			}
		}
		
		else
		{	*/
			int timeout;
			timeout = Integer.parseInt(args[2]) * 1000;
			//SudokuFile SudokuFileFromFile = SudokuBoardReader.readFile("src/examples/" + args[0]);
			SudokuFile SudokuFileFromFile = SudokuBoardReader.readFile(args[0]);
			
			
			BTSolver solver = new BTSolver(SudokuFileFromFile);
			//solver.setTimeout(Integer.parseInt(args[2]));
			
			if (args.length > 3)
			{
				for (int i = 3; i < args.length; ++i)
				{
					
					if (hash.containsKey(args[i]))
					{
						switch(hash.get(args[i]))
						{
							case 1:
								solver.setConsistencyChecks(ConsistencyCheck.ForwardChecking);
								break;
							case 2:
								if (solver.flag)
								{
									solver.setVariableSelectionHeuristic(VariableSelectionHeuristic.Both);
								}
								else
								{
									solver.setVariableSelectionHeuristic(VariableSelectionHeuristic.MinimumRemainingValue);
									solver.flag = true;
								}
								break;
							case 3:
								if (solver.flag)
								{
									solver.setVariableSelectionHeuristic(VariableSelectionHeuristic.Both);
								}
								else
								{
									solver.setVariableSelectionHeuristic(VariableSelectionHeuristic.Degree);
									solver.flag = true;
								}
								break;
							case 4:
								solver.setValueSelectionHeuristic(ValueSelectionHeuristic.LeastConstrainingValue);
								break;
							case 5:
								solver.setConsistencyChecks(ConsistencyCheck.PreArc);
								break;
							case 6:
								solver.setConsistencyChecks(ConsistencyCheck.ArcConsistency);
								break;
							default:
								System.out.println("Something somehow went wrong");
						}
						
					}
					else
						System.out.println("ERROR INCORRECT PARAMETER REQUESTED");
				}
					
			}
			/*solver.setConsistencyChecks(ConsistencyCheck.ForwardChecking);
			solver.setValueSelectionHeuristic(ValueSelectionHeuristic.None);
			solver.setVariableSelectionHeuristic(VariableSelectionHeuristic.None);*/
			
			Thread t1 = new Thread(solver);
			try
			{
				t1.start();
				t1.join(timeout);
				if(t1.isAlive())
				{
					t1.interrupt();
				}
			}catch(InterruptedException e)
			{
			}


			if(solver.hasSolution())
			{
				System.out.println("TOTAL_START=" + startTime + " ms");
				solver.printSolverStats();
				
				endTime = System.currentTimeMillis();
				//System.out.print("SOLUTION_TIME=" + (endTime - startTime) + " ms\n");
				System.out.println(solver.getSolution());	
				
				/*System.out.println("TEST SOLUTION");
				//System.out.println(solver.getSolution().getBoard()[0][0]);
				//System.out.println(solver.getSolution().getBoard()[0][1]);
				System.out.print("(");
				for (int i = 0, n = solver.getSolution().getN(); i < n; ++i)
				{
					for (int j = 0; j < n; ++j)
						if ((i != n - 1) || (j != n - 1))
							System.out.print(solver.getSolution().getBoard()[i][j] + ", ");
						else
							System.out.print(solver.getSolution().getBoard()[i][j] + ")\n\n");
				}
				*/
				
				try (Writer writer = new BufferedWriter(new OutputStreamWriter(
						//new FileOutputStream(fileName), "utf-8")))
			              new FileOutputStream(args[1]), "utf-8"))) 
				{
					writer.write("TOTAL_START=" + startTime + " seconds\n");
					writer.write(solver.writeSolverStats());
					//fileWriter.write("SOLUTION_TIME=" + (endTime - startTime) + " seconds\n");
					//fileWriter.write(solved);
				}
				/*try (Writer fileWriter = new FileWriter("src/examples/" + args[1])) {
					
					//String solved = BTSolver(SudokuFileFromFile).toString();
					fileWriter.write("TOTAL_START=" + startTime + " ms\n");
					fileWriter.write(solver.writeSolverStats());
					//fileWriter.write("SOLUTION_TIME=" + (endTime - startTime) + " seconds\n");
					//fileWriter.write(solved);
				
				}*/catch (IOException e1) {
						// TODO Auto-generated catch block
						System.err.print("Invalid file:"+args[0]+". Skipping to the next file.\n");
						
					}
			}

			else
			{
				System.out.println("TOTAL_START=" + startTime + " seconds");
				solver.printSolverStats();
				
				endTime = System.currentTimeMillis();
				System.out.print("SOLUTION_TIME=" + (endTime - startTime) / 1000 + " seconds\n");
				System.out.println(solver.getSolution());	
				
				/*System.out.println("TEST SOLUTION");
				//System.out.println(solver.getSolution().getBoard()[0][0]);
				//System.out.println(solver.getSolution().getBoard()[0][1]);
				System.out.print("(");
				for (int i = 0, n = solver.getSolution().getN(); i < n; ++i)
				{
					for (int j = 0; j < n; ++j)
						if ((i != n - 1) || (j != n - 1))
							System.out.print(solver.getSolution().getBoard()[i][j] + ", ");
						else
							System.out.print(solver.getSolution().getBoard()[i][j] + ")\n\n");
				}
				*/
				
				String fileName = "src/examples/" + args[1];
				try (Writer writer = new BufferedWriter(new OutputStreamWriter(
						//new FileOutputStream(fileName), "utf-8")))
			              new FileOutputStream(args[1]), "utf-8"))) 
				{
					writer.write("TOTAL_START=" + startTime + " seconds\n");
					writer.write(solver.writeSolverStats());
					//fileWriter.write("SOLUTION_TIME=" + (endTime - startTime) + " seconds\n");
					//fileWriter.write(solved);
				}
				/*try (Writer fileWriter = new FileWriter("src/examples/" + args[1])) {
					
					//String solved = BTSolver(SudokuFileFromFile).toString();
					fileWriter.write("TOTAL_START=" + startTime + " seconds\n");
					fileWriter.write(solver.writeSolverStats());
					//fileWriter.write("SOLUTION_TIME=" + (endTime - startTime) + " seconds\n");
					//fileWriter.write(solved);
				
				}*/catch (IOException e1) {
						// TODO Auto-generated catch block
						System.err.print("Invalid file:"+args[0]+". Skipping to the next file.\n");
					}
				
				/*System.out.println("Failed to find a solution");
				System.out.println("TOTAL_START=" + startTime + " seconds");
				solver.printSolverStats();
				
				endTime = System.currentTimeMillis() * 0.001;
				System.out.print("SOLUTION_TIME=" + (endTime - startTime) + " seconds\n");
				System.out.println(solver.getSolution());	
				
				
				
				try (Writer fileWriter = new FileWriter("src/examples/" + args[1])) {
					
					//String solved = BTSolver(SudokuFileFromFile).toString();
					fileWriter.write("TOTAL_START=" + startTime + " seconds\n");
					fileWriter.write(solver.writeSolverStats());
					//fileWriter.write("SOLUTION_TIME=" + (endTime - startTime) + " seconds\n");
					//fileWriter.write(solved);
				
				}catch (IOException e1) {
						// TODO Auto-generated catch block
						System.err.print("Invalid file:"+args[0]+". Skipping to the next file.\n");
					}*/
				
			}
				
			System.out.println("*****************************************");
			System.out.println("below is a SudokuFile generated from a file:");
			System.out.println("*****************************************");
			System.out.println(SudokuFileFromFile);
		}
		
	}
	
	/*public static SudokuFile BTSolver(SudokuFile sf)
	{
		//SudokuFile sf = SudokuBoardGenerator.generateBoard(9, 3, 3, 12);
		BTSolver solver = new BTSolver(sf);
		
		
		solver.setConsistencyChecks(ConsistencyCheck.None);
		solver.setValueSelectionHeuristic(ValueSelectionHeuristic.None);
		solver.setVariableSelectionHeuristic(VariableSelectionHeuristic.None);
		
		Thread t1 = new Thread(solver);
		try
		{
			t1.start();
			t1.join(60000);
			if(t1.isAlive())
			{
				t1.interrupt();
			}
		}catch(InterruptedException e)
		{
		}

		//FIX THIS UP
		if(solver.hasSolution())
		{
			//solver.printSolverStats();
			return solver.getSolution();
			
		}

		else
		{
			System.out.println("Failed to find a solution");
			return sf;
		}

	}
	*/
//}
