package com.shroomworks.myapplication;

import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.net.Uri;
import android.os.Environment;
import android.provider.MediaStore;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.os.Bundle;
import android.support.v4.app.ActivityCompat;
import android.support.v4.app.FragmentActivity;
import android.support.v4.content.FileProvider;
import android.util.Base64;
import android.view.MenuItem;
import android.view.View;
import android.widget.ImageView;
import android.widget.Toast;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.VolleyLog;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends FragmentActivity implements LocationListener {

    protected LocationManager locationManager;
    protected Context context;
    protected double latitude,longitude;
    protected boolean gps_enabled,network_enabled;
    private BottomNavigationView bottomNavigationView;
    private int mSelectedItem;
    private String lastTag = null;

    String mCurrentPhotoPath;
    String encodedPic = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bottomNavigationView = (BottomNavigationView) findViewById(R.id.bottom_navigation);
        navigationManager();
        locationManager();
        initialSetup();
    }

    private void locationManager() {
        ActivityCompat.requestPermissions(this,new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION}, 1);

        if (checkLocationPermission()) {
            locationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
            locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 0, this);
        }

    }

    public boolean checkLocationPermission() {
        String permission = "android.permission.ACCESS_FINE_LOCATION";
        int res = this.checkCallingOrSelfPermission(permission);
        return (res == PackageManager.PERMISSION_GRANTED);
    }

    private void navigationManager() {

        bottomNavigationView.setOnNavigationItemSelectedListener(
                new BottomNavigationView.OnNavigationItemSelectedListener() {
                    @Override
                    public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                        selectFragment(item);
                        return false;
                    }
                });
    }

    private void initialSetup() {
        android.support.v4.app.FragmentManager fm = getSupportFragmentManager();
        android.support.v4.app.FragmentTransaction ft = fm.beginTransaction();
        MapFragment frag = new MapFragment();
        lastTag = "frag";
        ft.add(R.id.container, frag, lastTag);
        ft.commit();
    }

    private void selectFragment(MenuItem item) {
        android.support.v4.app.FragmentManager fm = getSupportFragmentManager();
        if (lastTag != null) {
            android.support.v4.app.Fragment currentFragment = fm.findFragmentByTag(lastTag);
            if (currentFragment != null) {
                android.support.v4.app.FragmentTransaction ft = fm.beginTransaction();
                ft.remove(currentFragment);
                ft.commit();
            }
        }
        android.support.v4.app.FragmentTransaction ft = fm.beginTransaction();
        switch (item.getItemId()) {
            case R.id.action_map:
                MapFragment frag = new MapFragment();
                lastTag = "frag";
                ft.add(R.id.container, frag, lastTag);
                ft.commit();
                break;
            case R.id.action_newsfeed:
                NewsFeedFragment frag2 = new NewsFeedFragment();
                lastTag = "frag2";
                ft.add(R.id.container, frag2, lastTag);
                ft.commit();
                break;
            case R.id.action_profile:
                dispatchTakePictureIntent();
                Bundle bundle = new Bundle();
                bundle.putString("mCurrentPhotoPath", mCurrentPhotoPath);
                CreatePostFragment frag3 = new CreatePostFragment();
                frag3.setArguments(bundle);
                lastTag = "frag3";
                ft.add(R.id.container, frag3, lastTag);
                ft.commit();
                break;
        }

        // update selected item
        mSelectedItem = item.getItemId();

        // uncheck the other items.
        for (int i = 0; i< bottomNavigationView.getMenu().size(); i++) {
            MenuItem menuItem = bottomNavigationView.getMenu().getItem(i);
            menuItem.setChecked(menuItem.getItemId() == item.getItemId());
        }
    }

    static final int REQUEST_TAKE_PHOTO = 1;

    private void dispatchTakePictureIntent() {
        Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        // Ensure that there's a camera activity to handle the intent
        if (takePictureIntent.resolveActivity(getPackageManager()) != null) {
            // Create the File where the photo should go
            File photoFile = null;
            try {
                photoFile = createImageFile();
            } catch (IOException ex) {
                // Error occurred while creating the File
            }
            // Continue only if the File was successfully created
            if (photoFile != null) {
                Uri photoURI = FileProvider.getUriForFile(this,
                        "com.shroomworks.myapplication.fileprovider",
                        photoFile);
                takePictureIntent.putExtra(MediaStore.EXTRA_OUTPUT, photoURI);
                startActivityForResult(takePictureIntent, REQUEST_TAKE_PHOTO);
                galleryAddPic();
            }
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        //setPic();
    }

    private File createImageFile() throws IOException {
        // Create an image file name
        String timeStamp = new SimpleDateFormat("yyyyMMdd_HHmmss").format(new Date());
        String imageFileName = "JPEG_" + timeStamp + "_";
        File storageDir = getExternalFilesDir(Environment.DIRECTORY_PICTURES);
        File image = File.createTempFile(
                imageFileName,  /* prefix */
                ".jpg",         /* suffix */
                storageDir      /* directory */
        );

        // Save a file: path for use with ACTION_VIEW intents
        mCurrentPhotoPath = image.getAbsolutePath();
        return image;
    }

    private void galleryAddPic() {
        Intent mediaScanIntent = new Intent(Intent.ACTION_MEDIA_SCANNER_SCAN_FILE);
        File f = new File(mCurrentPhotoPath);
        Uri contentUri = Uri.fromFile(f);
        mediaScanIntent.setData(contentUri);
        this.sendBroadcast(mediaScanIntent);
    }

    public void postPicture(View view) {
        encodePicture();
        RequestQueue queue = Volley.newRequestQueue(this);

        final String URL = "http://aws-env.cjiqjg5vbi.us-west-2.elasticbeanstalk.com/api/create_post_kamil";

        Map<String,String> params = new HashMap<String, String>();

        params.put("image",null);
        params.put("lat",String.valueOf(latitude));
        params.put("lon",String.valueOf(longitude));
        params.put("caption","Test post");

        // pass second argument as "null" for GET requests
        JsonObjectRequest req = new JsonObjectRequest(URL, new JSONObject(params),
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        try {
                            VolleyLog.v("Response:%n %s", response.toString(4));
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                VolleyLog.e("Error: ", error.getMessage());
            }
        });
        // Add the request to the RequestQueue.
        queue.add(req);

    }

    public void encodePicture() {
        Bitmap bm = BitmapFactory.decodeFile(mCurrentPhotoPath);
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        bm.compress(Bitmap.CompressFormat.JPEG, 100, baos); //bm is the bitmap object
        byte[] b = baos.toByteArray();
        encodedPic = Base64.encodeToString(b, Base64.DEFAULT);
    }

    @Override
    public void onLocationChanged(Location location) {
        latitude = location.getLatitude();
        longitude = location.getLongitude();
        System.out.println("Latitude: " + latitude + ", Longitude: " + longitude);
    }

    @Override
    public void onProviderDisabled(String provider) {
        System.out.println("Latitude" + "disable");
    }

    @Override
    public void onProviderEnabled(String provider) {
        System.out.println("Latitude" + "enable");
    }

    @Override
    public void onStatusChanged(String provider, int status, Bundle extras) {
        System.out.println("Latitude" + "status");
    }

}
