package cspSolver;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;

import sudoku.Converter;
import sudoku.SudokuFile;
/**
 * Backtracking solver. 
 *
 */
public class BTSolver implements Runnable{

	//===============================================================================
	// Properties
	//===============================================================================

	private ConstraintNetwork network;
	private static Trail trail = Trail.getTrail();
	private boolean hasSolution = false;
	private SudokuFile sudokuGrid;

	// private int numNodeGens;
	private int numAssignments;
	private int numBacktracks;
	private long startTime;
	private long endTime;
	private String output = "(";
	private String solved = "error";
	List<Variable> array = new ArrayList<Variable>();
	HashSet<Variable> set = new HashSet<Variable>();
	private int count = 0;
	public boolean flag = false;
	//private long timeout;
	
	public enum VariableSelectionHeuristic 	{ None, MinimumRemainingValue, Degree, Both };
	public enum ValueSelectionHeuristic 		{ None, LeastConstrainingValue };
	public enum ConsistencyCheck				{ None, ForwardChecking, ArcConsistency, PreArc };
	
	private VariableSelectionHeuristic varHeuristics;
	private ValueSelectionHeuristic valHeuristics;
	private ConsistencyCheck cChecks;
	//===============================================================================
	// Constructors
	//===============================================================================

	public BTSolver(SudokuFile sf)
	{
		this.network = Converter.SudokuFileToConstraintNetwork(sf);
		this.sudokuGrid = sf;
		numAssignments = 0;
		numBacktracks = 0;
		this.cChecks = ConsistencyCheck.None;
		this.varHeuristics = VariableSelectionHeuristic.None;
		this.valHeuristics = ValueSelectionHeuristic.None;
	}

	//===============================================================================
	// Modifiers
	//===============================================================================
	
	public void setVariableSelectionHeuristic(VariableSelectionHeuristic vsh)
	{
		System.out.println(vsh);
		this.varHeuristics = vsh;
	}
	
	public void setValueSelectionHeuristic(ValueSelectionHeuristic vsh)
	{
		System.out.println(vsh);
		this.valHeuristics = vsh;
	}
	
	public void setConsistencyChecks(ConsistencyCheck cc)
	{
		System.out.println(cc);
		this.cChecks = cc;
	}
	//===============================================================================
	// Accessors
	//===============================================================================

	/** 
	 * @return true if a solution has been found, false otherwise. 
	 */
	public boolean hasSolution()
	{
		return hasSolution;
	}
	

	/**
	 * @return solution if a solution has been found, otherwise returns the unsolved puzzle.
	 */
	public SudokuFile getSolution()
	{
		return sudokuGrid;
	}
	
	public void setSolved(String status)
	{
		solved = status;
	}

	public void printSolverStats()
	{
		double end, start;
		start = startTime;
		end = endTime;
		
		int n = 0;
		if (output == "(")
		{
			n = getSolution().getBoard().length * getSolution().getBoard().length;
			for (int i = 0; i < n; ++i)
			{
				if (i == n - 1)
					output += "0)\n";
				else
					output += "0, ";
			}
		}
		
		System.out.println("SEARCH_START=" + start + " ms");
		System.out.println("SEARCH_DONE=" + end + " ms");
		System.out.println("SOLUTION_TIME=" + (end-start) + " ms");
		if (hasSolution)
			System.out.println("STATUS=success");
            // STATUS=success		
		else if (!hasSolution)
			System.out.println("STATUS=timeout");
		else
			System.out.println("STATUS=error");
		System.out.print("SOLUTION=");
		System.out.print(output);
		/*System.out.print("(");
		for (int i = 0, n = getSolution().getN(); i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
				if ((i != n - 1) || (j != n - 1))
					System.out.print(getSolution().getBoard()[i][j] + ", ");
				else
					System.out.print(getSolution().getBoard()[i][j] + ")\n");
		}*/
		System.out.println("COUNT_NODES=" + numAssignments);
		System.out.println("COUNT_DEADENDS=" + numBacktracks);
	}
	
