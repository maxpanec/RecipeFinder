import React from 'react';
import SiteItem from "./SiteItem";
import '../stylesheets/search.css';

function Search(props){

    const setSearchInfo = props.setSearchInfo;
    const searchInfo = props.searchInfo;

    const search = async () => {
        const myForm = new FormData(document.getElementById("temp-my-form"));
        const search_data = {};
        let baseUrl ="/scrape?";
        for(var pair of myForm.entries()){
            baseUrl += pair[0] + "=" + pair[1] + "&";
            search_data[pair[0]] = pair[1];
        }
        if(search_data["search"] === "")
            return;
        setSearchInfo(
            {
                recipes: [],
                loading: true,
                searching: true
            }
        );
        baseUrl = baseUrl.substring(0, baseUrl.length-1);

        const response = await fetch(baseUrl);
        const data = await response.json();
        setSearchInfo(
            {
                recipes: data,
                loading: false,
                searching: false
            }
        );   
    };
    
    const dropdown = () => {
        const container = document.getElementById("search-options-flex-wrapper");
        if(container.hidden){
            container.style.display = "inline-block";
            container.hidden=false;
        }
        else{
            container.style.display = "none";
            container.hidden=true;
        }
    };

    const preventSubmit = (e) => {
        e.preventDefault();
        if(!searchInfo.searching){
            search();
        }
    }

    const updateSlider = () => {
        const slideCounter = document.getElementById("slider-counter");
        const slideValue = document.getElementById("search-slider").value;
        slideCounter.innerHTML = slideValue;
    };
    
    return(
        <form className = "search-form" id = "temp-my-form" onSubmit = {preventSubmit}>
            <div className="search-textbox-container">
                <input type="textbox" className="search-textbox" name = "search"></input>
                <i className="material-icons" id='search-icon' onClick={search}>search</i>
            </div>
            <div className = "search-button-wrapper">
                <div className="search-button-container" onClick={dropdown}> 
                    <input type="button" value="Search Options" name = "search-button" className="search-button"></input>
                    <i className="material-icons" id='search-drop-arrow'>arrow_drop_down</i>
                </div>
            </div>

            <div className="search-options-flex-wrapper"  id="search-options-flex-wrapper" hidden>  
                <div className="search-options-flex-container">
                    <div className="search-options-flex-child">
                        <div className="site-options-grid-container">
                            <SiteItem site="Allrecipes" shortName = "allrecipes"></SiteItem>
                            <SiteItem site="Epicurious" shortName = "epicurious"></SiteItem>
                            <SiteItem site="Bon Appétit" shortName = "bonappetit"></SiteItem>
                            <SiteItem site="Food Network" shortName = "foodnetwork"></SiteItem>
                        </div>
                    </div>   
                    <div className="search-options-flex-child">
                        <div className="search-slider-container">
                            <p>Max Results Per Site: <span id="slider-counter">4</span></p>
                            <input type="range" min="1" max="7" defaultValue="4" id = "search-slider" name="range" onInput = {updateSlider}></input>
                        </div>
                    </div>
                </div>
            </div>
        </form>
    );
}

export default Search;