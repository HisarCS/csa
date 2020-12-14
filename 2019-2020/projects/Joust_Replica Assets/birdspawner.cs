using UnityEngine;

public class birdspawner : MonoBehaviour
{
public float spawnDelay = .3f;

	public GameObject bird;

	public Transform[] spawnPoints;

	float nextTimeToSpawn = 0f;

	void Update ()
	{
		if (nextTimeToSpawn <= Time.time)
		{
			SpawnBird();
			nextTimeToSpawn = Time.time + spawnDelay;
		}
	}

	void SpawnBird ()
	{
		int randomIndex = Random.Range(0, spawnPoints.Length);
		Transform spawnPoint = spawnPoints[randomIndex];

		Instantiate(bird, spawnPoint.position, spawnPoint.rotation);
	}

}
