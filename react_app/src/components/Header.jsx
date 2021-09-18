import React from 'react';
import '../stylesheets/header.css';

function Header(){

    return(
        <header className="header-container">
            <h1 className="title">
                <a href='http://localhost:3000/'>
                RecipeFinder
                </a>
            </h1>
        </header>
    );
}

export default Header;