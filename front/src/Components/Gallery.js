import React, { Component } from "react";
import ActivePhoto from "./ActivePhoto";
import Grid from "./Grid";
import axios from "axios";

export default class Gallery extends Component
{
  state = { Sultans : [], Index : 9 };

	componentDidMount ()
	{
		axios.get ("http://127.0.0.1:5000/").then (Response => this.setState ({ Sultans : Response.data.Sultans }));
	}

	RenderPhotos = () =>
	{
		const { Sultans, Index } = this.state;
		if (Sultans.length) return <ActivePhoto Current = {Sultans [Index]}/>;
		return null;
	}

	RenderFlag = () =>
	{
    return (
			<div style = {{ height : "30%", width : "100%" }}>
			  <img src = { "http://127.0.0.1:5000/File/" + "Flag.png" } alt = "" style = {{ height : "90%", width : "70%" }}/>
	    </div>
		);
	}

	RenderTughra = () =>
	{
		const { Sultans, Index } = this.state;
		if (Sultans.length) return (
		  <div style = {{ background : "darkgrey", height : "40%", width : "100%" }}>
		    <img src = { "http://127.0.0.1:5000/File/" + Sultans [Index].Tughra } alt = "" style = {{ height : "100%", width : "100%" }}/>
			</div>
		);
		return null;
	}

	RenderText = () =>
	{
		const { Sultans, Index } = this.state;
		if (Sultans.length) return (
			<div>
				<h1>{ Sultans [Index].Name } { ["", "I", "II", "III", "IV", "V", "VI"][ Sultans [Index].Number] }</h1>
		    { Sultans [Index].Reign.map (Period => { return (<h2>{Period.Start} - {Period.End}</h2>) })}
			</div>
		);
	}

	ClickHandler = (Event) =>
	{
		const NewIndex = Event.target.getAttribute ("Index");
    this.setState ({ Index : NewIndex });
	}

	render ()
	{
    const { Sultans } = this.state;

		return (
			<div style = {Style}>
				<div style = {{ flex : 1 }}>
          { this.RenderPhotos () }
					<Grid Sultans = {Sultans} ClickHandler = {this.ClickHandler}/>
				</div>
				<div style = {{ flex : 1, padding : "40px", textAlign : "center" }}>
					{ this.RenderFlag () }
          { this.RenderText () }
					{ this.RenderTughra () }
				</div>
			</div>
		);
	}
}

const Style = 
{
	background : "grey",
	height : "650px",
	width : "1000px",
	margin : "20px auto",
	display : "flex",
	borderWidth : "3px", 
	borderStyle : "solid", 
	borderColor: "black"
};