using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;

[CustomEditor(typeof(BoardView))]
public class BoardInspector : Editor
{
	public override void OnInspectorGUI()
	{
		BoardView boardView = target as BoardView;
		base.OnInspectorGUI();
		if (GUILayout.Button("Clear"))
		{
			boardView.Clear();
		}
	}
}
