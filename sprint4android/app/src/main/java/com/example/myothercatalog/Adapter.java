package com.example.myothercatalog;

import android.app.Activity;
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
    }

    //Aquí devolvemos el número total de elementos de la lista
    public int getItemCount() {
        return allTheData.size();
    }
}
