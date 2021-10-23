import React from 'react'
import card_itemStyle from '../styles/Card_item.module.css'

function Card_item({ article }) {
  return (
    <div className={card_itemStyle.main}>
      <div className ={card_itemStyle.text}>
        <p>{article.id}</p>
        <br/>
        {article.Title}
        <p>{article.Summary}</p>
        <p>{article.topic}</p>

      </div>
      <div>
      <div className ={card_itemStyle.img}>
        lol
      </div>
      <div className={card_itemStyle.author}>
        {article.author}
      </div>
      </div>
    </div>
  )
}

export default Card_item
