import Head from 'next/head'
import styles from '../styles/Home.module.css'
import Navbar from '../components/Navbar'
import Hero from '../components/Hero'
import Cards from '../components/Cards'
import { server } from '../config'
export default function Home({articles}) {
  return (
    <div className={styles.container}>
      <Head>
        <title>Create Next App</title>
        <link rel="icon" href="/favicon.ico"/>
      </Head>
      <Hero/>
    <Cards articles ={articles}/>
    </div>
  )
}

export const getStaticProps = async () => {
  const res = await fetch(`${server}`)
  const articles = await res.json();
  return{
    props:{
      articles
    },
  }

}
