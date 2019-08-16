import { BrowserModule } from '@angular/platform-browser';
import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { HttpModule } from '@angular/http';
import { HttpClientModule } from '@angular/common/http';
import { MarkdownModule } from 'ngx-markdown';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { BlogComponent } from './components/blog/main/main.component';
import { PostComponent } from './components/blog/post/post.component';
import { ErrorComponent } from './components/error/error.component';
import { NavbarComponent } from './components/shared/navbar/navbar.component';
import { FooterComponent } from './components/shared/footer/footer.component';
import { HeaderComponent } from './components/shared/header/header.component';
import { ProfileComponent } from './components/profile/profile.component';
import { CategoryComponent } from './components/blog/category/category.component'

import { ConfigService } from 'src/app/services/config.service';
import { UserService } from 'src/app/services/user/user.service';
import { BlogService } from 'src/app/services/blog/blog.service';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    BlogComponent,
    PostComponent,
    ErrorComponent,
    NavbarComponent,
    FooterComponent,
    HeaderComponent,
    ProfileComponent,
    CategoryComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpModule, 
    HttpClientModule,
    MarkdownModule.forRoot()
  ],
  providers: [ConfigService, BlogService, UserService],
  bootstrap: [AppComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AppModule { }
