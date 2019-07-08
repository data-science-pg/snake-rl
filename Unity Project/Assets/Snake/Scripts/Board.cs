using System.Collections;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using UnityEngine;

public class Board : IGameStateHandler
{
	private FieldState[] fields;
	private GameSettings settings;

	public FieldState GetFieldState(int x, int y)
	{
		return fields[GetIndexFromCoords(x, y)];
	}
	
	public GameState Initialze(GameState gameState, GameSettings gameSettings)
	{
		settings = gameSettings;
		fields = new FieldState[settings.boardSize.x * settings.boardSize.y];
		return gameState;
	}

	public GameState Update(GameState gameState)
	{
		int numFields = fields.Length;
		for(int i=0;i<numFields;++i)
		{
			fields[i] = FieldState.Empty;
		}
		foreach (var snakeElement in gameState.CurrentSnakeElements)
		{
			fields[GetIndexFromCoords(snakeElement.x, snakeElement.y)] = FieldState.Snake;			
		}
		
		return gameState;
	}
	

	private int GetIndexFromCoords(int x, int y)
	{
		return y * settings.boardSize.x + x;
	}
}

public enum FieldState
{
	Empty = 0,
	Snake,
	Border,
	Point
}