	public String writeSolverStats()
	{
		double end, start;
		start = startTime;
		end = endTime;
		
		
		if (hasSolution)
			solved = "success";
		else if (!hasSolution)
			solved = "timeout";
		else
			solved = "error";
		
		String stats = "";
		int n = 0;
		if (output == "(")
		{
			n = getSolution().getBoard().length * getSolution().getBoard().length;
			for (int i = 0; i < n; ++i)
			{
				if (i == n - 1)
					output += "0)\n";
				else
					output += "0, ";
			}
		}
		stats = "SEARCH_START=" + start + " ms\n" + "SEARCH_DONE=" + end + " ms\n" + "SOLUTION_TIME=" + (end-start) / 1000 + " ms\n" 
		+ "STATUS=" + solved + "\n" + "SOLUTION=" + output + "COUNT_NODES=" + numAssignments + "\n"
		+ "COUNT_DEADENDS=" + numBacktracks;
		return stats;
	}

	/**
	 * 
	 * @return time required for the solver to attain in seconds
	 */
	public long getTimeTaken()
	{
		return endTime-startTime;
	}
	
	/*public void setTimeout(long time)
	{
		timeout = time;
	}*/

	public int getNumAssignments()
	{
		return numAssignments;
	}

	public int getNumBacktracks()
	{
		return numBacktracks;
	}

	public ConstraintNetwork getNetwork()
	{
		return network;
	}

	//===============================================================================
	// Helper Methods
	//===============================================================================

	/**
	 * Checks whether the changes from the last time this method was called are consistent. 
	 * @return true if consistent, false otherwise
	 */
	private boolean checkConsistency(Variable v)
	{
		boolean isConsistent = false;
		switch(cChecks)
		{
		case None: 				isConsistent = assignmentsCheck();
		break;
		case ForwardChecking: 	isConsistent = forwardChecking(v);
		break;
		case ArcConsistency: 	isConsistent = arcConsistency(v);
		break;
		case PreArc:			isConsistent = preArc(v);
		default: 				isConsistent = assignmentsCheck();
		break;
		}
		return isConsistent;
	}
	
	/**
	 * default consistency check. Ensures no two variables are assigned to the same value.
	 * @return true if consistent, false otherwise. 
	 */
	private boolean assignmentsCheck()
	{
		for(Variable v : network.getVariables())
		{
			if(v.isAssigned())
			{
				for(Variable vOther : network.getNeighborsOfVariable(v))
				{
					if (v.getAssignment() == vOther.getAssignment())
					{
						return false;
					}
				}
			}
		}
		return true;
	}
	
	/**
	 * TODO: Implement forward checking. 
	 */
	private boolean forwardChecking(Variable v)
	{
		for (Variable item : network.getVariables())
		{
			if (item.isAssigned())
			{
				for (Variable neighbor : network.getNeighborsOfVariable(item))
				{
					neighbor.removeValueFromDomain(item.getAssignment());
				}
			}
		}
		
		if (assignmentsCheck())
		{			
			for(Variable vOther : network.getNeighborsOfVariable(v))
			{
				if (!vOther.isAssigned())
				{
					vOther.removeValueFromDomain(v.getAssignment());
				}
				//System.out.println("YO YO YO");
				//System.out.println(network.getConstraintsContainingVariable(vOther));
			}
		
			return true;
		}
		return false;
		/*if(v.isAssigned())
		{
			for(Variable vOther : network.getNeighborsOfVariable(v))
			{
				//if (!vOther.isAssigned())
					if (v.getAssignment() == vOther.getAssignment())
					{
						return false;
					}
					else
					{
						System.out.println("TEST");
						vOther.removeValueFromDomain(v.getAssignment());
					}
			}
		}
		return true;*/
	}
	
	private boolean preArc(Variable v)
	{
		for (Variable item : network.getVariables())
		{
			if (item.isAssigned())
			{
				for (Variable neighbor : network.getNeighborsOfVariable(item))
				{
					neighbor.removeValueFromDomain(item.getAssignment());
				}
			}
		}
		return true;
	}
	
