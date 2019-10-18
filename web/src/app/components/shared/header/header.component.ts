import { Component, OnInit, Input } from '@angular/core';
import { Header } from 'src/app/models/header.model';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  @Input() header: Header;
  
  constructor() { }

  ngOnInit() {
  }

}
