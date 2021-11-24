import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MainComponent } from './main.component';
import { Routes, RouterModule } from '@angular/router';

import { ApiService } from '../api.service';


import { OfferListComponent } from './offer-list/offer-list.component';
import { OfferDetailComponent } from './offer-detail/offer-detail.component';

const routes: Routes = [
  {path: 'offers', component: MainComponent},
  {path: 'offers/{{offer.id}}', component: OfferDetailComponent}
];

@NgModule({
  declarations: [
    MainComponent,
    OfferListComponent,
    OfferDetailComponent
  ],
  imports: [
    CommonModule,
    RouterModule.forChild(routes)
  ],
  exports: [
    RouterModule
  ],
  providers: [
    ApiService
  ]
})
export class MainModule { }
