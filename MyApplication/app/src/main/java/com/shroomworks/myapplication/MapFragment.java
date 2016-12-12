package com.shroomworks.myapplication;

import android.app.Activity;
import android.content.Intent;
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
        googleMap.moveCamera( CameraUpdateFactory.newLatLngZoom(london , 4.0f) );

        addShroom(1, R.raw.thumbnail1, 34.457273, 6.191111, googleMap);
        addShroom(2, R.raw.thumbnail2, 38.660948, -2.832371, googleMap);
        addShroom(3, R.raw.thumbnail3, 41.622547, 13.241491, googleMap);
        addShroom(4, R.raw.thumbnail4, 45.275715, 2.530006, googleMap);
        addShroom(5, R.raw.thumbnail5, 47.543471, 9.013686, googleMap);
        addShroom(6, R.raw.thumbnail6, 57.066100, -4.443216, googleMap);
        // addShroom(7, R.raw.thumbnail7, 51.640808, -0.149897, googleMap);
        addShroom(8, R.raw.thumbnail8, 51.646455, 6.691372, googleMap);
        addShroom(9, R.raw.thumbnail9, 52.736266, 12.276732, googleMap);
        addShroom(10, R.raw.thumbnail10, 49.270427, 17.363879, googleMap);
        addShroom(11, R.raw.thumbnail11, 44.645009, 23.553241, googleMap);
        addShroom(12, R.raw.thumbnail12, 61.305673, 6.729652, googleMap);
        addShroom(13, R.raw.thumbnail13, 58.816978, 16.900343, googleMap);
        addShroom(14, R.raw.thumbnail14, 55.106565, 24.384436, googleMap);
        addShroom(15, R.raw.thumbnail15, 49.358012, 29.990032, googleMap);
        addShroom(16, R.raw.thumbnail16, 37.881976, 30.909031, googleMap);
        addShroom(17, R.raw.thumbnail17, 44.102645, 37.145775, googleMap);
        addShroom(18, R.raw.thumbnail18, 34.554323, 43.478470, googleMap);
        addShroom(19, R.raw.thumbnail19, 40.484530, 49.139515, googleMap);
        addShroom(20, R.raw.thumbnail20, 43.964683, 60.077805, googleMap);
        addShroom(21, R.raw.thumbnail21, 58.221728, 36.556270, googleMap);
        addShroom(22, R.raw.thumbnail22, 60.605470, 56.939094, googleMap);
        addShroom(23, R.raw.thumbnail23, 53.713835, 47.565175, googleMap);
        addShroom(24, R.raw.thumbnail24, 52.146938, 59.432245, googleMap);

        googleMap.setOnMarkerClickListener(new GoogleMap.OnMarkerClickListener() {
            @Override
            public boolean onMarkerClick(Marker marker) {
                openSingle(marker.getTitle());
                return true;
            }
        });
        googleMap.moveCamera(CameraUpdateFactory.newLatLng(london));
    }

    public void addShroom(int id, int iconNumber, double lat, double lng, GoogleMap googleMap) {
        LatLng position = new LatLng((float)lat, (float)lng);

        Marker shroom = googleMap.addMarker(new MarkerOptions()
                .position(position)
                .title(Integer.toString(id))
                .icon(BitmapDescriptorFactory.fromResource(iconNumber))
                .anchor((float)0.5, (float)0.5)
        );

        dictionary.put(id, shroom);
    }

    public void openSingle(String title) {
        MainActivity activity = (MainActivity) getActivity();
        activity.openSingle(title);
    }


}