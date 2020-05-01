import React from "react";

const GridElement = ({ Image, ClickHandler, Index }) =>
{
	return (
		<div style = {Style}>
			<img src = { "http://127.0.0.1:5000/File/" + Image } alt = "" style = {ImageStyle} onClick = {ClickHandler} Index = {Index}/>
		</div>
	);
}

const Style = 
{
	background : "white",
	height : "50%",
	width : "25%",
	position : "relative",
	cursor : "pointer"
};

const ImageStyle =
{
	height : "100%",
	width : "100%"
}

export default GridElement;