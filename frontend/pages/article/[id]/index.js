import {server} from '../../../config'
import { useRouter } from 'next/router'
import Sidebar from '../../../components/Sidebar'
import articleStyles from '../../../styles/article.module.css'
//
const article = ({article}) => {
  const router = useRouter()
    return (
      <div className={articleStyles.main}>
        <div className={articleStyles.body}>'
        <div className={articleStyles.side}> 
        <Sidebar/>
        </div>  
        <div className={articleStyles.middle}>
          <div className={articleStyles.heading}>
          <h1>{article.Title}</h1>       
          </div>
          <div className={articleStyles.text}>
          <h3>{article.Body}</h3>  
          <h4>{article.id}</h4>  
          </div>
        </div>
    </div>
    <button onClick={() => router.back()}> Back</button>

    </div>
    ) 
}
//
export const getStaticProps = async (context) => {
  const res = await fetch(`${server}/${context.params.id}`)
  const article = await res.json() 
  return {
    props: {
      article,
    }
  }
}
//
export const getStaticPaths = async (context) => {
  const res = await fetch(`${server}`)
  const articles = await res.json()

  console.log(articles);
  const ids = articles.map(article => article.id)
  console.log(ids);
  const paths = ids.map(id => ({params: {id: id.toString()}}));
  
  return {
    paths,
    fallback:false,
  }}
export default article

