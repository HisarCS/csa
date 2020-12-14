  
using UnityEngine;

public class birdscript : MonoBehaviour {

	public Rigidbody2D rb;
    public GameObject gg;
	public float minSpeed = 8f;
	public float maxSpeed = 12f;
   
	float speed = 1f;

	void Start ()
	{
		speed = Random.Range(minSpeed, maxSpeed);
	}

	void FixedUpdate () {
       
        Vector3 notnice = new Vector3(3.9f, transform.position.y, 0.0f);
        Vector3 nice = new Vector3(-3.9f, transform.position.y, 0.0f);
		Vector2 forward = new Vector2(transform.right.x, transform.right.y + 0.05f);
		rb.MovePosition(rb.position + forward * Time.fixedDeltaTime * speed);
        if(transform.position.x > 4){
            rb.MovePosition(nice);
            Debug.Log("!");
        }
        if(transform.position.x < -4){
            rb.MovePosition(notnice);
            Debug.Log("!");
        }
	}

   void OnCollisionEnter2D (Collision2D col){
        if(col.gameObject.tag == "platform"){
        Debug.Log("Collision");
        if(transform.rotation.z >=180){
        transform.eulerAngles = Vector3.forward *(transform.rotation.z - 180);
        }
        else {
             transform.eulerAngles = Vector3.forward *(transform.rotation.z + 180);
        }
   }
         if(col.gameObject.tag == "adam"){
        Debug.Log("Collision");
       Destroy(GameObject.Find("bird(Clone)"));
       Instantiate(gg, new Vector3(transform.position.x, transform.position.y, 0), Quaternion.identity);
        transform.eulerAngles = Vector3.forward *(transform.rotation.z + 180);
        }
   }

}
