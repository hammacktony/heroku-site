(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["main"],{

/***/ "./$$_lazy_route_resource lazy recursive":
/*!******************************************************!*\
  !*** ./$$_lazy_route_resource lazy namespace object ***!
  \******************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

function webpackEmptyAsyncContext(req) {
	// Here Promise.resolve().then() is used instead of new Promise() to prevent
	// uncaught exception popping up in devtools
	return Promise.resolve().then(function() {
		var e = new Error("Cannot find module '" + req + "'");
		e.code = 'MODULE_NOT_FOUND';
		throw e;
	});
}
webpackEmptyAsyncContext.keys = function() { return []; };
webpackEmptyAsyncContext.resolve = webpackEmptyAsyncContext;
module.exports = webpackEmptyAsyncContext;
webpackEmptyAsyncContext.id = "./$$_lazy_route_resource lazy recursive";

/***/ }),

/***/ "./node_modules/raw-loader/index.js!./src/app/app.component.html":
/*!**************************************************************!*\
  !*** ./node_modules/raw-loader!./src/app/app.component.html ***!
  \**************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<!--The content below is only a placeholder and can be replaced.-->\n<app-navbar></app-navbar>\n<router-outlet></router-outlet>\n<app-footer></app-footer>"

/***/ }),

/***/ "./node_modules/raw-loader/index.js!./src/app/components/blog/category/category.component.html":
/*!********************************************************************************************!*\
  !*** ./node_modules/raw-loader!./src/app/components/blog/category/category.component.html ***!
  \********************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<app-header [header]=\"currentHeader\"></app-header>\n\n<article>\n    <div class=\"col-lg-9 col-md-10 mx-auto\">\n        <div class=\"post-preview\" style=\"text-align: center\">\n            <a *ngFor=\"let post of posts\" (click)=\"navigate(post)\">\n                <h2 class=\"post-title post\">\n                    {{ post.title }}\n                    <hr>\n                </h2>\n            </a>\n        </div>\n    </div>\n</article>"

/***/ }),

/***/ "./node_modules/raw-loader/index.js!./src/app/components/blog/main/main.component.html":
/*!************************************************************************************!*\
  !*** ./node_modules/raw-loader!./src/app/components/blog/main/main.component.html ***!
  \************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<app-header [header]=\"currentHeader\"></app-header>\n\n<div class=\"col-lg-9 col-md-10 mx-auto\">\n    <div class=\"post-preview\" style=\"text-align: center\">\n        <ng-container *ngIf=\"posts\">\n            <a *ngFor=\"let data of posts\" (click)=\"navigate(data)\">\n                <h2 class=\"post-title post\">\n                    {{ data['title'] }}\n                </h2>\n                <hr>\n            </a>\n        </ng-container>\n    </div>\n</div>"

/***/ }),

/***/ "./node_modules/raw-loader/index.js!./src/app/components/blog/post/post.component.html":
/*!************************************************************************************!*\
  !*** ./node_modules/raw-loader!./src/app/components/blog/post/post.component.html ***!
  \************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<app-header [header]=\"currentHeader\"></app-header>\n\n<article>\n    <div class=\"container\">\n        <div class=\"row\">\n            <div class=\"col-lg-8 col-md-9 mx-auto\">\n                <ng-container *ngIf=\"body\">\n                    <div class=\"post\">\n                        <markdown [data]=\"body\"></markdown>\n                    </div>\n                </ng-container>\n            </div>\n\n        </div>\n    </div>\n\n</article>"

/***/ }),

/***/ "./node_modules/raw-loader/index.js!./src/app/components/error/error.component.html":
/*!*********************************************************************************!*\
  !*** ./node_modules/raw-loader!./src/app/components/error/error.component.html ***!
  \*********************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<app-header [header]=\"currentHeader\"></app-header>\n"

/***/ }),

/***/ "./node_modules/raw-loader/index.js!./src/app/components/home/home.component.html":
/*!*******************************************************************************!*\
  !*** ./node_modules/raw-loader!./src/app/components/home/home.component.html ***!
  \*******************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<app-header [header]=\"currentHeader\"></app-header>\n\n<div id=\"intro\">\n  <div class=\"container\">\n    <div class=\"row\">\n      <div class=\"col-lg-8 col-md-9 mx-auto \">\n        <p>As an avid reader and podcast listener, I love to embrace the challenge of learning new things that are\n          outside my realm of knowledge. I believe that human life has nearly unlimited potential, and the only key to\n          unlock it is through knowledge and grit. My goal is to use my resources and talents to affect change in this\n          world, and help everyone reach their potential.\n        </p>\n\n        <p>I like to dabble and tinker with multiple technologies with the goal of solving intriguing problems and\n          puzzles. Stay tuned for more projects, and if you have any more questions, feel free to contact me.</p>\n      </div>\n\n      <div class=\"col-lg-4 col-md-3 mx-auto\">\n\n        <div class=\"col-md-12\">\n          <app-profile></app-profile>\n        </div>\n\n      </div>\n    </div>\n  </div>\n</div>"

/***/ }),

/***/ "./node_modules/raw-loader/index.js!./src/app/components/profile/profile.component.html":
/*!*************************************************************************************!*\
  !*** ./node_modules/raw-loader!./src/app/components/profile/profile.component.html ***!
  \*************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div class=\"profile\" itemscope itemtype=\"http://schema.org/Person\">\n    <ng-container *ngIf=\"data\">\n        <div class=\"author__avatar\">\n            <img src=\"{{ data['image'] }}\" class=\"avatar\" itemprop=\"image\">\n        </div>\n\n        <div class=\"author__content\">\n            <h3 class=\"author__name\" itemprop=\"name\">Tony Hammack</h3>\n            <p class=\"author__bio\" itemprop=\"description\">\n                {{ data['bio'] }}\n            </p>\n        </div>\n\n        <div class=\"author__urls-wrapper\">\n            <ul class=\"fa-ul\">\n                <li>\n                    <a href=\"http://{{ data['website'] }}\" itemprop=\"url\">\n                        <i class=\"fas fa-li fa-link\" aria-hidden=\"true\"></i> {{ data['website'] }}\n                    </a>\n                </li>\n                <li>\n                    <a href=\"https://www.linkedin.com/in/{{ data['linkedin'] }}\" itemprop=\"sameAs\">\n                        <i class=\"fab fa-li fa-linkedin\" aria-hidden=\"true\"></i> LinkedIn\n                    </a>\n                </li>\n                <li>\n                    <a href=\"https://github.com/{{ data['github'] }}\" itemprop=\"sameAs\">\n                        <i class=\"fab fa-li fa-github\" aria-hidden=\"true\"></i> GitHub\n                    </a>\n                </li>\n                <li>\n                    <a href=\"https://dev.to/{{ data['devto'] }}\" itemprop=\"sameAs\">\n                        <i class=\"fab fa-li fa-dev\" aria-hidden=\"true\"></i> Dev.to\n                    </a>\n                </li>\n            </ul>\n        </div>\n    </ng-container>\n</div>"

/***/ }),

