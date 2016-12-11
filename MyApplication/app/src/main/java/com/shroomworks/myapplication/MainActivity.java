package com.shroomworks.myapplication;

import android.app.Fragment;
import android.app.FragmentManager;
import android.app.FragmentTransaction;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.view.MenuItem;

public class MainActivity extends FragmentActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        navigationManager();

    }

    private void navigationManager() {
        BottomNavigationView bottomNavigationView = (BottomNavigationView)
                findViewById(R.id.bottom_navigation);


        bottomNavigationView.setOnNavigationItemSelectedListener(
                new BottomNavigationView.OnNavigationItemSelectedListener() {
                    @Override
                    public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                        switch (item.getItemId()) {
                            case R.id.action_map:
                                addFragment();
                                break;
                            case R.id.action_newsfeed:
                                addFragment();
                                break;
                            case R.id.action_profile:
                                addFragment();
                                break;
                        }
                        return false;
                    }
                });
    }

    private void addFragment() {
        getSupportFragmentManager().beginTransaction().add(R.id.contentFragment, new NewsfeedFragment()).commit();
    }

}
