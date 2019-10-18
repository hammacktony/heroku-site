import { Component, OnInit } from '@angular/core';
import { ConfigService } from 'src/app/services/config.service';
import { Header } from 'src/app/models/header.model';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  currentHeader: Header = new Header();

  constructor() { }

  ngOnInit() {
    this.setHeader();
  }

  setHeader(): void {
    this.currentHeader.title = "Tony Hammack";
    this.currentHeader.subtitle = "Curious Tinkerer | hammack.tony@gmail.com";
    this.currentHeader.image = `url(${ConfigService.S3_LOCATION}/user/img/marketing-wallpaper-27.jpg)`;
  }
}
