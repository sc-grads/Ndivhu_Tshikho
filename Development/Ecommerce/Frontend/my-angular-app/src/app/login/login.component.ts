import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username: string = '';
  password: string = '';

  constructor(private http: HttpClient, private router: Router) {}

  onSubmit(): void {
    const loginData = { username: this.username, password: this.password };
    this.http.post('http://localhost:5000/auth/login', loginData).subscribe(
      (response: any) => {
        alert('Login successful');
        this.router.navigate(['/']); // Redirect to the home page after login
      },
      (error) => {
        alert('Login failed: ' + error.error.message);
      }
    );
  }
}
