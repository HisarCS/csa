using UnityEngine;
using UnityEngine.SceneManagement;

public class adamscript : MonoBehaviour {

	public Rigidbody2D rb;

	void Update () {

		if (Input.GetKeyDown(KeyCode.RightArrow)){
			rb.MovePosition(rb.position + Vector2.right);
            
        }
		 if (Input.GetKeyDown(KeyCode.LeftArrow)){
			rb.MovePosition(rb.position + Vector2.left);
          
         }
		 if (Input.GetKeyDown(KeyCode.UpArrow))
			rb.MovePosition(rb.position + Vector2.up);
		
	}
}