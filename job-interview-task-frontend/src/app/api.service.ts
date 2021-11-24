import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class ApiService {

  offersURL = "http://127.0.0.1:8000/api/offers/";
  categoriesURL = "http://127.0.0.1:8000/api/categories/";
  headers = new HttpHeaders({
    'Content-Type': 'application/json'
  });

  constructor(
    private httpClient: HttpClient
  ) { }

  getOffers() {
    return this.httpClient.get(this.offersURL, {headers: this.headers});
  }

  getCategories() {
    return this.httpClient.get(this.categoriesURL, {headers: this.headers});
  }

}
