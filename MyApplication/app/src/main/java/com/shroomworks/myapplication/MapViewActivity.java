package com.shroomworks.myapplication;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class MapViewActivity extends AppCompatActivity implements OnMapReadyCallback {

    private Map<Integer, Marker> dictionary = new HashMap<Integer, Marker>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_map_view);
        setTitle("Map View");
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);
    }

    public void openNewsFeed(View view) {
        Intent intent = new Intent(this, NewsFeedActivity.class);
        startActivity(intent);
    }

    public void openMap(View view) {
        Intent intent = new Intent(this, MapViewActivity.class);
        startActivity(intent);
    }

    public void openUserProfile(View view) {
        Intent intent = new Intent(this, UserProfileActivity.class);
        startActivity(intent);
    }

    public void openCreatePost(View view) {
        Intent intent = new Intent(this, CreatePostActivity.class);
        startActivity(intent);
    }

    public void openSingle(String title) {
        Intent intent = new Intent(this, FullScreenPostActivity.class);
        intent.putExtra("title", title);
        startActivity(intent);
    }

    @Override
    public void onMapReady(GoogleMap googleMap) {
        LatLng sydney = new LatLng(-33.852, 151.211);
        for (int i = 0; i < 10; i++) {
            Random rand = new Random();
            int lat = rand.nextInt(80 + 80) - 80;
            int lng = rand.nextInt(170 + 170) - 170;
            addShroom(i, lat, lng, googleMap);
        }
        googleMap.setOnMarkerClickListener(new GoogleMap.OnMarkerClickListener() {
            @Override
            public boolean onMarkerClick(Marker marker) {
                openSingle(marker.getTitle());
                return true;
            }
        });
        googleMap.moveCamera(CameraUpdateFactory.newLatLng(sydney));
    }

    public void addShroom(int id, float lat, float lng, GoogleMap googleMap) {
        LatLng position = new LatLng(lat, lng);
        Marker shroom = googleMap.addMarker(new MarkerOptions()
                .position(position)
                .title(Integer.toString(id))
                .icon(BitmapDescriptorFactory.fromResource(R.drawable.shroomthumb))
        );
        dictionary.put(id, shroom);
    }

}
