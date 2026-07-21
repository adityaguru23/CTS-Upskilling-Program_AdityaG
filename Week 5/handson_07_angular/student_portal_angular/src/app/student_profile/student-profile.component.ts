import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-student-profile',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  template: `
    <form [formGroup]="profileForm" (ngSubmit)="onSubmit()">
      <div>
        <label>Name:</label>
        <input formControlName="name">
        <span *ngIf="profileForm.get('name')?.touched && profileForm.get('name')?.invalid">Name is required</span>
      </div>
      <div>
        <label>Email:</label>
        <input formControlName="email">
        <span *ngIf="profileForm.get('email')?.touched && profileForm.get('email')?.invalid">Enter a valid email</span>
      </div>
      <div>
        <label>Semester:</label>
        <input formControlName="semester" type="number">
      </div>
      <button type="submit" [disabled]="profileForm.invalid">Submit</button>
    </form>
  `
})
export class StudentProfileComponent {
  profileForm: FormGroup;

  constructor(private fb: FormBuilder) {
    this.profileForm = this.fb.group({
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      semester: ['', [Validators.required, Validators.min(1), Validators.max(8)]]
    });
  }

  onSubmit() {
    if (this.profileForm.valid) {
      console.log(this.profileForm.value);
    }
  }
}