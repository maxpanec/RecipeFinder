import React from "react";
import {Rating} from '@material-ui/lab';
import '../stylesheets/recipegrid.css';

function RecipeGrid(props) {

    const temp = [];
    if(props.searchInfo.loading)
        temp.push(
            <Loading key = '1'></Loading>
        );

    for(let [key, value] of Object.entries(props.searchInfo.recipes)){
        if(value == null)
            continue;
        for(let i = 0; i < value.length; i += 1){
            const foo = value[i];
            const bar = key + i;
            temp.push(
                <Recipe
                    name = {foo.name}
                    link = {foo.link}
                    stars = {foo.stars}
                    key = {bar}
                >
                </Recipe>
            );
        }
    }

    return(
        <div className = "results-grid">
            {temp}
        </div>
    );
}

function Recipe (props) {
    
    return(
        <div className='results-grid-item'>
            <div className = 'results-grid-item-wrapper'>
                <div className='results-gird-item-desc'> 
                    <a className = 'recipe-link' href={props.link} target="_blank" rel="noopener noreferrer">{props.name}</a>
                </div>
                <div className='results-gird-item-stars'> 
                    <Rating className = 'recipe-stars' value = {parseFloat(props.stars)} precision = {0.5} readOnly></Rating>
                </div>
            </div>
        </div>
    );
}

function Loading (props) {

    return(
        <span className='loading'>
            Loading...
        </span>
    );
}

export default RecipeGrid;