	/**
	 * TODO: Implement Maintaining Arc Consistency.
	 */
	private boolean arcConsistency(Variable v)
	{
		if (assignmentsCheck())
		{
			for (Variable item : network.getVariables())
			{
				if (item.isAssigned())
				{
					for (Variable neighbor : network.getNeighborsOfVariable(item))
					{
						neighbor.removeValueFromDomain(item.getAssignment());
					}
				}
			}
					
			for (Variable vOther : network.getNeighborsOfVariable(v))
			{
				if (!vOther.isAssigned())
				{
					vOther.removeValueFromDomain(v.getAssignment());
				}
				
				if (vOther.getDomain().size() == 1)
				{
					if (!set.contains(vOther))
					{
						set.add(vOther);
						arcConsistency(vOther);
					}	
					//System.out.println("Checking neighbors");
				}
			}
			
			/*for (Variable neighbor : network.getNeighborsOfVariable(v))
			{
				if (neighbor.getDomain().size() == 1)
				{
					System.out.println("Checking neighbors");
					arcConsistency(neighbor);
				}
			}*/
			return true;
				
		}
		return false;
		/*//if(v.isAssigned())
		//{
			for(Variable vOther : network.getNeighborsOfVariable(v))
			{
				if (v.getAssignment() == vOther.getAssignment())
				{
					return false;
				}
				else
				{
					vOther.removeValueFromDomain(v.getAssignment());
					
					for(Variable vNew : network.getNeighborsOfVariable(vOther))
					{
						if (vOther.getAssignment() == vNew.getAssignment())
						{
							return false;
						}
						else
						{
							vOther.removeValueFromDomain(vNew.getAssignment());
							
							//arcConsistency(vOther);
						}
					}
				
					return true;
					
					//arcConsistency(vOther);
				}
			}
		//}
		return true;*/
	}
	
	/**
	 * Selects the next variable to check.
	 * @return next variable to check. null if there are no more variables to check. 
	 */
	private Variable selectNextVariable()
	{
		Variable next = null;
		switch(varHeuristics)
		{
		case None: 					next = getfirstUnassignedVariable();
		break;
		case MinimumRemainingValue: next = getMRV();
		break;

		//case Degree: if MRV was also true then getMRV(); getDegree();
		//             else getDegree()
        		
		case Degree:				next = getDegree(); 
		break;
		case Both:					next = getBoth();
		break;
		default:					next = getfirstUnassignedVariable();
		break;
		}
		return next;
	}
	
	/**
	 * default next variable selection heuristic. Selects the first unassigned variable. 
	 * @return first unassigned variable. null if no variables are unassigned. 
	 */
	private Variable getfirstUnassignedVariable()
	{
		for(Variable v : network.getVariables())
		{
			if(!v.isAssigned())
			{
				return v;
			}
		}
		return null;
	}

	/**
	 * TODO: Implement MRV heuristic
	 * @return variable with minimum remaining values that isn't assigned, null if all variables are assigned. 
	 */
	private Variable getMRV()
	{
		//System.out.println("WHAT IS COUNT: " + count);
		int smallest = 99999;
		Variable firstVar;
		if (count == 0)
		{
			++count;
			firstVar = getfirstUnassignedVariable();
			//System.out.println("Printing the first time");
			return firstVar;
		}
		else
		{
			array.clear();
			//System.out.println("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV");
			for(Variable v : network.getVariables())
			{
				//System.out.println("//////////////////////// SIZE IS: " + v.getDomain().size());
				
				//New Smallest found so clear the array
				if (v.getDomain().size() != 1 && v.getDomain().size() < smallest)
				{
					//System.out.println("|||||||||||||| SMALLEST IS: " + smallest);	
					smallest = v.getDomain().size();
					array.clear();
				}
				
				//v.getDomain().size() != 9
				if(v.getDomain().size() != 1 && v.getDomain().size() <= smallest)
				{
					//array.add(v);	
					//return v;
					array.add(v);	
					//System.out.print("ZZZZZZZZZZZZZZZZZ Array is size: " + array.size() + " and array is: ");
					
					/*for(Variable i: array)
					{
						System.out.print(i + " ");
					}*/
					//System.out.println("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^");
				}
			}
			
			//System.out.println("TRY THIS");
			//System.out.println(array);
			if (!array.isEmpty())
			{
				//System.out.println("CHECK THIS");
				return array.get(0);
			}
			
			//System.out.println("SHOULD NOT HAPPEN");
			return null;
		}
		
		
		/*int smallest = 9999;
		
		for(Variable v : network.getVariables())
		{
			if(v.getDomain().size() != 1 && v.getDomain().size() <= smallest)
			{
				smallest = v.getDomain().size();
				array.clear();
				array.add(v);	
			}
		}
		if (array.size() == 0)
		{
			return null;
		}
		else
		{
			return array.get(0);
		}*/
	}
	
