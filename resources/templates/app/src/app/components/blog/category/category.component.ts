import { Component, OnInit, OnDestroy } from '@angular/core';
import { Header } from 'src/app/models/header.model';
import { ConfigService } from 'src/app/services/config.service';
import { Router, ActivatedRoute } from '@angular/router';
import { BlogService } from 'src/app/services/blog/blog.service';


@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.scss']
})
export class CategoryComponent implements OnInit, OnDestroy {
  currentHeader: Header = new Header();

  subscriptions: any[] = [];
  category: string;
  blog: string;
  posts: any[] = [];

  blogs = { 'personal': { 'name': 'Personal', 'image': 'blog/img/categories.jpg' }, 'tech': { 'name': 'Tech', 'image': 'blog/img/library-2.jpg' } };

  constructor(private router: Router, private route: ActivatedRoute, private _blog: BlogService) { }

  ngOnInit() {
    this.blog = this.route.snapshot.url[0].path;
    this.subscriptions.push(this.route.params.subscribe(params => this.category = params.category));
    this.onLoad();
  }

  onLoad(): void {
    this.setHeader();
    this.subscriptions.push(this._blog.all(this.blog, { "category": this.category }).subscribe(data => this.posts = data));
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(x => x.unsubscribe())
  }

  navigate(data): void {
    this.router.navigate([this.blog, data.slug]);
  }

  setHeader(): void {
    this.currentHeader.title = this.category;
    this.currentHeader.image = `url(${ConfigService.S3_LOCATION}/${this.blogs[this.blog]["image"]})`;
  }

}
