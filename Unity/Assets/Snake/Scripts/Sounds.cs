using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Sounds : MonoBehaviour
{
    public AudioSource pointSource;
    private int lastScore = 0;

    public void Reset()
    {
        lastScore = 0;
    }
    
    public void UpdateSounds(GameState state)
    {
        if (state.score > lastScore)
        {
            PlayPointSound();
        }

        lastScore = state.score;
    }

    void PlayPointSound()
    {
        pointSource.Play();
    }
    
    
}