/***/ "./node_modules/raw-loader/index.js!./src/app/components/shared/footer/footer.component.html":
/*!******************************************************************************************!*\
  !*** ./node_modules/raw-loader!./src/app/components/shared/footer/footer.component.html ***!
  \******************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<footer>\n    <div class=\"container\">\n        <div class=\"row\">\n            <div class=\"col-lg-8 col-md-10 mx-auto\">\n                <p class=\"copyright text-muted\">Copyright &copy; 2019 Tony Hammack</p>\n            </div>\n        </div>\n    </div>\n</footer>"

/***/ }),

/***/ "./node_modules/raw-loader/index.js!./src/app/components/shared/header/header.component.html":
/*!******************************************************************************************!*\
  !*** ./node_modules/raw-loader!./src/app/components/shared/header/header.component.html ***!
  \******************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<header class=\"masthead\" [style.background-image]=\"header.image\">\n    <div class=\"overlay\"></div>\n    <div class=\"container\">\n        <div class=\"row\">\n            <div class=\"col-lg-8 col-md-10 mx-auto\">\n                <div class=\"site-heading\">\n                    <h1>{{ header.title }}</h1>\n                    <span class=\"subheading\">{{ header.subtitle }}</span>\n                </div>\n            </div>\n        </div>\n    </div>\n</header>"

/***/ }),

/***/ "./node_modules/raw-loader/index.js!./src/app/components/shared/navbar/navbar.component.html":
/*!******************************************************************************************!*\
  !*** ./node_modules/raw-loader!./src/app/components/shared/navbar/navbar.component.html ***!
  \******************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<!-- Navigation -->\n<nav class=\"navbar navbar-expand-lg navbar-light fixed-top\" id=\"mainNav\">\n    <div class=\"container\">\n        <ng-container>\n            <a class=\"navbar-brand\" [routerLink]=\"['.']\">Tony Hammack</a>\n            <button class=\"navbar-toggler navbar-toggler-right\" type=\"button\" data-toggle=\"collapse\"\n                data-target=\"#navbarResponsive\" aria-controls=\"navbarResponsive\" aria-expanded=\"false\"\n                aria-label=\"Toggle navigation\">\n                Menu\n                <i class=\"fa fa-bars\"></i>\n            </button>\n            <div class=\"collapse navbar-collapse\" id=\"navbarResponsive\">\n                <ul class=\"navbar-nav ml-auto\">\n                    <li class=\"nav-item\">\n                        <a class=\"nav-link\" [routerLink]=\"['.']\">Home</a>\n                    </li>\n                    <!-- <li class=\"nav-item\">\n              <a class=\"nav-link\" href=\"/contact\">Contact</a>\n            </li> -->\n                    <li class=\"nav-item\">\n                        <a class=\"nav-link\" [routerLink]=\"['/personal']\">Blog</a>\n                    </li>\n                    <li class=\"nav-item\">\n                        <a class=\"nav-link\" [routerLink]=\"['/tech']\">Tech Stuff</a>\n                    </li>\n                </ul>\n            </div>\n        </ng-container>\n    </div>\n</nav>"

/***/ }),

/***/ "./src/app/app-routing.module.ts":
/*!***************************************!*\
  !*** ./src/app/app-routing.module.ts ***!
  \***************************************/
/*! exports provided: AppRoutingModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppRoutingModule", function() { return AppRoutingModule; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _components_home_home_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./components/home/home.component */ "./src/app/components/home/home.component.ts");
/* harmony import */ var _components_blog_main_main_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./components/blog/main/main.component */ "./src/app/components/blog/main/main.component.ts");
/* harmony import */ var _components_blog_post_post_component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./components/blog/post/post.component */ "./src/app/components/blog/post/post.component.ts");
/* harmony import */ var _components_blog_category_category_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./components/blog/category/category.component */ "./src/app/components/blog/category/category.component.ts");
/* harmony import */ var _components_error_error_component__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./components/error/error.component */ "./src/app/components/error/error.component.ts");








var routes = [
    { path: 'personal', component: _components_blog_main_main_component__WEBPACK_IMPORTED_MODULE_4__["BlogComponent"] },
    { path: 'personal/:slug', component: _components_blog_post_post_component__WEBPACK_IMPORTED_MODULE_5__["PostComponent"] },
    { path: 'personal/category/:category', component: _components_blog_category_category_component__WEBPACK_IMPORTED_MODULE_6__["CategoryComponent"] },
    { path: 'tech', component: _components_blog_main_main_component__WEBPACK_IMPORTED_MODULE_4__["BlogComponent"] },
    { path: 'tech/:slug', component: _components_blog_post_post_component__WEBPACK_IMPORTED_MODULE_5__["PostComponent"] },
    { path: 'tech/category/:category', component: _components_blog_category_category_component__WEBPACK_IMPORTED_MODULE_6__["CategoryComponent"] },
    { path: '', component: _components_home_home_component__WEBPACK_IMPORTED_MODULE_3__["HomeComponent"] },
    // Errors
    { path: 'error', component: _components_error_error_component__WEBPACK_IMPORTED_MODULE_7__["ErrorComponent"] },
    { path: '**', redirectTo: '/error' }
];
var AppRoutingModule = /** @class */ (function () {
    function AppRoutingModule() {
    }
    AppRoutingModule = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["NgModule"])({
            imports: [_angular_router__WEBPACK_IMPORTED_MODULE_2__["RouterModule"].forRoot(routes, { useHash: true })],
            exports: [_angular_router__WEBPACK_IMPORTED_MODULE_2__["RouterModule"]]
        })
    ], AppRoutingModule);
    return AppRoutingModule;
}());



