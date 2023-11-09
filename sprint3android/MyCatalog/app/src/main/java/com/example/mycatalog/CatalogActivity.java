package com.example.mycatalog;

import androidx.annotation.NonNull;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;

import com.google.android.material.navigation.NavigationView;

public class CatalogActivity extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener {


    // Creamos un archivo layout drawer_header que será el nombre del menu cuando se despliegue
    // Creamos un archivo layout drawer_toolbar
    // Creamos un archivo layout containt_main que será el contenedor de los fragment
    // Creamos un nuevo android resource file drawer_menu en res, type menu
    // Creamos un item para cada elemento del menu
    // Añadimos dos include (toolbar y container) para mostrarlos en la actividad y un NavigationView en el layout ligado a la actividad
    // Añadimos el menú y el header al navigationView para que se muestren al desplegarlo
    // Cambiamos DetailActivity y AboutActivity a extends Fragments y hacemos el metodo onCreateView para poder trabajar con ellos en el drawer_menu
    // Hecho eso, ya podemos empezar a trabajar en la actividad

    DrawerLayout drawerLayout;
    ActionBarDrawerToggle actionBarDrawerToggle;
    Toolbar toolbar;
    NavigationView navigationView;
    FragmentManager fragmentManager;
    FragmentTransaction fragmentTransaction;
    private Context context;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_catalog);

        context = this;
        //Iniciamos la toolbar
        toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        //Iniciamos el drawerLayout
        drawerLayout = findViewById(R.id.drawer);

        //Iniciamos el navigationView
        navigationView = findViewById(R.id.navigationView);
        navigationView.setNavigationItemSelectedListener(this);

        actionBarDrawerToggle = new ActionBarDrawerToggle(this, drawerLayout, toolbar, R.string.open, R.string.close);
        drawerLayout.addDrawerListener(actionBarDrawerToggle);
        actionBarDrawerToggle.setDrawerIndicatorEnabled(true);
        actionBarDrawerToggle.syncState();

        //Cargamos el primer fragment (PrimeraPantalla)
        fragmentManager = getSupportFragmentManager();
        fragmentTransaction = fragmentManager.beginTransaction();
        fragmentTransaction.add(R.id.container, new PrimeraPantalla());
        fragmentTransaction.commit();

    }


    public boolean onNavigationItemSelected(@NonNull MenuItem item) {
        //Esto sirve para que una vez se haya clickado en un fragment el toolbar se cierre de forma automática
        drawerLayout.closeDrawer(GravityCompat.START);

        //Usamos el ID de cada fragmento/item para saber a que actividad corresponde
        if (item.getItemId() == R.id.personas){
            //Reemplazamos el fragment actual por el que corresponde a AboutActivity
            fragmentManager = getSupportFragmentManager();
            fragmentTransaction = fragmentManager.beginTransaction();
            fragmentTransaction.replace(R.id.container, new AboutActivity());
            fragmentTransaction.commit();
        }

        if (item.getItemId() == R.id.home){
            //Reemplazamos el fragment actual por el que corresponde a DetailActivity
            fragmentManager = getSupportFragmentManager();
            fragmentTransaction = fragmentManager.beginTransaction();
            fragmentTransaction.replace(R.id.container, new DetailActivity());
            fragmentTransaction.commit();
        }

        return false;
    }


}
