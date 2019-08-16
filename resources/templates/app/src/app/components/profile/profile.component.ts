import { Component, OnInit, OnDestroy } from '@angular/core';
import { ConfigService } from 'src/app/services/config.service';
import { UserService } from 'src/app/services/user/user.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit, OnDestroy {
  data: any;
  user: string = 'tonus';
  image: string;
  subscriptions: any[] = [];

  constructor(private _user: UserService) { }

  ngOnInit(): void {
    this.loadUser();
  }

  loadUser(): void {
    this.subscriptions.push(this._user.get(this.user).subscribe(data => {
      this.data = data[0];
      this.data["image"] = `${ConfigService.S3_LOCATION}/${this.data["image"]}`;
    }));
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(x => x.unsubscribe())
  }

}