/***/ }),

/***/ "./src/app/app.component.scss":
/*!************************************!*\
  !*** ./src/app/app.component.scss ***!
  \************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2FwcC5jb21wb25lbnQuc2NzcyJ9 */"

/***/ }),

/***/ "./src/app/app.component.ts":
/*!**********************************!*\
  !*** ./src/app/app.component.ts ***!
  \**********************************/
/*! exports provided: AppComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppComponent", function() { return AppComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");


var AppComponent = /** @class */ (function () {
    function AppComponent() {
        this.title = 'app';
    }
    AppComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-root',
            template: __webpack_require__(/*! raw-loader!./app.component.html */ "./node_modules/raw-loader/index.js!./src/app/app.component.html"),
            styles: [__webpack_require__(/*! ./app.component.scss */ "./src/app/app.component.scss")]
        })
    ], AppComponent);
    return AppComponent;
}());



/***/ }),

/***/ "./src/app/app.module.ts":
/*!*******************************!*\
  !*** ./src/app/app.module.ts ***!
  \*******************************/
/*! exports provided: AppModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppModule", function() { return AppModule; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/platform-browser */ "./node_modules/@angular/platform-browser/fesm5/platform-browser.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_http__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @angular/http */ "./node_modules/@angular/http/fesm5/http.js");
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @angular/common/http */ "./node_modules/@angular/common/fesm5/http.js");
/* harmony import */ var ngx_markdown__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ngx-markdown */ "./node_modules/ngx-markdown/fesm5/ngx-markdown.js");
/* harmony import */ var _app_routing_module__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./app-routing.module */ "./src/app/app-routing.module.ts");
/* harmony import */ var _app_component__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./app.component */ "./src/app/app.component.ts");
/* harmony import */ var _components_home_home_component__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./components/home/home.component */ "./src/app/components/home/home.component.ts");
/* harmony import */ var _components_blog_main_main_component__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./components/blog/main/main.component */ "./src/app/components/blog/main/main.component.ts");
/* harmony import */ var _components_blog_post_post_component__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ./components/blog/post/post.component */ "./src/app/components/blog/post/post.component.ts");
/* harmony import */ var _components_error_error_component__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! ./components/error/error.component */ "./src/app/components/error/error.component.ts");
/* harmony import */ var _components_shared_navbar_navbar_component__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! ./components/shared/navbar/navbar.component */ "./src/app/components/shared/navbar/navbar.component.ts");
/* harmony import */ var _components_shared_footer_footer_component__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! ./components/shared/footer/footer.component */ "./src/app/components/shared/footer/footer.component.ts");
/* harmony import */ var _components_shared_header_header_component__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! ./components/shared/header/header.component */ "./src/app/components/shared/header/header.component.ts");
/* harmony import */ var _components_profile_profile_component__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! ./components/profile/profile.component */ "./src/app/components/profile/profile.component.ts");
/* harmony import */ var _components_blog_category_category_component__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__(/*! ./components/blog/category/category.component */ "./src/app/components/blog/category/category.component.ts");
/* harmony import */ var src_app_services_config_service__WEBPACK_IMPORTED_MODULE_17__ = __webpack_require__(/*! src/app/services/config.service */ "./src/app/services/config.service.ts");
/* harmony import */ var src_app_services_user_user_service__WEBPACK_IMPORTED_MODULE_18__ = __webpack_require__(/*! src/app/services/user/user.service */ "./src/app/services/user/user.service.ts");
/* harmony import */ var src_app_services_blog_blog_service__WEBPACK_IMPORTED_MODULE_19__ = __webpack_require__(/*! src/app/services/blog/blog.service */ "./src/app/services/blog/blog.service.ts");




















var AppModule = /** @class */ (function () {
    function AppModule() {
    }
    AppModule = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_2__["NgModule"])({
            declarations: [
                _app_component__WEBPACK_IMPORTED_MODULE_7__["AppComponent"],
                _components_home_home_component__WEBPACK_IMPORTED_MODULE_8__["HomeComponent"],
                _components_blog_main_main_component__WEBPACK_IMPORTED_MODULE_9__["BlogComponent"],
                _components_blog_post_post_component__WEBPACK_IMPORTED_MODULE_10__["PostComponent"],
                _components_error_error_component__WEBPACK_IMPORTED_MODULE_11__["ErrorComponent"],
                _components_shared_navbar_navbar_component__WEBPACK_IMPORTED_MODULE_12__["NavbarComponent"],
                _components_shared_footer_footer_component__WEBPACK_IMPORTED_MODULE_13__["FooterComponent"],
                _components_shared_header_header_component__WEBPACK_IMPORTED_MODULE_14__["HeaderComponent"],
                _components_profile_profile_component__WEBPACK_IMPORTED_MODULE_15__["ProfileComponent"],
                _components_blog_category_category_component__WEBPACK_IMPORTED_MODULE_16__["CategoryComponent"]
            ],
            imports: [
                _angular_platform_browser__WEBPACK_IMPORTED_MODULE_1__["BrowserModule"],
                _app_routing_module__WEBPACK_IMPORTED_MODULE_6__["AppRoutingModule"],
                _angular_http__WEBPACK_IMPORTED_MODULE_3__["HttpModule"],
                _angular_common_http__WEBPACK_IMPORTED_MODULE_4__["HttpClientModule"],
                ngx_markdown__WEBPACK_IMPORTED_MODULE_5__["MarkdownModule"].forRoot()
            ],
            providers: [src_app_services_config_service__WEBPACK_IMPORTED_MODULE_17__["ConfigService"], src_app_services_blog_blog_service__WEBPACK_IMPORTED_MODULE_19__["BlogService"], src_app_services_user_user_service__WEBPACK_IMPORTED_MODULE_18__["UserService"]],
            bootstrap: [_app_component__WEBPACK_IMPORTED_MODULE_7__["AppComponent"]],
            schemas: [_angular_core__WEBPACK_IMPORTED_MODULE_2__["CUSTOM_ELEMENTS_SCHEMA"]]
        })
    ], AppModule);
    return AppModule;
}());



/***/ }),

