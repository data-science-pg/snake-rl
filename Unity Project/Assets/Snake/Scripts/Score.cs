using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Score : IGameStateHandler
{
	private GameSettings settings;
	
	public GameState Initialze(GameState gameState, GameSettings gameSettings)
	{
		settings = gameSettings;
		gameState.currentPointLocation = GetRandomPointLocation();
		gameState.score = 0;
		return gameState;
	}

	public GameState Update(GameState gameState)
	{
		if (gameState.currentPointLocation == gameState.CurrentSnakeElements[0])
		{
			++gameState.score;
			gameState.CurrentSnakeElements.Insert(0,gameState.currentPointLocation+gameState.currentDirection);
			gameState.currentPointLocation = GetRandomPointLocation();
		}
		return gameState;
	}

	private Vector2Int GetRandomPointLocation()
	{
		return new Vector2Int(Random.Range(0,settings.boardSize.x),Random.Range(0,settings.boardSize.y));
	}
}
