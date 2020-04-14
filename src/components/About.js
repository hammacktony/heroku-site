import React from 'react'
import config from '../../data/SiteConfig'
import BackgroundImage from '../components/BackgroundImage'

const About = () => (
  <>
    <BackgroundImage src={config.backgroundImages.general} />
    <p>As an avid reader and podcast listener, I love to embrace the challenge of learning new things that are outside my realm of knowledge. I believe that human life has nearly unlimited potential, and the only key to unlock it is through knowledge and grit. My goal is to use my resources and talents to affect change in this world, and help everyone reach their potential.
    </p>
    <p>
      I like to dabble and tinker with multiple technologies with the goal of solving intriguing problems and puzzles. Stay tuned for more projects, and if you have any more questions, feel free to contact me.
    </p>
  </>
)

export default About