/***/ "./src/app/components/blog/category/category.component.scss":
/*!******************************************************************!*\
  !*** ./src/app/components/blog/category/category.component.scss ***!
  \******************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2NvbXBvbmVudHMvYmxvZy9jYXRlZ29yeS9jYXRlZ29yeS5jb21wb25lbnQuc2NzcyJ9 */"

/***/ }),

/***/ "./src/app/components/blog/category/category.component.ts":
/*!****************************************************************!*\
  !*** ./src/app/components/blog/category/category.component.ts ***!
  \****************************************************************/
/*! exports provided: CategoryComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "CategoryComponent", function() { return CategoryComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var src_app_models_header_model__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! src/app/models/header.model */ "./src/app/models/header.model.ts");
/* harmony import */ var src_app_services_config_service__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! src/app/services/config.service */ "./src/app/services/config.service.ts");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var src_app_services_blog_blog_service__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! src/app/services/blog/blog.service */ "./src/app/services/blog/blog.service.ts");






var CategoryComponent = /** @class */ (function () {
    function CategoryComponent(router, route, _blog) {
        this.router = router;
        this.route = route;
        this._blog = _blog;
        this.currentHeader = new src_app_models_header_model__WEBPACK_IMPORTED_MODULE_2__["Header"]();
        this.subscriptions = [];
        this.posts = [];
        this.blogs = { 'personal': { 'name': 'Personal', 'image': 'blog/img/categories.jpg' }, 'tech': { 'name': 'Tech', 'image': 'blog/img/library-2.jpg' } };
    }
    CategoryComponent.prototype.ngOnInit = function () {
        var _this = this;
        this.blog = this.route.snapshot.url[0].path;
        this.subscriptions.push(this.route.params.subscribe(function (params) { return _this.category = params.category; }));
        this.onLoad();
    };
    CategoryComponent.prototype.onLoad = function () {
        var _this = this;
        this.setHeader();
        this.subscriptions.push(this._blog.all(this.blog, { "category": this.category }).subscribe(function (data) { return _this.posts = data; }));
    };
    CategoryComponent.prototype.ngOnDestroy = function () {
        this.subscriptions.forEach(function (x) { return x.unsubscribe(); });
    };
    CategoryComponent.prototype.navigate = function (data) {
        this.router.navigate([this.blog, data.slug]);
    };
    CategoryComponent.prototype.setHeader = function () {
        this.currentHeader.title = this.category;
        this.currentHeader.image = "url(" + src_app_services_config_service__WEBPACK_IMPORTED_MODULE_3__["ConfigService"].S3_LOCATION + "/" + this.blogs[this.blog]["image"] + ")";
    };
    CategoryComponent.ctorParameters = function () { return [
        { type: _angular_router__WEBPACK_IMPORTED_MODULE_4__["Router"] },
        { type: _angular_router__WEBPACK_IMPORTED_MODULE_4__["ActivatedRoute"] },
        { type: src_app_services_blog_blog_service__WEBPACK_IMPORTED_MODULE_5__["BlogService"] }
    ]; };
    CategoryComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-category',
            template: __webpack_require__(/*! raw-loader!./category.component.html */ "./node_modules/raw-loader/index.js!./src/app/components/blog/category/category.component.html"),
            styles: [__webpack_require__(/*! ./category.component.scss */ "./src/app/components/blog/category/category.component.scss")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [_angular_router__WEBPACK_IMPORTED_MODULE_4__["Router"], _angular_router__WEBPACK_IMPORTED_MODULE_4__["ActivatedRoute"], src_app_services_blog_blog_service__WEBPACK_IMPORTED_MODULE_5__["BlogService"]])
    ], CategoryComponent);
    return CategoryComponent;
}());



/***/ }),

/***/ "./src/app/components/blog/main/main.component.scss":
/*!**********************************************************!*\
  !*** ./src/app/components/blog/main/main.component.scss ***!
  \**********************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2NvbXBvbmVudHMvYmxvZy9tYWluL21haW4uY29tcG9uZW50LnNjc3MifQ== */"

/***/ }),

/***/ "./src/app/components/blog/main/main.component.ts":
/*!********************************************************!*\
  !*** ./src/app/components/blog/main/main.component.ts ***!
  \********************************************************/
/*! exports provided: BlogComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "BlogComponent", function() { return BlogComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var src_app_services_blog_blog_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! src/app/services/blog/blog.service */ "./src/app/services/blog/blog.service.ts");
/* harmony import */ var src_app_models_header_model__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! src/app/models/header.model */ "./src/app/models/header.model.ts");
/* harmony import */ var src_app_services_config_service__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! src/app/services/config.service */ "./src/app/services/config.service.ts");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");






var BlogComponent = /** @class */ (function () {
    function BlogComponent(router, route, _blog) {
        this.router = router;
        this.route = route;
        this._blog = _blog;
        this.currentHeader = new src_app_models_header_model__WEBPACK_IMPORTED_MODULE_3__["Header"]();
        this.subscriptions = [];
        this.blog = "";
        this.posts = [];
        this.blogs = { 'personal': { 'name': 'Personal', 'image': 'blog/img/blog-header.jpg' }, 'tech': { 'name': 'Tech', 'image': 'blog/img/laptop-blog.jpg' } };
    }
    BlogComponent.prototype.ngOnInit = function () {
        this.blog = this.route.snapshot.url[0].path;
        this.onLoad();
    };
    BlogComponent.prototype.setHeader = function () {
        this.currentHeader.title = this.blogs[this.blog]["name"] + " Thoughts";
        this.currentHeader.image = "url(" + src_app_services_config_service__WEBPACK_IMPORTED_MODULE_4__["ConfigService"].S3_LOCATION + "/" + this.blogs[this.blog]["image"] + ")";
    };
    BlogComponent.prototype.onLoad = function () {
        var _this = this;
        this.setHeader();
        this.subscriptions.push(this._blog.all(this.blog).subscribe(function (data) { return _this.posts = data; }));
    };
    BlogComponent.prototype.navigate = function (data) {
        this.router.navigate([this.blog, data.slug]);
    };
    BlogComponent.prototype.ngOnDestroy = function () {
        this.subscriptions.forEach(function (x) { return x.unsubscribe(); });
    };
    BlogComponent.ctorParameters = function () { return [
        { type: _angular_router__WEBPACK_IMPORTED_MODULE_5__["Router"] },
        { type: _angular_router__WEBPACK_IMPORTED_MODULE_5__["ActivatedRoute"] },
        { type: src_app_services_blog_blog_service__WEBPACK_IMPORTED_MODULE_2__["BlogService"] }
    ]; };
    BlogComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-blog',
            template: __webpack_require__(/*! raw-loader!./main.component.html */ "./node_modules/raw-loader/index.js!./src/app/components/blog/main/main.component.html"),
            styles: [__webpack_require__(/*! ./main.component.scss */ "./src/app/components/blog/main/main.component.scss")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [_angular_router__WEBPACK_IMPORTED_MODULE_5__["Router"], _angular_router__WEBPACK_IMPORTED_MODULE_5__["ActivatedRoute"], src_app_services_blog_blog_service__WEBPACK_IMPORTED_MODULE_2__["BlogService"]])
    ], BlogComponent);
    return BlogComponent;
}());



