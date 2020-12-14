using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DestroyBytime : MonoBehaviour
{public float lifetime = 5;

 
     void Update ()
     {
         Destroy (GameObject.Find("bird(Clone)"), lifetime);
     }
 }