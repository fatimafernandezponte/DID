package com.example.myothercatalog;

import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class GatitoData {
    private String name;
    private String imageUrl;


    public GatitoData(JSONObject json) {
        try {
            this.name = json.getString("name");
            this.imageUrl = json.getString("image_url");
        }catch (JSONException e){
            e.printStackTrace();
        }
    }

    public String getName(){return name;}
    public String getImageUrl(){return imageUrl;}
}