/***/ }),

/***/ "./src/app/components/blog/post/post.component.scss":
/*!**********************************************************!*\
  !*** ./src/app/components/blog/post/post.component.scss ***!
  \**********************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2NvbXBvbmVudHMvYmxvZy9wb3N0L3Bvc3QuY29tcG9uZW50LnNjc3MifQ== */"

/***/ }),

/***/ "./src/app/components/blog/post/post.component.ts":
/*!********************************************************!*\
  !*** ./src/app/components/blog/post/post.component.ts ***!
  \********************************************************/
/*! exports provided: PostComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "PostComponent", function() { return PostComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var src_app_services_blog_blog_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! src/app/services/blog/blog.service */ "./src/app/services/blog/blog.service.ts");
/* harmony import */ var src_app_models_header_model__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! src/app/models/header.model */ "./src/app/models/header.model.ts");
/* harmony import */ var src_app_services_config_service__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! src/app/services/config.service */ "./src/app/services/config.service.ts");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");






var PostComponent = /** @class */ (function () {
    function PostComponent(route, _blog) {
        this.route = route;
        this._blog = _blog;
        this.currentHeader = new src_app_models_header_model__WEBPACK_IMPORTED_MODULE_3__["Header"]();
        this.subscriptions = [];
        this.body = "";
    }
    PostComponent.prototype.ngOnInit = function () {
        var _this = this;
        this.blog = this.route.snapshot.url[0].path;
        this.subscriptions.push(this.route.params.subscribe(function (params) { return _this.slug = params.slug; }));
        this.onLoad();
    };
    PostComponent.prototype.setHeader = function () {
        this.currentHeader.title = this.post["title"];
        this.currentHeader.image = "url(" + src_app_services_config_service__WEBPACK_IMPORTED_MODULE_4__["ConfigService"].S3_LOCATION + "/" + this.post["image"] + ")";
    };
    PostComponent.prototype.onLoad = function () {
        var _this = this;
        this.subscriptions.push(this._blog.get(this.blog, this.slug).subscribe(function (data) { _this.post = data[0]; _this.body = _this.post["body"]; _this.setHeader(); }));
    };
    PostComponent.prototype.ngOnDestroy = function () {
        this.subscriptions.forEach(function (x) { return x.unsubscribe(); });
    };
    PostComponent.ctorParameters = function () { return [
        { type: _angular_router__WEBPACK_IMPORTED_MODULE_5__["ActivatedRoute"] },
        { type: src_app_services_blog_blog_service__WEBPACK_IMPORTED_MODULE_2__["BlogService"] }
    ]; };
    PostComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-post',
            template: __webpack_require__(/*! raw-loader!./post.component.html */ "./node_modules/raw-loader/index.js!./src/app/components/blog/post/post.component.html"),
            styles: [__webpack_require__(/*! ./post.component.scss */ "./src/app/components/blog/post/post.component.scss")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [_angular_router__WEBPACK_IMPORTED_MODULE_5__["ActivatedRoute"], src_app_services_blog_blog_service__WEBPACK_IMPORTED_MODULE_2__["BlogService"]])
    ], PostComponent);
    return PostComponent;
}());



/***/ }),

/***/ "./src/app/components/error/error.component.scss":
/*!*******************************************************!*\
  !*** ./src/app/components/error/error.component.scss ***!
  \*******************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2NvbXBvbmVudHMvZXJyb3IvZXJyb3IuY29tcG9uZW50LnNjc3MifQ== */"

/***/ }),

/***/ "./src/app/components/error/error.component.ts":
/*!*****************************************************!*\
  !*** ./src/app/components/error/error.component.ts ***!
  \*****************************************************/
/*! exports provided: ErrorComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "ErrorComponent", function() { return ErrorComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var src_app_services_config_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! src/app/services/config.service */ "./src/app/services/config.service.ts");
/* harmony import */ var src_app_models_header_model__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! src/app/models/header.model */ "./src/app/models/header.model.ts");




var ErrorComponent = /** @class */ (function () {
    function ErrorComponent() {
        this.currentHeader = new src_app_models_header_model__WEBPACK_IMPORTED_MODULE_3__["Header"]();
    }
    ErrorComponent.prototype.ngOnInit = function () {
        this.setHeader();
    };
    ErrorComponent.prototype.setHeader = function () {
        this.currentHeader.title = "Error";
        this.currentHeader.subtitle = "Sorry for the inconvience!";
        this.currentHeader.image = "url(" + src_app_services_config_service__WEBPACK_IMPORTED_MODULE_2__["ConfigService"].S3_LOCATION + "/blog/img/glitch.png)";
    };
    ErrorComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-error',
            template: __webpack_require__(/*! raw-loader!./error.component.html */ "./node_modules/raw-loader/index.js!./src/app/components/error/error.component.html"),
            styles: [__webpack_require__(/*! ./error.component.scss */ "./src/app/components/error/error.component.scss")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [])
    ], ErrorComponent);
    return ErrorComponent;
}());



/***/ }),

/***/ "./src/app/components/home/home.component.scss":
/*!*****************************************************!*\
  !*** ./src/app/components/home/home.component.scss ***!
  \*****************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2NvbXBvbmVudHMvaG9tZS9ob21lLmNvbXBvbmVudC5zY3NzIn0= */"

/***/ }),

/***/ "./src/app/components/home/home.component.ts":
/*!***************************************************!*\
  !*** ./src/app/components/home/home.component.ts ***!
  \***************************************************/
