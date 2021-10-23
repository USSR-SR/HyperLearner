import React from 'react'
import heroStyles from '../styles/Hero.module.css'
import {motion} from 'framer-motion'
import Typical from 'react-typical'

function Hero() {
  return (
    <div class ={heroStyles.main}>
      <div>Welcome to </div>
        <Typical className={heroStyles.ani_text}
        steps = {[
          "Success...!",
          2500,
          "Fun...!",
          2500,
          "Learning...",
          2500,
          "HyperLearning...!!",
          5000,

        ]}
        loop ={Infinity}
        wrapper ='p'/>
    </div>
  )
}

export default Hero
