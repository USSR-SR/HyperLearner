import React from 'react'
import card_itemStyle from '../styles/Card_item.module.css'
import Link from 'next/link'

function Card_item({ article }) {
  return (
    <div className={card_itemStyle.main}>
      {/* <Link href={`/article/${article.id}`}> */}
      <div className ={card_itemStyle.text}>
        <p>{article.id}</p>
        <br/>
        <p>{article.name}</p>
        <p>{article.subject}</p>
      </div>
      {/* </Link> */}
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
