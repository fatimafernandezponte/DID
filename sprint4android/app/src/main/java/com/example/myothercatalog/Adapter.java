package com.example.myothercatalog;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class Adapter extends RecyclerView.Adapter<AnimalitosViewHolder> {

    private List<AnimalitosData> allTheData;
    private Activity activity;



    //El método constructor del Adapter recibe una lista con todos los datos a cargar.
    public Adapter(List<AnimalitosData> dataset, Activity activity) {
        this.allTheData = dataset;
        this.activity = activity;
    }

    //Aquí creamos una celda.
    public AnimalitosViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType){
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.animalitos_view_holder, parent, false);
        //Aquí invocamos el constructor de AnimalitosViewHolder
        return new AnimalitosViewHolder(view);
    }

    //Aquí le pasamos a la celda el contenido que debe mostrar según su posición, dependiendo de hasta dónde scrollee el usuario
    public void onBindViewHolder(AnimalitosViewHolder holder, int position){
        AnimalitosData dataIntPositionToBeRendered = allTheData.get(position);
        holder.showData(dataIntPositionToBeRendered, activity);

        //EJERCICIO 2:
        //Configuramos el OnClickListener para la celda
        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                //Obtenemos el elmento de datos en la posición clicada
                int adapterPosition = holder.getAdapterPosition();
                AnimalitosData elementoClickado = allTheData.get(adapterPosition);

                //Instanciamos la actividad
                Intent intent = new Intent(activity, DetailActivity.class);
                //EJERCICIO 3
                //Utilizamos putExtra para pasar los datos a la DetailActivity
                intent.putExtra("name", elementoClickado.getName());
                intent.putExtra("description", elementoClickado.getDescription());
                intent.putExtra("image_url", elementoClickado.getImageUrl());
                //Iniciamos la actividad
                activity.startActivity(intent);


            }
        });
    }

    //Aquí devolvemos el número total de elementos de la lista
    public int getItemCount() {
        return allTheData.size();
    }
}
