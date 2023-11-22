package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class Adapter extends RecyclerView.Adapter<GatitosViewHolder> {

    private List<GatitoData> allTheData;
    private Activity activity;

    //El método constructor del Adapter recibe una lista con todos los datos a cargar.
    public Adapter(List<GatitoData> dataset, Activity activity) {
        this.allTheData = dataset;
        this.activity = activity;
    }

    //Aquí creamos una celda.
    public GatitosViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType){
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.gatito_view_holder, parent, false);
        //Aquí invocamos el constructor de GatitosViewHolder
        return new GatitosViewHolder(view);
    }

    //Aquí le pasamos a la celda el contenido que debe mostrar según su posición, dependiendo de hasta dónde scrollee el usuario
    public void onBindViewHolder(GatitosViewHolder holder, int position){
        GatitoData dataIntPositionToBeRendered = allTheData.get(position);
        holder.showData(dataIntPositionToBeRendered, activity);
    }

    //Aquí devolvemos el número total de elementos de la lista
    public int getItemCount() {
        return allTheData.size();
    }
}
