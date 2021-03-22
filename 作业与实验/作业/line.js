let width = 960, height = 640;
let margin = {
    top: 20,
    right: 30,
    bottom: 30,
    left: 40
};
let top_n = 12
let svg = d3
    .select('body').append('svg')
    .attr('width', width).attr('height', height)
d3.dsv(',', './driving.csv', function (item) {
    return {
        orient: item.side,
        name: item.year,
        x: +item.miles,
        y: +item.gas
    }
}).then(function (data) {

    data.x = 'Miles per person per year'
    data.y = 'Cost per gallon'

    console.log(data)
    console.log(d3.extent(data, item => item.y))
    x = d3.scaleLinear()
        .domain(d3.extent(data, item => item.x)).nice()
        .range([margin.left, width - margin.right])
    y = d3.scaleLinear()
        .domain(d3.extent(data, item => item.y)).nice()
        .range([height - margin.bottom, margin.top])
    xAxis = d3.axisBottom()
        .scale(x)
        .ticks(width / 100)
    svg
        .append('g')
        .attr('transform', `translate(${0}, ${height - margin.bottom})`)
        .call(xAxis)
    svg.call(item => item.select('.domain').remove())
    // .call 在该元素内部执行 body 可以选中svg，svg可以选中内部的g
    // d3.select('body').call(item => item.select('svg').style('background', 'blue'))
    svg.call(item =>
        item.selectAll('.tick line')
            .clone()
            .attr('y2', -height)
            .attr('stroke-opacity', 0.1)
    ).call(item =>
        item.append('text')
            .attr('x', width - margin.right - 4)
            .attr('y', height - margin.bottom - 4)
            .attr('font-weight', 'bold')
            .attr('text-anchor', 'end')
            .attr('fill', 'black')
            .text(data.x)
    )
    /*
    yAxis = d3.axisLeft()
        .scale(y)
        .ticks(null, '$.2f')
    */
    yAxis = g => g
        .attr('transform', `translate(${margin.left}, 0)`)
        .call(d3.axisLeft(y).ticks(null, '$.2f'))
        .call(g => g.select('.domain').remove())
        .call(g => g
            .selectAll('.tick line').clone()
            .attr('x2', width - margin.right)
            .attr('stroke-opacity', 0.1)
        )

    svg.append('g').call(yAxis)
}).catch(error => console.log(error))