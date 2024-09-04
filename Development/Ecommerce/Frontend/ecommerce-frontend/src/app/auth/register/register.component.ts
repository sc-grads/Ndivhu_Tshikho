import { Component } from '@angular/core';
import { Router } from '@angular/router'; // Import Router
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  user = { username: '', email: '', password: '' };
  successMessage: string | null = null;
  errorMessage: string | null = null;

  constructor(private authService: AuthService, private router: Router) {} // Inject Router

  register() {
    this.authService.register(this.user).subscribe(
      response => {
        console.log('Registration successful', response);
        this.successMessage = 'Registration successful! Redirecting to login...';
        this.errorMessage = null;
        
        // Redirect after 2 seconds to the login page
        setTimeout(() => {
          this.router.navigate(['/login']);
        }, 2000);
      },
      error => {
        console.error('Registration failed', error);
        this.errorMessage = 'Registration failed. Please try again.';
        this.successMessage = null;
      }
    );
  }
}
