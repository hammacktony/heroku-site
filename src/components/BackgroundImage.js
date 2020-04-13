import React from 'react'

const BackgroundImage = props => {
    const backgroundImageStyle = {
        width: "100%",
        height: "350px",
        backgroundImage: "url(" + props.src + ")",
        backgroundSize: "cover"
    }
    return (
        <>
            <div style={backgroundImageStyle}>
                <h1>{props.text}</h1>
            </div>
        </>
    )
}

export default BackgroundImage
