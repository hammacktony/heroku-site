import { Component, OnInit } from '@angular/core';
import { ConfigService } from 'src/app/services/config.service';
import { Header } from 'src/app/models/header.model';

@Component({
  selector: 'app-error',
  templateUrl: './error.component.html',
  styleUrls: ['./error.component.scss']
})
export class ErrorComponent implements OnInit {
  currentHeader: Header = new Header();

  constructor() { }

  ngOnInit() {
    this.setHeader()
  }

  setHeader(): void {
    this.currentHeader.title = "Error";
    this.currentHeader.subtitle = "Sorry for the inconvience!";
    this.currentHeader.image = `url(${ConfigService.S3_LOCATION}/blog/img/glitch.png)`;
  }

}