	/**
	 * TODO: Implement Degree heuristic
	 * @return variable constrained by the most unassigned variables, null if all variables are assigned.
	 */
	private Variable getDegree()
	{
		int max = 0;
		List<Variable> degrees = new ArrayList<Variable>();
		//Most unassigned neighbors
		//System.out.println("DEGREE HEURISTIC ENGAGED");
		//degrees.clear();
		
		if (array.isEmpty())
		{
			for(Variable v : network.getVariables())
			{
				if (!v.isAssigned())
				{
					// LOOP OVER VARIABLE OF THE NHB OF v
					//	 count unassigned in the nhd(v)
					// if current count is greater than current maximum
					//   replace curretn max with current one [record var / deg]
					
					int counter = 0;
					for (Variable neighbor : network.getNeighborsOfVariable(v))
					{	
						if (!neighbor.isAssigned())
						{
							++counter;
						}
					}
					if (counter > max)
					{
						max = counter;
						degrees.clear();
					}
					if (counter >= max)
					{
						degrees.add(v);
					}
					
					/*if (network.getNeighborsOfVariable(v).size() > neighbors)
					{
						neighbors = network.getNeighborsOfVariable(v).size();
						degrees.clear();
						degrees.add(v);
					}
					if (network.getNeighborsOfVariable(v).size() > neighbors)
					{
						degrees.add(v);
					}*/
				}
				/*for(Variable vOther : network.getNeighborsOfVariable(v))
				{
					if (v.getAssignment() == vOther.getAssignment())
					{
						return false;
					}
					else
					{
						vOther.removeValueFromDomain(v.getAssignment());
					}
				}*/
			}
			
			if (!degrees.isEmpty())
			{
				return degrees.get(0);
			}
			return null;
		}
		else
		{
			for(Variable v : array)
			{
				if (!v.isAssigned())
				{
					int counter = 0;
					
					for (Variable neighbor : network.getNeighborsOfVariable(v))
					{
						
						if (!neighbor.isAssigned())
						{
							++counter;
						}
					}
					if (counter > max)
					{
						max = counter;
						degrees.clear();
					}
					if (counter >= max)
					{
						degrees.add(v);
					}
				
					/*if (network.getNeighborsOfVariable(v).size() > neighbors)
					{
						neighbors = network.getNeighborsOfVariable(v).size();
						degrees.clear();
					}
					if (network.getNeighborsOfVariable(v).size() >= neighbors)
					{
						degrees.add(v);
					}*/
				}
			}
			
			if (!degrees.isEmpty())
			{
				return degrees.get(0);
			}
			return null;
		}
	}
	
