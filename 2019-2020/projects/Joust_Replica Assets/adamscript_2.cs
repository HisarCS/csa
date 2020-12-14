using UnityEngine;
using UnityEngine.SceneManagement;

public class adamscript_2 : MonoBehaviour {
	int score  = 0;
	public Rigidbody2D rb;
bool checkCol = true;
	void Update () {
Vector2 forward = new Vector2(transform.right.x *0, transform.right.y - 0.5f);
		if(checkCol == false){
		rb.MovePosition(rb.position + forward * Time.fixedDeltaTime);
		}
		if (Input.GetKeyDown(KeyCode.RightArrow)){
			rb.MovePosition(rb.position + Vector2.right);
            
        }
		 if (Input.GetKeyDown(KeyCode.LeftArrow)){
			rb.MovePosition(rb.position + Vector2.left);
          
         }
		 if (Input.GetKeyDown(KeyCode.UpArrow))
			rb.MovePosition(rb.position + Vector2.up);
		
	}
	void OnCollisionEnter2D (Collision2D col){
        if(col.gameObject.tag == "platform"){
        Debug.Log("Collision");
        

        }
         if(col.gameObject.tag == "yer"){
        Debug.Log("Collision");
       
        }
		 if(col.gameObject.tag == "egg"){
        Debug.Log("Collision");
		score++;
		Debug.Log(score);
		Destroy(GameObject.Find("unnamed(Clone)"));
       
        }
   }
}