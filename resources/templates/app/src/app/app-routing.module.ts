import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './components/home/home.component';
import { BlogComponent } from './components/blog/main/main.component';
import { PostComponent } from './components/blog/post/post.component';
import { CategoryComponent } from './components/blog/category/category.component';
import { ErrorComponent } from './components/error/error.component';


const routes: Routes = [
  { path: 'personal', component: BlogComponent },
  { path: 'personal/:slug', component: PostComponent },
  { path: 'personal/category/:category', component: CategoryComponent },
  { path: 'tech', component: BlogComponent },
  { path: 'tech/:slug', component: PostComponent },
  { path: 'tech/category/:category', component: CategoryComponent },
  { path: '', component: HomeComponent },
  // Errors
  { path: 'error', component: ErrorComponent },
  { path: '**', redirectTo: '/error' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { useHash: true })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
