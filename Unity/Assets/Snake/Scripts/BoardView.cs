using System.Collections;
using System.Collections.Generic;
using System.Data.SqlTypes;
using System.Linq;
using UnityEngine;
using UnityEngine.UI;

public class BoardView : MonoBehaviour
{
	[SerializeField] private GameObject fieldTemplate;
	[SerializeField] private GameObject[] fields;

	public float offset;
	private int width;
	private int height;

	public void Redraw(GameState gameState)
	{
		var coords = new Vector2Int();
		for (int y = 0; y < height; ++y)
		{
			for (int x = 0; x < width; ++x)
			{
				coords.x = x;
				coords.y = y;
				fields[GetIndexFromCoords(x,y)].SetActive(IsFieldEmpty(coords,gameState));
			}
		}
	}
	
	public void Generate(int width, int height)
	{
		this.width = width;
		this.height = height;
		Clear();
		fields = new GameObject[width*height];
		Vector2 maxSize = new Vector2()
		{
			x = width * (GetFieldSize() + offset),
			y = height * (GetFieldSize() + offset)
		};
		for (int y = 0; y < height; y += 1)
		{
			for(int x=0; x< width; x+=1)
			{
				float size = (GetFieldSize() + offset);
				Vector2 fieldPosition = new Vector2(-maxSize.x/2 + x*size,maxSize.y/2 -y*size);
				GameObject newField = Instantiate(fieldTemplate, transform);
				newField.transform.localPosition = fieldPosition;
				newField.isStatic = true;
				fields[GetIndexFromCoords(x, y)] = newField;
//				newField.SetActive(false);
			}
		}
	}
	
	public void Clear()
	{
		foreach (var field in fields)
		{
			if (Application.isPlaying)
			{
				Destroy(field);
			}
			else
			{
				DestroyImmediate(field);
			}
		}
	}

	private float GetFieldSize()
	{
		return fieldTemplate.GetComponent<RectTransform>().rect.width;
	}
	
	private int GetIndexFromCoords(int x, int y)
	{
		return y * width + x;
	}

	private bool IsFieldEmpty(Vector2Int coords, GameState gameState)
	{
		return gameState.CurrentSnakeElements.Any(field => field == coords) ||
		       (gameState.currentPointLocation == coords);
	}
}
