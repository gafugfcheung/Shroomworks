package com.shroomworks.myapplication;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class FullScreenPostActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_full_screen_post);
        setTitle("Full screen post");
        TextView t = (TextView)findViewById(R.id.titleLabel);
        Intent intent = getIntent();
        String title = intent.getStringExtra("title");
        t.setText(title);
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
}
