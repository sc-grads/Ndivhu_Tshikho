import { Component } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html'
})
export class RegisterComponent {
  registerForm: FormGroup;

  constructor(private fb: FormBuilder, private authService: AuthService) {
    this.registerForm = this.fb.group({
      username: [''],
      email: [''],
      password: ['']
    });
  }

  onRegister(): void {
    this.authService.register(this.registerForm.value).subscribe(
      response => {
        console.log('User registered successfully', response);
      },
      error => {
        console.error('Error registering user', error);
      }
    );
  }
}
