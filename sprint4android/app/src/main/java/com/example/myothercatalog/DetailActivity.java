package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import com.bumptech.glide.Glide;

public class DetailActivity extends AppCompatActivity {
    private TextView titulo;
    private ImageView fotito;
    private TextView descripcion;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        //EJERCICIO 3
        //Obtenemos los datos
        Intent intent = getIntent(); //?
        String tit = intent.getStringExtra("name");
        String im = intent.getStringExtra("image_url");
        String des = intent.getStringExtra("description");

        renderizarDatos(tit, im, des);
    }

    private void renderizarDatos(String tit, String im, String des) {
        //Lo mostramos en la interfaz de usuario:
        titulo = findViewById(R.id.titulo);
        titulo.setText(tit);

        fotito = findViewById(R.id.fotito);
        Glide.with(this).load(im).into(fotito);

        descripcion = findViewById(R.id.descripcion);
        descripcion.setText(des);
    }
}