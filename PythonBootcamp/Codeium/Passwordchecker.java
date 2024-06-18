package com.barosamu;

public class Passwordchecker(String password) {
    public boolean checkPassword(String password) {
        if (password.length() < 8) {
            return false;
        }   

        if (password.length() > 20) {
            return false;
        }   

        if(!password.matches( ".*[a-z].*")) {
            return false;
        }   

        if(!password.matches(".*[A-Z].*")) {
            return false;   

        }
        if(!password.matches(".*\\d.*")) {
            return false;
        }

        return true;
    }   
}