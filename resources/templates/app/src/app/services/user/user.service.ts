import { Injectable } from '@angular/core';
// import { HttpService } from 'src/app/services/http.service'
import { Subject, Observable } from 'rxjs';
import { ConfigService } from 'src/app/services/config.service';
import { Http } from '@angular/http';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  private _collection$: Subject<any> = new Subject();
  get collection$() { return this._collection$.asObservable(); }

  constructor(private http: Http) { }

  public get(user: string): Observable<any[]> {
    this.http
      .get(`${ConfigService.API_URL}/api/user/${user}`)
      .subscribe((response: any) => {
        this._collection$.next(JSON.parse(response._body));
      });

    return this._collection$.asObservable();
  }
}
