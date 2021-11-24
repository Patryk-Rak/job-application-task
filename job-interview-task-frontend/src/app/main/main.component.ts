import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  offers: any = [];
  categories: any = [];

  constructor(
    private apiService: ApiService
  ) { }

  ngOnInit() {
    this.getOffers();
    this.getCategories();

  }

  getOffers() {
    this.apiService.getOffers().subscribe(
      data => {
        this.offers = data;
      },
      error => console.log(error)
    );
  }

  getCategories() {
    this.apiService.getCategories().subscribe(
      data => {
        this.categories = data;
      },
      error => console.log(error)
    );
  }

}
