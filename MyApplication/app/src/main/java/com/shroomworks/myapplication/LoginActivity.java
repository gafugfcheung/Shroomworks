package com.shroomworks.myapplication;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class LoginActivity extends AppCompatActivity {
    public final static String EXTRA_MESSAGE = "com.example.myfirstapp.MESSAGE";
    private static final String TAG = "LoginActivity";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
    }
    /** Called when the user clicks the Send button */
    public void sendMessage(View view) {

        EditText emailText = (EditText)findViewById(R.id.login_email);
        String emailValue = emailText.getText().toString();
        EditText passwordText = (EditText)findViewById(R.id.login_password);
        String passwordValue = passwordText.getText().toString();

        android.util.Log.v(TAG, "email=" + emailValue + " password=" + passwordValue);
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);
    }
}
