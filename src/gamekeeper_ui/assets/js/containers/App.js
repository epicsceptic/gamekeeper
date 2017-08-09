import React from 'react'
import Body from '../containers/Body'
import MainHeader from '../containers/MainHeader'


var App = React.createClass({
    
    componentDidMount: function(){
	$.ajax({
            url: '127.0.0.1:8000/players/?format=json',
            datatype: 'json',
            cache: false,
            success: function(data) {
                alert({data: data});
            }.bind(this)
        })
    },
    
    render: function() {
	return (
	    <div>
		<MainHeader />
		<Body />
	    </div>
	)
    }
})

export default App
