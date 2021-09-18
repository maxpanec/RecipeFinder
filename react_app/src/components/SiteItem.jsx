import React, {useState} from 'react';
import '../stylesheets/siteitem.css';

function SiteItem(props){
    
    const [value, setValue] = useState(1);

    const selected = () => {
        const checkValue = document.getElementById(props.shortName);
        const tempValue = 1 - value;
        setValue(tempValue);
        checkValue.value = tempValue;
    };
    
    return(
        <span className="site-checkbox-container">
            <label className = "site-checkbox-label">{props.site}
                <input className = "site-checkbox" type="checkbox" defaultChecked  = {true} onChange={selected}></input>
            </label>
            <input type = "hidden" id = {props.shortName} name = {props.shortName} value = {value}></input>
        </span>
    );
}

export default SiteItem;