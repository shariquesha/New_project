import { Component, OnInit } from '@angular/core';
import { AccountService } from '../account.service';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-account',
  templateUrl: './account.component.html',
  styleUrls: ['./account.component.css']
})
export class AccountComponent implements OnInit {

    public users = [];
  constructor(private accountservice : AccountService) { }

  ngOnInit() {
      this.accountservice.getAccount().subscribe(data => this.users = data);
  }

  add(post : any) {
    this.accountservice.updateAccount(post).subscribe(data => console.log('form submitted successfully'));
    // alert(JSON.stringify(post))
}

}
