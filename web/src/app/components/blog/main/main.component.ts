import { Component, OnInit, OnDestroy } from '@angular/core';
import { BlogService } from 'src/app/services/blog/blog.service';
import { Header } from 'src/app/models/header.model';
import { ConfigService } from 'src/app/services/config.service';
import { Router, ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-blog',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class BlogComponent implements OnInit, OnDestroy {
  currentHeader: Header = new Header();

  subscriptions: any[] = [];
  blog: string = "";
  posts: any[] = [];

  blogs = { 'personal': { 'name': 'Personal', 'image': 'blog/img/blog-header.jpg' }, 'tech': { 'name': 'Tech', 'image': 'blog/img/laptop-blog.jpg' } };

  constructor(private router: Router, private route: ActivatedRoute, private _blog: BlogService) { }

  ngOnInit() {
    this.blog = this.route.snapshot.url[0].path;
    this.onLoad();
  }

  setHeader(): void {
    this.currentHeader.title = `${this.blogs[this.blog]["name"]} Thoughts`;
    this.currentHeader.image = `url(${ConfigService.S3_LOCATION}/${this.blogs[this.blog]["image"]})`;
  }

  onLoad(): void {
    this.setHeader();
    this.subscriptions.push(this._blog.all(this.blog).subscribe(data => this.posts = data));
  }

  navigate(data): void {
    this.router.navigate([this.blog, data.slug]);
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(x => x.unsubscribe());
  }

}
