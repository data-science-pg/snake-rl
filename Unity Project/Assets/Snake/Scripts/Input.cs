using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public interface IInputListener
{
	void HandleInput(Vector2Int direction);
}

public abstract class InputDevice
{
	public IInputListener listener;

	public abstract void UpdateInput();

	public abstract bool AnyKeyDown();
}

public class KeyboardInputDevice : InputDevice
{
	private Dictionary<KeyCode, Vector2Int> keyToDirection = new Dictionary<KeyCode, Vector2Int>()
	{
		{KeyCode.UpArrow,Vector2Int.down},
		{KeyCode.DownArrow,Vector2Int.up},
		{KeyCode.RightArrow,Vector2Int.right},
		{KeyCode.LeftArrow,Vector2Int.left}
	};
	
	public override void UpdateInput()
	{
		if (listener == null)
		{
			return;
		}

		foreach (var keyDirPair in keyToDirection)
		{
			if (Input.GetKeyDown(keyDirPair.Key))
			{
				listener.HandleInput(keyDirPair.Value);
			}
		}
	}

	public override bool AnyKeyDown()
	{
		return Input.anyKeyDown;
	}
}