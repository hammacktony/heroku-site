import { Component, OnInit, OnDestroy } from '@angular/core';
import { BlogService } from 'src/app/services/blog/blog.service';
import { Header } from 'src/app/models/header.model';
import { ConfigService } from 'src/app/services/config.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.scss']
})
export class PostComponent implements OnInit, OnDestroy {
  currentHeader: Header = new Header();

  subscriptions: any[] = [];
  blog: string;
  slug: string;
  post: any;
  body: string = "";

  constructor(private route: ActivatedRoute, private _blog: BlogService) { }

  ngOnInit() {
    this.blog = this.route.snapshot.url[0].path;
    this.subscriptions.push(this.route.params.subscribe(params => this.slug = params.slug));
    this.onLoad();
  }

  setHeader(): void {
    this.currentHeader.title = this.post["title"];
    this.currentHeader.image = `url(${ConfigService.S3_LOCATION}/${this.post["image"]})`;
  }

  onLoad(): void {
    this.subscriptions.push(this._blog.get(this.blog, this.slug).subscribe(data => { this.post = data[0]; this.body = this.post["body"]; this.setHeader() }));
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(x => x.unsubscribe())
  }

}
