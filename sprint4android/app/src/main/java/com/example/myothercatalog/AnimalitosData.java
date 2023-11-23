package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class AnimalitosData {
    private String name;
    private String imageUrl;
    //Añadimos description para el Ejercicio 3
    private String description;


    public AnimalitosData(JSONObject json) {
        try {
            this.name = json.getString("name");
            this.imageUrl = json.getString("image_url");
            this.description = json.getString("description");
        }catch (JSONException e){
            e.printStackTrace();
        }
    }

    public String getName(){return name;}
    public String getImageUrl(){return imageUrl;}

    public String getDescription(){return this.description;}
}