	public Variable getBoth()
	{
		//System.out.println("HERE WE GO!");
		int smallest = 99999;
		Variable firstVar;
		if (count == 0)
		{
			++count;
			firstVar = getfirstUnassignedVariable();
			//System.out.println("Printing the first time");
			return firstVar;
		}
		else
		{
			array.clear();
			//System.out.println("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV");
			for(Variable v : network.getVariables())
			{
				//System.out.println("//////////////////////// SIZE IS: " + v.getDomain().size());
				
				//New Smallest found so clear the array
				if (v.getDomain().size() != 1 && v.getDomain().size() < smallest)
				{
					//System.out.println("|||||||||||||| SMALLEST IS: " + smallest);	
					smallest = v.getDomain().size();
					array.clear();
				}
				
				//v.getDomain().size() != 9
				if(v.getDomain().size() != 1 && v.getDomain().size() <= smallest)
				{
					//array.add(v);	
					//return v;
					array.add(v);	
					//System.out.print("ZZZZZZZZZZZZZZZZZ Array is size: " + array.size() + " and array is: ");
					
					for(Variable i: array)
					{
						//System.out.print(i + " ");
					}
					//System.out.println("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^");
				}
			}
			
			//System.out.println("TRY THIS");
			//System.out.println(array);
			if (!array.isEmpty())
			{
				//System.out.println("CHECK THIS");
				int max = 0;
				List<Variable> degrees = new ArrayList<Variable>();
				//Most unassigned neighbors
				//System.out.println("DEGREE HEURISTIC ENGAGED");
				//degrees.clear();
				
				if (array.isEmpty())
				{
					for(Variable v : network.getVariables())
					{
						if (!v.isAssigned())
						{
							// LOOP OVER VARIABLE OF THE NHB OF v
							//	 count unassigned in the nhd(v)
							// if current count is greater than current maximum
							//   replace curretn max with current one [record var / deg]
							
							int counter = 0;
							for (Variable neighbor : network.getNeighborsOfVariable(v))
							{	
								if (!neighbor.isAssigned())
								{
									++counter;
								}
							}
							if (counter > max)
							{
								max = counter;
								degrees.clear();
							}
							if (counter >= max)
							{
								degrees.add(v);
							}
							
							/*if (network.getNeighborsOfVariable(v).size() > neighbors)
							{
								neighbors = network.getNeighborsOfVariable(v).size();
								degrees.clear();
								degrees.add(v);
							}
							if (network.getNeighborsOfVariable(v).size() > neighbors)
							{
								degrees.add(v);
							}*/
						}
						/*for(Variable vOther : network.getNeighborsOfVariable(v))
						{
							if (v.getAssignment() == vOther.getAssignment())
							{
								return false;
							}
							else
							{
								vOther.removeValueFromDomain(v.getAssignment());
							}
						}*/
					}
					
					if (!degrees.isEmpty())
					{
						return degrees.get(0);
					}
					return null;
				}
				else
				{
					for(Variable v : array)
					{
						if (!v.isAssigned())
						{
							int counter = 0;
							
							for (Variable neighbor : network.getNeighborsOfVariable(v))
							{
								
								if (!neighbor.isAssigned())
								{
									++counter;
								}
							}
							if (counter > max)
							{
								max = counter;
								degrees.clear();
							}
							if (counter >= max)
							{
								degrees.add(v);
							}
						
							/*if (network.getNeighborsOfVariable(v).size() > neighbors)
							{
								neighbors = network.getNeighborsOfVariable(v).size();
								degrees.clear();
							}
							if (network.getNeighborsOfVariable(v).size() >= neighbors)
							{
								degrees.add(v);
							}*/
						}
					}
					
					if (!degrees.isEmpty())
					{
						return degrees.get(0);
					}
					return null;
				}
			}
			
			System.out.println("SHOULD NOT HAPPEN");
			return null;
		}
		
	}
	
	/**
	 * Value Selection Heuristics. Orders the values in the domain of the variable 
	 * passed as a parameter and returns them as a list.
	 * @return List of values in the domain of a variable in a specified order. 
	 */
	public List<Integer> getNextValues(Variable v)
	{
		List<Integer> orderedValues;
		switch(valHeuristics)
		{
		case None: 						orderedValues = getValuesInOrder(v);
		break;
		case LeastConstrainingValue: 	orderedValues = getValuesLCVOrder(v);
		break;
		default:						orderedValues = getValuesInOrder(v);
		break;
		}
		return orderedValues;
	}
	
	/**
	 * Default value ordering. 
	 * @param v Variable whose values need to be ordered
	 * @return values ordered by lowest to highest. 
	 */
	public List<Integer> getValuesInOrder(Variable v)
	{
		List<Integer> values = v.getDomain().getValues();
		//System.out.println("STARTING VALUES: " + values);
		
		
		Comparator<Integer> valueComparator = new Comparator<Integer>(){

			@Override
			public int compare(Integer i1, Integer i2) {
				return i1.compareTo(i2);
			}
		};
		Collections.sort(values, valueComparator);
		//System.out.println("RESULT: " + values);
		return values;
	}
	
