import React, {useState} from "react";
import Header from './Header';
import Search from './Search';
import RecipeGrid from './RecipeGrid';

function Display() {
    
    const [searchInfo, setSearchInfo] = useState(
        {
            recipes: [],
            loading: false,
            searching: false
        }
    );

    return(
        <div>
            <Header></Header>
            <Search setSearchInfo = {setSearchInfo} searchInfo = {searchInfo}></Search>
            <RecipeGrid searchInfo = {searchInfo}></RecipeGrid>
        </div>
    ); 
}

export default Display;