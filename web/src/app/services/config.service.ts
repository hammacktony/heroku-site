import { Injectable } from '@angular/core';

@Injectable({
    providedIn: 'root'
})
export class ConfigService {
    public static get S3_LOCATION(): string { return "//tony-hammack.s3-website.us-east-2.amazonaws.com" }
    public static get API_URL(): string { return `${document.location.protocol}//${document.location.hostname}` }

    constructor() { }
}