	/**
	 * TODO: LCV heuristic
	 */
	public List<Integer> getValuesLCVOrder(Variable v)
	{
		
		//System.out.println(v);
		//System.out.println("DOMAIN: " + v.getDomain());
		List<Integer> values = v.getDomain().getValues();
		List<Integer> values2 = new ArrayList<Integer>();
		for (int item : values)
		{
			values2.add(item);
		}
		//List<Integer> copy = values;
		List<Integer> frequency = new ArrayList<Integer>();
		List<Integer> result = new ArrayList<Integer>();
		
		
		/*System.out.println("STARTING VALUES: " + values);
		if (values.isEmpty())
		{
			System.out.println("WTF");
			for (int i = 1; i < 10; ++i)
			{
				values.add(i);
			}
			return values;
		}*/
		
		//Least neighbors with that domain
		
		for (Integer choice: values2)
		{
			int counter = 0;
			for(Variable vOther : network.getNeighborsOfVariable(v))
			{
				if (!vOther.isAssigned())
				{
					//System.out.println(vOther);
					//System.out.println("THIS IS NEIGHBOR DOMAIN: " + vOther.getDomain().size() + " " + vOther.getDomain());
					if (vOther.getDomain().contains(choice))
					{
						++counter;
					}
				}
			}
			frequency.add(counter);
			//System.out.println("THIS IS FREQUENCY NOW: " + frequency);
		}
		
		while (!values2.isEmpty())
		{
			//System.out.println(values);
			int smallestIndex = 0;
			int smallest = 999999;
			for (int i = 0; i < frequency.size(); ++i)
			{
				if (frequency.get(i) < smallest)
				{
					smallest = frequency.get(i);
					smallestIndex = i;
				}
			}
			result.add(values2.get(smallestIndex));
			frequency.remove(smallestIndex);
			
			values2.remove(smallestIndex);
		}
		/*List<Integer> test = new ArrayList<Integer>();
		for (int i = 1; i <= 9; ++i)
		{
			test.add(i);
		}
		result = test;*/
		//System.out.println(values);
		//System.out.println("LCV ENGAGED");
		//System.out.println("RESULT: " + result);
		return result;
	}
	/**
	 * Called when solver finds a solution
	 */
	private void success()
	{
		hasSolution = true;
		sudokuGrid = Converter.ConstraintNetworkToSudokuFile(network, sudokuGrid.getN(), sudokuGrid.getP(), sudokuGrid.getQ());
	}

	//===============================================================================
	// Solver
	//===============================================================================

	/**
	 * Method to start the solver
	 */
	public void solve()
	{
		startTime = System.currentTimeMillis();
		try {
			solve(0);
		}catch (VariableSelectionException e)
		{
			System.out.println("error with variable selection heuristic.");
		}
		endTime = System.currentTimeMillis();
		Trail.clearTrail();
	}

	/**
	 * Solver
	 * @param level How deep the solver is in its recursion. 
	 * @throws VariableSelectionException 
	 */

	private void solve(int level) throws VariableSelectionException
	{
		/*if (System.currentTimeMillis() - startTime >= timeout * 0.001)
		{
			solved = "timeout";
			return;
		}*/
		
		if(!Thread.currentThread().isInterrupted())

		{//Check if assignment is completed
			if(hasSolution)
			{
				return;
			}

			//Select unassigned variable
			Variable v = selectNextVariable();		

			//check if the assignment is complete
			if(v == null)
			{
				for(Variable var : network.getVariables())
				{
					if(!var.isAssigned())
					{
						throw new VariableSelectionException("Something happened with the variable selection heuristic");
					}
				}
				success();
				return;
			}

			//loop through the values of the variable being checked LCV

			
			for(Integer i : getNextValues(v))
			{
				//System.out.println("CHECK OUT THIS integer: " + i);
				trail.placeBreadCrumb();

				// count number of nodes gen numNodeGen++
				//check a value
				v.updateDomain(new Domain(i));
				numAssignments++;
				boolean isConsistent = checkConsistency(v);
				
				//move to the next assignment
				if(isConsistent)
				{		
					solve(level + 1);
				}

				//if this assignment failed at any stage, backtrack
				if(!hasSolution)
				{
					trail.undo();
					numBacktracks++;
				}
				
				else
				{
					return;
				}
			}	
		}	
	}

	@Override
	public void run() {
		solve();
		for (int i = 0, n = getSolution().getN(); i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
				if ((i != n - 1) || (j != n - 1))
					output += getSolution().getBoard()[i][j] + ", ";
				else
					output += getSolution().getBoard()[i][j] + ")\n";
		}
	}
}