/*! exports provided: HomeComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "HomeComponent", function() { return HomeComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var src_app_services_config_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! src/app/services/config.service */ "./src/app/services/config.service.ts");
/* harmony import */ var src_app_models_header_model__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! src/app/models/header.model */ "./src/app/models/header.model.ts");




var HomeComponent = /** @class */ (function () {
    function HomeComponent() {
        this.currentHeader = new src_app_models_header_model__WEBPACK_IMPORTED_MODULE_3__["Header"]();
    }
    HomeComponent.prototype.ngOnInit = function () {
        this.setHeader();
    };
    HomeComponent.prototype.setHeader = function () {
        this.currentHeader.title = "Tony Hammack";
        this.currentHeader.subtitle = "Curious Tinkerer | hammack.tony@gmail.com";
        this.currentHeader.image = "url(" + src_app_services_config_service__WEBPACK_IMPORTED_MODULE_2__["ConfigService"].S3_LOCATION + "/user/img/marketing-wallpaper-27.jpg)";
    };
    HomeComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-home',
            template: __webpack_require__(/*! raw-loader!./home.component.html */ "./node_modules/raw-loader/index.js!./src/app/components/home/home.component.html"),
            styles: [__webpack_require__(/*! ./home.component.scss */ "./src/app/components/home/home.component.scss")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [])
    ], HomeComponent);
    return HomeComponent;
}());



/***/ }),

/***/ "./src/app/components/profile/profile.component.scss":
/*!***********************************************************!*\
  !*** ./src/app/components/profile/profile.component.scss ***!
  \***********************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".avatar {\n  vertical-align: middle;\n  max-width: 110px;\n  border-radius: 50%;\n}\n\n.profile {\n  border-left: 1px solid #f2f2f2;\n  padding-left: 20px;\n  padding-bottom: 10px;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3RvbnkvQ29kZS9wcml2YXRlL3RvbnloYW1tYWNrLmNvbS9yZXNvdXJjZXMvdGVtcGxhdGVzL2FwcC9zcmMvYXBwL2NvbXBvbmVudHMvcHJvZmlsZS9wcm9maWxlLmNvbXBvbmVudC5zY3NzIiwic3JjL2FwcC9jb21wb25lbnRzL3Byb2ZpbGUvcHJvZmlsZS5jb21wb25lbnQuc2NzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQTtFQUNJLHNCQUFBO0VBQ0EsZ0JBQUE7RUFDQSxrQkFBQTtBQ0NKOztBRENBO0VBQ0ksOEJBQUE7RUFDQSxrQkFBQTtFQUNBLG9CQUFBO0FDRUoiLCJmaWxlIjoic3JjL2FwcC9jb21wb25lbnRzL3Byb2ZpbGUvcHJvZmlsZS5jb21wb25lbnQuc2NzcyIsInNvdXJjZXNDb250ZW50IjpbIi5hdmF0YXIge1xuICAgIHZlcnRpY2FsLWFsaWduOiBtaWRkbGU7XG4gICAgbWF4LXdpZHRoOiAxMTBweDtcbiAgICBib3JkZXItcmFkaXVzOiA1MCU7XG59XG4ucHJvZmlsZSB7XG4gICAgYm9yZGVyLWxlZnQ6IDFweCBzb2xpZCAjZjJmMmYyO1xuICAgIHBhZGRpbmctbGVmdDogMjBweDtcbiAgICBwYWRkaW5nLWJvdHRvbTogMTBweDtcbn1cblxuIiwiLmF2YXRhciB7XG4gIHZlcnRpY2FsLWFsaWduOiBtaWRkbGU7XG4gIG1heC13aWR0aDogMTEwcHg7XG4gIGJvcmRlci1yYWRpdXM6IDUwJTtcbn1cblxuLnByb2ZpbGUge1xuICBib3JkZXItbGVmdDogMXB4IHNvbGlkICNmMmYyZjI7XG4gIHBhZGRpbmctbGVmdDogMjBweDtcbiAgcGFkZGluZy1ib3R0b206IDEwcHg7XG59Il19 */"

/***/ }),

/***/ "./src/app/components/profile/profile.component.ts":
/*!*********************************************************!*\
  !*** ./src/app/components/profile/profile.component.ts ***!
  \*********************************************************/
/*! exports provided: ProfileComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "ProfileComponent", function() { return ProfileComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var src_app_services_config_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! src/app/services/config.service */ "./src/app/services/config.service.ts");
/* harmony import */ var src_app_services_user_user_service__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! src/app/services/user/user.service */ "./src/app/services/user/user.service.ts");




var ProfileComponent = /** @class */ (function () {
    function ProfileComponent(_user) {
        this._user = _user;
        this.user = 'tonus';
        this.subscriptions = [];
    }
    ProfileComponent.prototype.ngOnInit = function () {
        this.loadUser();
    };
    ProfileComponent.prototype.loadUser = function () {
        var _this = this;
        this.subscriptions.push(this._user.get(this.user).subscribe(function (data) {
            _this.data = data[0];
            _this.data["image"] = src_app_services_config_service__WEBPACK_IMPORTED_MODULE_2__["ConfigService"].S3_LOCATION + "/" + _this.data["image"];
        }));
    };
    ProfileComponent.prototype.ngOnDestroy = function () {
        this.subscriptions.forEach(function (x) { return x.unsubscribe(); });
    };
    ProfileComponent.ctorParameters = function () { return [
        { type: src_app_services_user_user_service__WEBPACK_IMPORTED_MODULE_3__["UserService"] }
    ]; };
    ProfileComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-profile',
            template: __webpack_require__(/*! raw-loader!./profile.component.html */ "./node_modules/raw-loader/index.js!./src/app/components/profile/profile.component.html"),
            styles: [__webpack_require__(/*! ./profile.component.scss */ "./src/app/components/profile/profile.component.scss")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [src_app_services_user_user_service__WEBPACK_IMPORTED_MODULE_3__["UserService"]])
    ], ProfileComponent);
    return ProfileComponent;
}());



/***/ }),

/***/ "./src/app/components/shared/footer/footer.component.scss":
/*!****************************************************************!*\
  !*** ./src/app/components/shared/footer/footer.component.scss ***!
  \****************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2NvbXBvbmVudHMvc2hhcmVkL2Zvb3Rlci9mb290ZXIuY29tcG9uZW50LnNjc3MifQ== */"

