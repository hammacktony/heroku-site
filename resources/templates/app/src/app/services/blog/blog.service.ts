import { Injectable } from '@angular/core';
// import { HttpService } from 'src/app/services/http.service'
import { Subject, Observable } from 'rxjs';
import { ConfigService } from 'src/app/services/config.service';
import { Post } from 'src/app/models/post.model'
import { Http } from '@angular/http';

@Injectable({
  providedIn: 'root'
})
export class BlogService {

  private _collection$: Subject<any> = new Subject();
  get collection$() { return this._collection$.asObservable(); }

  constructor(private http: Http) { }

  public all(blog: string, query: any = null): Observable<any[]> {
    if (query) {
      var url = `${ConfigService.API_URL}/api/${blog}?`;
      for (let [key, value] of Object.entries(query)) {
        url = url + `${key}=${value}`
      };
      this.http
        .get(url)
        .subscribe((response: any) => {
          this._collection$.next(JSON.parse(response._body));
        });
    } else {
      this.http
        .get(`${ConfigService.API_URL}/api/${blog}`)
        .subscribe((response: any) => {
          this._collection$.next(JSON.parse(response._body));
        });
    }

    return this._collection$.asObservable();
  }

  public get(blog: string, slug: string): Observable<any[]> {
    this.http
      .get(`${ConfigService.API_URL}/api/${blog}/${slug}`)
      .subscribe((response: any) => {
        this._collection$.next(JSON.parse(response._body));
      });

    return this._collection$.asObservable();
  }

  public create(blog: string, payload: Post): Observable<any[]> {
    this.http
      .post(`${ConfigService.API_URL}/api/${blog}`, payload)
      .subscribe((response: any) => {
        this._collection$.next(JSON.parse(response._body));
      });

    return this._collection$.asObservable();
  }

  public update(blog: string, slug: string, payload: Post): Observable<any[]> {
    this.http
      .put(`${ConfigService.API_URL}/api/${blog}/${slug}`, payload)
      .subscribe((response: any) => {
        this._collection$.next(JSON.parse(response._body));
      });

    return this._collection$.asObservable();
  }

  public delete(blog: string, slug: string): Observable<any[]> {
    this.http
      .delete(`${ConfigService.API_URL}/api/${blog}/${slug}`)
      .subscribe((response: any) => {
        this._collection$.next(JSON.parse(response._body));
      });

    return this._collection$.asObservable();
  }
}
