import {Injectable} from '@angular/core';
import {Http, Headers, RequestOptions} from '@angular/http';

@Injectable()
export class HttpService {
    constructor(private http: Http) {}

    createAuthorizationHeader(headers: Headers) {
        headers.append('x-access-token', localStorage.getItem('id_token'));
    }

    get(url, params = null) {
        return this.http.get(url, { params: params });
    }

    put(url, body = null) {
        const headers = new Headers();
        this.createAuthorizationHeader(headers);
        return this.http.put(url, body, { headers: headers });
    }

    delete(url, body = null) {
        const headers = new Headers();
        this.createAuthorizationHeader(headers);
        const options = new RequestOptions({
            headers: headers,
            body: body
        });

        return this.http.delete(url, options);
    }

    post(url, data) {
        const headers = new Headers();
        this.createAuthorizationHeader(headers);
        return this.http.post(url, data, { headers: headers });
    }
}
