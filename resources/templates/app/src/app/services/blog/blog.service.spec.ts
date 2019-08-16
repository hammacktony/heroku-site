import { TestBed } from '@angular/core/testing';
import { HttpModule } from '@angular/http';

import { BlogService } from './blog.service';

describe('BlogService', () => {
  beforeEach(() => TestBed.configureTestingModule({
    imports: [ HttpModule ],
  }));

  it('should be created', () => {
    const service: BlogService = TestBed.get(BlogService);
    expect(service).toBeTruthy();
  });
});
