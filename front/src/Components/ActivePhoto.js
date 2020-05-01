import React from "react";

const ActivePhoto = ({ Current }) =>
{
	return (
		<div style = {Style}>
      <img src = { "http://127.0.0.1:5000/File/" + Current.Image } alt = "" style = {Image}/>
		</div>
	);
}

const Style = 
{
	background : "darkgrey",
	height : "60%",
	width : "100%",
};

const Image =
{
	height : "350px",
	width : "300px",
	paddingLeft : "100px",
	paddingRight : "100px",
	paddingTop : "20px"
}

export default ActivePhoto;