/***/ }),

/***/ "./src/app/components/shared/footer/footer.component.ts":
/*!**************************************************************!*\
  !*** ./src/app/components/shared/footer/footer.component.ts ***!
  \**************************************************************/
/*! exports provided: FooterComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "FooterComponent", function() { return FooterComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");


var FooterComponent = /** @class */ (function () {
    function FooterComponent() {
    }
    FooterComponent.prototype.ngOnInit = function () {
    };
    FooterComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-footer',
            template: __webpack_require__(/*! raw-loader!./footer.component.html */ "./node_modules/raw-loader/index.js!./src/app/components/shared/footer/footer.component.html"),
            styles: [__webpack_require__(/*! ./footer.component.scss */ "./src/app/components/shared/footer/footer.component.scss")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [])
    ], FooterComponent);
    return FooterComponent;
}());



/***/ }),

/***/ "./src/app/components/shared/header/header.component.scss":
/*!****************************************************************!*\
  !*** ./src/app/components/shared/header/header.component.scss ***!
  \****************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2NvbXBvbmVudHMvc2hhcmVkL2hlYWRlci9oZWFkZXIuY29tcG9uZW50LnNjc3MifQ== */"

/***/ }),

/***/ "./src/app/components/shared/header/header.component.ts":
/*!**************************************************************!*\
  !*** ./src/app/components/shared/header/header.component.ts ***!
  \**************************************************************/
/*! exports provided: HeaderComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "HeaderComponent", function() { return HeaderComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var src_app_models_header_model__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! src/app/models/header.model */ "./src/app/models/header.model.ts");



var HeaderComponent = /** @class */ (function () {
    function HeaderComponent() {
    }
    HeaderComponent.prototype.ngOnInit = function () {
    };
    tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Input"])(),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:type", src_app_models_header_model__WEBPACK_IMPORTED_MODULE_2__["Header"])
    ], HeaderComponent.prototype, "header", void 0);
    HeaderComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-header',
            template: __webpack_require__(/*! raw-loader!./header.component.html */ "./node_modules/raw-loader/index.js!./src/app/components/shared/header/header.component.html"),
            styles: [__webpack_require__(/*! ./header.component.scss */ "./src/app/components/shared/header/header.component.scss")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [])
    ], HeaderComponent);
    return HeaderComponent;
}());



/***/ }),

/***/ "./src/app/components/shared/navbar/navbar.component.scss":
/*!****************************************************************!*\
  !*** ./src/app/components/shared/navbar/navbar.component.scss ***!
  \****************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2NvbXBvbmVudHMvc2hhcmVkL25hdmJhci9uYXZiYXIuY29tcG9uZW50LnNjc3MifQ== */"

/***/ }),

/***/ "./src/app/components/shared/navbar/navbar.component.ts":
/*!**************************************************************!*\
  !*** ./src/app/components/shared/navbar/navbar.component.ts ***!
  \**************************************************************/
/*! exports provided: NavbarComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "NavbarComponent", function() { return NavbarComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");


var NavbarComponent = /** @class */ (function () {
    function NavbarComponent() {
    }
    NavbarComponent.prototype.ngOnInit = function () {
    };
    NavbarComponent = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"])({
            selector: 'app-navbar',
            template: __webpack_require__(/*! raw-loader!./navbar.component.html */ "./node_modules/raw-loader/index.js!./src/app/components/shared/navbar/navbar.component.html"),
            styles: [__webpack_require__(/*! ./navbar.component.scss */ "./src/app/components/shared/navbar/navbar.component.scss")]
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [])
    ], NavbarComponent);
    return NavbarComponent;
}());



/***/ }),

/***/ "./src/app/models/header.model.ts":
/*!****************************************!*\
  !*** ./src/app/models/header.model.ts ***!
  \****************************************/
/*! exports provided: Header */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "Header", function() { return Header; });
var Header = /** @class */ (function () {
    function Header() {
    }
    return Header;
}());



/***/ }),

/***/ "./src/app/services/blog/blog.service.ts":
/*!***********************************************!*\
  !*** ./src/app/services/blog/blog.service.ts ***!
  \***********************************************/
/*! exports provided: BlogService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "BlogService", function() { return BlogService; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var rxjs__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! rxjs */ "./node_modules/rxjs/_esm5/index.js");
/* harmony import */ var src_app_services_config_service__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! src/app/services/config.service */ "./src/app/services/config.service.ts");
/* harmony import */ var _angular_http__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @angular/http */ "./node_modules/@angular/http/fesm5/http.js");


// import { HttpService } from 'src/app/services/http.service'



