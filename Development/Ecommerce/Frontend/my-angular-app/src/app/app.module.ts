import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';  // Ensure this is imported

import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';  // Import your component

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,  // Declare your component here
    // Other components...
  ],
  imports: [
    BrowserModule,
    FormsModule,  // Add FormsModule here
    // Other modules...
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
