import React from "react";
import GridElement from "./GridElement";

const Grid = ({ Sultans, ClickHandler }) =>
{
	return (
		<div style = {Style}>
			{
				Sultans.map ((Sultan, Index) => 
				{ 
					return (<GridElement key = {Sultan.ID} Image = {Sultan.Image} ClickHandler = {ClickHandler} Index = {Index}/>) 
				})
			}
		</div>
	);
}

const Style = 
{
	background : "lightgrey",
	height : "40%",
	width : "100%",
	display : "flex",
	flexWrap : "wrap",
	overflowY : "scroll"
};

export default Grid;