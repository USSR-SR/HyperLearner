import React from 'react'
import Link from 'next/link'
import navStyles from '../styles/Nav.module.css'

function Nav() {
    return (
        <nav className ={navStyles.nav}>
            <ul>
                <li>
                    <Link href='/'>
                        Home
                    </Link>
                </li>
                <li>
                    <Link href='/signin'>
                        Signin
                    </Link>
                </li>
                <li>
                    <Link href='/signup'>
                        Signup
                    </Link>
                </li>
            </ul>
        </nav>
    )
}

export default Nav
