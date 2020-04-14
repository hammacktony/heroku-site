import React from 'react'
import Helmet from 'react-helmet'
import { graphql } from 'gatsby'
import Layout from '../layout'
import PostListing from '../components/PostListing'
import config from '../../data/SiteConfig'
import BackgroundImage from '../components/BackgroundImage'

const CategoryTemplate = ({ data, pageContext }) => {
  const siteTitle = `${pageContext.category} - ${config.siteTitle}`
  const backgroundImage = config.backgroundImages[pageContext.category.toLowerCase()]
  const headingText = `${pageContext.category} Blog`
  const headingStyle = { 'text-align': 'center' }

  return (
    <Layout>
      <main>
        <Helmet title={siteTitle} />
        <BackgroundImage src={backgroundImage} />
        <h1 style={headingStyle}>
          {headingText}
        </h1>
        <PostListing postEdges={data.allMarkdownRemark.edges} />
      </main>
    </Layout>
  )
}

export default CategoryTemplate

/* eslint no-undef: "off" */
export const pageQuery = graphql`
  query CategoryPage($category: String) {
    allMarkdownRemark(
      limit: 1000
      sort: { fields: [fields___date], order: DESC }
      filter: { frontmatter: { categories: { in: [$category] } } }
    ) {
      totalCount
      edges {
        node {
          fields {
            slug
            date(formatString: "MMMM DD, YYYY")
          }
          excerpt
          timeToRead
          frontmatter {
            title
            tags
            cover
            date
            categories
          }
        }
      }
    }
  }
`
