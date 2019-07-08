using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Snake : IGameStateHandler
{
	private GameSettings settings;
	private Vector2Int lastDirection;
    
    public GameState Initialze(GameState gameState, GameSettings gameSettings)
    {
	    settings = gameSettings;
	    int length = settings.initialSnakeWidth;
	    Vector2Int direction = settings.initialSnakeDirection;
	    Vector2Int position = settings.initialSnakePosition;
        
	    gameState.CurrentSnakeElements = new List<Vector2Int>(length);
	    for (int i = 0; i < length; ++i)
	    {
		    Vector2Int offset = new Vector2Int()
		    {
			    x = i * direction.x,
			    y = i * direction.y
		    };
            
		    gameState.CurrentSnakeElements.Add(position-offset);
	    }

	    return gameState;
    }

    public GameState Update(GameState gameState)
    {
	    Vector2Int direction = gameState.currentDirection;
	    if (lastDirection.magnitude!=0 && (direction.x == -lastDirection.x || direction.y == -lastDirection.y))//when snake is moving right, left is invalid
	    {
		    direction = lastDirection;
	    }
	    
	    int numElements = gameState.CurrentSnakeElements.Count;
	    for (int i = numElements - 1; i > 0; --i)
	    {
		    gameState.CurrentSnakeElements[i] = gameState.CurrentSnakeElements[i - 1];
	    }

	    gameState.CurrentSnakeElements[0] = gameState.CurrentSnakeElements[0] + direction;

	    Vector2Int firstElement = gameState.CurrentSnakeElements[0];
	    
	    for (int i = 1; i < numElements; ++i)
	    {
		    if (firstElement == gameState.CurrentSnakeElements[i])
		    {
			    gameState.lastValidMove = false;
			    return gameState;
		    }
	    }
	    
	    bool invalidMove = (firstElement.x < 0 || firstElement.x >= settings.boardSize.x || firstElement.y < 0 ||
	                        firstElement.y >= settings.boardSize.y);

	    gameState.lastValidMove = !invalidMove;
	    lastDirection = direction;

	    return gameState;
    }
}
