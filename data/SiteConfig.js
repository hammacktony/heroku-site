const config = {
  siteTitle: 'Tony Hammack', // Site title.
  siteTitleShort: 'Tony Hammack', // Short site title for homescreen (PWA). Preferably should be under 12 characters to prevent truncation.
  siteTitleAlt: 'Tony Hammack', // Alternative site title for SEO.
  siteLogo: '', // Logo used for SEO and manifest.
  siteUrl: 'http://tonyhammack.com', // Domain of your website without pathPrefix.
  pathPrefix: '', // Prefixes all links. For cases when deployed to example.github.io/gatsby-advanced-starter/.
  siteDescription:
    'A place for my thoughts...', // Website description used for RSS feeds/meta description tag.
  siteRss: '/rss.xml', // Path to the RSS file.
  siteFBAppID: '', // FB Application ID for using app insights
  googleAnalyticsID: '', // GA tracking ID.
  dateFromFormat: 'YYYY-MM-DD', // Date format used in the frontmatter.
  dateFormat: 'DD/MM/YYYY', // Date format for display.
  userName: 'Tony Hammack', // Username to display in the author segment.
  userEmail: 'hammack.tony@gmail.com', // Email used for RSS feed's author segment
  userTwitter: '', // Optionally renders "Follow Me" in the Bio segment.
  userGitHub: 'hammacktony', // Optionally renders "Follow Me" in the Bio segment.
  userLocation: 'St. Louis, MO', // User location to display in the author segment.
  userAvatar: 'http://th-website.s3-website.us-east-2.amazonaws.com/user/img/imageedit_3_5218818746.gif', // User avatar to display in the author segment.
  userDescription:
    "I really enjoy coffee.", // User description to display in the author segment.
  copyright: 'Copyright © 2020. All rights reserved.', // Copyright string for the footer of the website and RSS feed.
  themeColor: '#c62828', // Used for setting manifest and progress theme colors.
  backgroundColor: 'red', // Used for setting manifest background color.
  backgroundImages: {
    general: 'https://th-website.s3.us-east-2.amazonaws.com/user/img/cover3.jpg',
    personal: 'https://th-website.s3.us-east-2.amazonaws.com/blog/img/blog-header.jpg',
    tech: 'https://th-website.s3.us-east-2.amazonaws.com/blog/img/laptop-blog.jpg'
  }
}

// Validate

// Make sure pathPrefix is empty if not needed
if (config.pathPrefix === '/') {
  config.pathPrefix = ''
} else {
  // Make sure pathPrefix only contains the first forward slash
  config.pathPrefix = `/${config.pathPrefix.replace(/^\/|\/$/g, '')}`
}

// Make sure siteUrl doesn't have an ending forward slash
if (config.siteUrl.substr(-1) === '/')
  config.siteUrl = config.siteUrl.slice(0, -1)

// Make sure siteRss has a starting forward slash
// if (config.siteRss && config.siteRss[0] !== "/")
//   config.siteRss = `/${config.siteRss}`;

module.exports = config
