using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu]
public class GameSettings : ScriptableObject
{
	public Vector2Int boardSize;
	public bool useBorders;
	public int initialSnakeWidth;
	public Vector2Int initialSnakePosition;
	public Vector2Int initialSnakeDirection = Vector2Int.up;
}