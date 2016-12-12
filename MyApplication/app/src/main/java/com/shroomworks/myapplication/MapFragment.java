package com.shroomworks.myapplication;

import android.app.Activity;
import android.os.Bundle;
import android.support.v4.app.ActivityCompat;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentTransaction;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.MapView;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;


public class MapFragment extends Fragment implements OnMapReadyCallback {

    private Map<Integer, Marker> dictionary = new HashMap<Integer, Marker>();

    private MapView mapView;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_map, container, false);
    }

    @Override
    public void onViewCreated(View view, Bundle savedInstanceState) {
        mapView = (MapView) view.findViewById(R.id.map);
        mapView.onCreate(savedInstanceState);
        mapView.onResume();
        mapView.getMapAsync(this);
    }

    @Override
    public void onMapReady(GoogleMap googleMap) {
        LatLng london = new LatLng(51.5074, 0.1278);
        for (int i = 0; i < 10; i++) {
            Random rand = new Random();
            int lat = rand.nextInt(80 + 80) - 80;
            int lng = rand.nextInt(170 + 170) - 170;
            addShroom(i, lat, lng, googleMap);
        }
        googleMap.setOnMarkerClickListener(new GoogleMap.OnMarkerClickListener() {
            @Override
            public boolean onMarkerClick(Marker marker) {
                //openSingle(marker.getTitle());
                return true;
            }
        });
        googleMap.moveCamera(CameraUpdateFactory.newLatLng(london));
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