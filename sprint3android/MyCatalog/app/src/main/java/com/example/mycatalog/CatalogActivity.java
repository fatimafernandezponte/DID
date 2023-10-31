package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class CatalogActivity extends AppCompatActivity {
    //Creamos el botón
    private Button botonNavegacion;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_catalog);

        //Lo asociamos con el botón creado en activity_catalog
        botonNavegacion = findViewById(R.id.botonNavegacion);

        //con el OnClickListener le decimos qué hacer cuando se clicke
        botonNavegacion.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //Aquí lanzamos la actividad DetailActivity dentro del método OnClick
                Intent detalActivity = new Intent(CatalogActivity.this, DetailActivity.class);
                startActivity(detalActivity);

            }
        });
    }



}