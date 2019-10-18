import { TestBed } from '@angular/core/testing';
import { HttpModule } from '@angular/http';

import { UserService } from './user.service';

describe('UserService', () => {
  beforeEach(() => TestBed.configureTestingModule({
    imports: [ HttpModule ],
  }));

  it('should be created', () => {
    const service: UserService = TestBed.get(UserService);
    expect(service).toBeTruthy();
  });
});