var BlogService = /** @class */ (function () {
    function BlogService(http) {
        this.http = http;
        this._collection$ = new rxjs__WEBPACK_IMPORTED_MODULE_2__["Subject"]();
    }
    Object.defineProperty(BlogService.prototype, "collection$", {
        get: function () { return this._collection$.asObservable(); },
        enumerable: true,
        configurable: true
    });
    BlogService.prototype.all = function (blog, query) {
        var _this = this;
        var e_1, _a;
        if (query === void 0) { query = null; }
        if (query) {
            var url = src_app_services_config_service__WEBPACK_IMPORTED_MODULE_3__["ConfigService"].API_URL + "/api/" + blog + "?";
            try {
                for (var _b = tslib__WEBPACK_IMPORTED_MODULE_0__["__values"](Object.entries(query)), _c = _b.next(); !_c.done; _c = _b.next()) {
                    var _d = tslib__WEBPACK_IMPORTED_MODULE_0__["__read"](_c.value, 2), key = _d[0], value = _d[1];
                    url = url + (key + "=" + value);
                }
            }
            catch (e_1_1) { e_1 = { error: e_1_1 }; }
            finally {
                try {
                    if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
                }
                finally { if (e_1) throw e_1.error; }
            }
            ;
            this.http
                .get(url)
                .subscribe(function (response) {
                _this._collection$.next(JSON.parse(response._body));
            });
        }
        else {
            this.http
                .get(src_app_services_config_service__WEBPACK_IMPORTED_MODULE_3__["ConfigService"].API_URL + "/api/" + blog)
                .subscribe(function (response) {
                _this._collection$.next(JSON.parse(response._body));
            });
        }
        return this._collection$.asObservable();
    };
    BlogService.prototype.get = function (blog, slug) {
        var _this = this;
        this.http
            .get(src_app_services_config_service__WEBPACK_IMPORTED_MODULE_3__["ConfigService"].API_URL + "/api/" + blog + "/" + slug)
            .subscribe(function (response) {
            _this._collection$.next(JSON.parse(response._body));
        });
        return this._collection$.asObservable();
    };
    BlogService.prototype.create = function (blog, payload) {
        var _this = this;
        this.http
            .post(src_app_services_config_service__WEBPACK_IMPORTED_MODULE_3__["ConfigService"].API_URL + "/api/" + blog, payload)
            .subscribe(function (response) {
            _this._collection$.next(JSON.parse(response._body));
        });
        return this._collection$.asObservable();
    };
    BlogService.prototype.update = function (blog, slug, payload) {
        var _this = this;
        this.http
            .put(src_app_services_config_service__WEBPACK_IMPORTED_MODULE_3__["ConfigService"].API_URL + "/api/" + blog + "/" + slug, payload)
            .subscribe(function (response) {
            _this._collection$.next(JSON.parse(response._body));
        });
        return this._collection$.asObservable();
    };
    BlogService.prototype.delete = function (blog, slug) {
        var _this = this;
        this.http
            .delete(src_app_services_config_service__WEBPACK_IMPORTED_MODULE_3__["ConfigService"].API_URL + "/api/" + blog + "/" + slug)
            .subscribe(function (response) {
            _this._collection$.next(JSON.parse(response._body));
        });
        return this._collection$.asObservable();
    };
    BlogService.ctorParameters = function () { return [
        { type: _angular_http__WEBPACK_IMPORTED_MODULE_4__["Http"] }
    ]; };
    BlogService = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Injectable"])({
            providedIn: 'root'
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [_angular_http__WEBPACK_IMPORTED_MODULE_4__["Http"]])
    ], BlogService);
    return BlogService;
}());



/***/ }),

/***/ "./src/app/services/config.service.ts":
/*!********************************************!*\
  !*** ./src/app/services/config.service.ts ***!
  \********************************************/
/*! exports provided: ConfigService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "ConfigService", function() { return ConfigService; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");


var ConfigService = /** @class */ (function () {
    function ConfigService() {
    }
    Object.defineProperty(ConfigService, "S3_LOCATION", {
        get: function () { return "//tony-hammack.s3-website.us-east-2.amazonaws.com"; },
        enumerable: true,
        configurable: true
    });
    Object.defineProperty(ConfigService, "API_URL", {
        get: function () { return document.location.protocol + "//" + document.location.hostname + ":80"; },
        enumerable: true,
        configurable: true
    });
    ConfigService = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Injectable"])({
            providedIn: 'root'
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [])
    ], ConfigService);
    return ConfigService;
}());



/***/ }),

/***/ "./src/app/services/user/user.service.ts":
/*!***********************************************!*\
  !*** ./src/app/services/user/user.service.ts ***!
  \***********************************************/
/*! exports provided: UserService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "UserService", function() { return UserService; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var rxjs__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! rxjs */ "./node_modules/rxjs/_esm5/index.js");
/* harmony import */ var src_app_services_config_service__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! src/app/services/config.service */ "./src/app/services/config.service.ts");
/* harmony import */ var _angular_http__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @angular/http */ "./node_modules/@angular/http/fesm5/http.js");


// import { HttpService } from 'src/app/services/http.service'



var UserService = /** @class */ (function () {
    function UserService(http) {
        this.http = http;
        this._collection$ = new rxjs__WEBPACK_IMPORTED_MODULE_2__["Subject"]();
    }
    Object.defineProperty(UserService.prototype, "collection$", {
        get: function () { return this._collection$.asObservable(); },
        enumerable: true,
        configurable: true
    });
    UserService.prototype.get = function (user) {
        var _this = this;
        this.http
            .get(src_app_services_config_service__WEBPACK_IMPORTED_MODULE_3__["ConfigService"].API_URL + "/api/user/" + user)
            .subscribe(function (response) {
            _this._collection$.next(JSON.parse(response._body));
        });
        return this._collection$.asObservable();
    };
    UserService.ctorParameters = function () { return [
        { type: _angular_http__WEBPACK_IMPORTED_MODULE_4__["Http"] }
    ]; };
    UserService = tslib__WEBPACK_IMPORTED_MODULE_0__["__decorate"]([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["Injectable"])({
            providedIn: 'root'
        }),
        tslib__WEBPACK_IMPORTED_MODULE_0__["__metadata"]("design:paramtypes", [_angular_http__WEBPACK_IMPORTED_MODULE_4__["Http"]])
    ], UserService);
    return UserService;
}());



/***/ }),

/***/ "./src/environments/environment.ts":
/*!*****************************************!*\
  !*** ./src/environments/environment.ts ***!
  \*****************************************/
/*! exports provided: environment */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "environment", function() { return environment; });
// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.
var environment = {
    production: false,
};
/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.


/***/ }),

/***/ "./src/main.ts":
/*!*********************!*\
  !*** ./src/main.ts ***!
  \*********************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_platform_browser_dynamic__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/platform-browser-dynamic */ "./node_modules/@angular/platform-browser-dynamic/fesm5/platform-browser-dynamic.js");
/* harmony import */ var _app_app_module__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./app/app.module */ "./src/app/app.module.ts");
/* harmony import */ var _environments_environment__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./environments/environment */ "./src/environments/environment.ts");




if (_environments_environment__WEBPACK_IMPORTED_MODULE_3__["environment"].production) {
    Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["enableProdMode"])();
}
Object(_angular_platform_browser_dynamic__WEBPACK_IMPORTED_MODULE_1__["platformBrowserDynamic"])().bootstrapModule(_app_app_module__WEBPACK_IMPORTED_MODULE_2__["AppModule"])
    .catch(function (err) { return console.error(err); });


/***/ }),

/***/ 0:
/*!***************************!*\
  !*** multi ./src/main.ts ***!
  \***************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__(/*! /home/tony/Code/private/tonyhammack.com/resources/templates/app/src/main.ts */"./src/main.ts");


/***/ })

},[[0,"runtime","vendor"]]]);
//# sourceMappingURL=main-es5.js.map