var React = require("react");

var HelloWorldPage = React.createClass({
    render: function () {
        return (
            <div className="hello-world-page">
                <h1>Hello World!</h1>
                <p>这是一个简单的Hello World应用</p>
                <div className="hello-content">
                    <h2>欢迎来到Arachnado项目</h2>
                    <p>你现在看到的是一个嵌入到Arachnado爬虫项目中的Hello World页面。</p>
                    <button onClick={this.handleClick}>
                        点击我！
                    </button>
                    <p className="message">{this.state.message}</p>
                </div>
            </div>
        );
    },

    getInitialState: function() {
        return {
            message: ''
        };
    },

    handleClick: function() {
        this.setState({
            message: '你点击了按钮！Hello World! 🎉'
        });
    }
});

module.exports = { HelloWorldPage };