package com.shroomworks.myapplication;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import java.util.ArrayList;

public class NewsFeedActivity extends AppCompatActivity {

    private ListView newsFeedContentView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_news_feed);
        setTitle("News feed");

        newsFeedContentView = (ListView) findViewById(R.id.news_feed_content_view);
        final ArrayList<Recipe> recipeList = Recipe.getRecipesFromFile("recipes.json", this);

        String[] listItems = new String[recipeList.size()];

        for(int i = 0; i < recipeList.size(); i++){
            Recipe recipe = recipeList.get(i);
            listItems[i] = recipe.title;
        }

        ArrayAdapter adapter = new ArrayAdapter(this, android.R.layout.simple_list_item_1, listItems);
        newsFeedContentView.setAdapter(adapter);


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

    public void openDisplayPost(View view) {
        Intent intent = new Intent(this, FullScreenPostActivity.class);
        startActivity(intent);
    }



}