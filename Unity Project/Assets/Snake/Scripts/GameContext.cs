using System.Collections;
using System.Collections.Generic;
using System.Security.AccessControl;
using UnityEngine;

public class GameContext : MonoBehaviour, IInputListener
{
    public GameSettings settings;
    public BoardView boardView;
    public Sounds sounds;
    
    private Board board;
    private Snake snake;
    private Score score;
    private GameState gameState = new GameState();
    private InputDevice inputDevice;
    
    public void Awake()
    {
	    inputDevice = new KeyboardInputDevice {listener = this};
	    ResetGame();
	    StartCoroutine(LoopTicks());
    }

    private IEnumerator LoopTicks()
    {
	    while (true)
	    {
		    GameTick();
		    yield return new WaitForSeconds(0.5f);
	    }
    }

    private void Update()
    {
	    inputDevice.UpdateInput();        
}

    private void GameTick()
    {
	    gameState.Update(snake).Update(score);
        if (gameState.lastValidMove)
        {
	        boardView.Redraw(gameState);
	        sounds.UpdateSounds(gameState);
        }
        else
        {
	        ResetGame();
        }
    }

    private void ResetGame()
    {
	    gameState.currentDirection = settings.initialSnakeDirection;
	    snake = new Snake();
	    board = new Board();
	    score = new Score();

	    gameState.Initialize(snake, settings).Initialize(board, settings).Initialize(score, settings);

	    boardView.Generate(settings.boardSize.x,settings.boardSize.y);
	    sounds.Reset();
    }

    public void HandleInput(Vector2Int direction)
    {
	    gameState.currentDirection = direction;
    }
}

public interface IGameStateHandler
{
	GameState Initialze(GameState gameState, GameSettings gameSettings);

	GameState Update(GameState gameState);
}

public class GameState
{
	public Vector2Int currentPointLocation;
	public Vector2Int currentDirection;
	public Vector2Int pointPosition;
	public List<Vector2Int> CurrentSnakeElements;
	public bool lastValidMove;
	public int score;

	public GameState Initialize(IGameStateHandler handler,GameSettings settings)
	{
		return handler.Initialze(this,settings);
	}

	public GameState Update(IGameStateHandler handler)
	{
		return handler.Update(this);
	}
}
