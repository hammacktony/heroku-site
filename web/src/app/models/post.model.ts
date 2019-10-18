export class Post {
    title: string;
    category: string;
    body: string;
    image: string;
    is_live: boolean;

    constructor(title?: string, category?: string, body?: string, image?: string, is_live: boolean = true) {
        this.title = title || '';
        this.category = category || '';
        this.body = body || '';
        this.image = image || "";
        this.is_live = is_live;
    }
}