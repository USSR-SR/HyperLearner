import React from 'react'
import cardsStyle from '../styles/Cards.module.css'
import Card_item from '../components/Card_item'

function cards({articles}) {
  return (
    <div className={cardsStyle.main}>
      {articles.map((article) =>(
      <Card_item article={article}/>
      ))}
    </div>
  )
}

export default cards
