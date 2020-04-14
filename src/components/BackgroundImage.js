import React from 'react'

const BackgroundImage = props => {
    const backgroundImageStyle = {
        width: "100%",
        height: "350px",
        backgroundImage: "url(" + props.src + ")",
        backgroundSize: "cover",
        marginBottom: '10px'
    }
    return (
        <>
            <div style={backgroundImageStyle} />
        </>
    )
}

export default BackgroundImage
