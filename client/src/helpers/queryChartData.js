import Highcharts from 'highcharts'
export const poiChartData = {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie',
    },
    title: {
        text: 'POI stats',
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>',
    },
    accessibility: {
        point: {
            valueSuffix: '%',
        },
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: false,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %',
            },
            showInLegend: true,
        },
    },
    series: [
        {
            name: 'POI',
            colorByPoint: true,
            data: [],
        },
    ],
}
export const langChartData = {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie',
    },
    title: {
        text: 'Language wise stats',
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>',
    },
    accessibility: {
        point: {
            valueSuffix: '%',
        },
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: false,
            },
            showInLegend: true,
            innerSize: 100,
            depth: 45,
        },
    },
    series: [
        {
            name: 'Language',
            colorByPoint: true,
            data: [],
        },
    ],
}
export const countryChartData = {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie',
    },
    title: {
        text: 'Country wise stats',
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>',
    },
    accessibility: {
        point: {
            valueSuffix: '%',
        },
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: false,
            },
            showInLegend: true,
        },
    },
    series: [
        {
            name: 'Language',
            colorByPoint: true,
            data: [],
        },
    ],
}
export const sentimentChartData = {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie',
    },
    title: {
        text: 'Sentiment Analysis',
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>',
    },
    accessibility: {
        point: {
            valueSuffix: '%',
        },
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: false,
            },
            showInLegend: true,
        },
    },
    series: [
        {
            name: 'Sentiment',
            colorByPoint: true,
            data: [],
        },
    ],
}

export const wordCloudData = {
    accessibility: {
        screenReaderSection: {
            beforeChartFormat:
                '<h5>{chartTitle}</h5>' +
                '<div>{chartSubtitle}</div>' +
                '<div>{chartLongdesc}</div>' +
                '<div>{viewTableButton}</div>',
        },
    },
    series: [
        {
            type: 'wordcloud',
            data: [],
            name: 'Occurrences',
        },
    ],
    title: {
        text: 'Wordcloud for Top 50 Hashtags',
    },
}

export const timeSeriesData = {
    chart: {
        zoomType: 'x',
    },
    title: {
        text: 'Tweets count vs Tweet date',
    },
    subtitle: {
        text:
            document.ontouchstart === undefined
                ? 'Click and drag in the plot area to zoom in'
                : 'Pinch the chart to zoom in',
    },
    xAxis: {
        type: 'datetime',
    },
    yAxis: {
        title: {
            text: 'Tweets count',
        },
    },
    legend: {
        enabled: false,
    },
    plotOptions: {
        area: {
            fillColor: {
                linearGradient: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 1,
                },
                stops: [
                    [0, Highcharts.getOptions().colors[0]],
                    [
                        1,
                        Highcharts.color(Highcharts.getOptions().colors[0])
                            .setOpacity(0)
                            .get('rgba'),
                    ],
                ],
            },
            marker: {
                radius: 2,
            },
            lineWidth: 1,
            states: {
                hover: {
                    lineWidth: 1,
                },
            },
            threshold: null,
        },
    },

    series: [
        {
            type: 'area',
            name: 'Tweet count',
            data: [],
        },
    ],
}

export const sentimentTimeSeriesData = {
    chart: {
        zoomType: 'x',
    },
    title: {
        text: 'Sentiment time series',
    },
    subtitle: {
        text:
            document.ontouchstart === undefined
                ? 'Click and drag in the plot area to zoom in'
                : 'Pinch the chart to zoom in',
    },
    xAxis: {
        type: 'datetime',
    },
    yAxis: {
        title: {
            text: 'Tweets count by sentiment',
        },
    },
    legend: {
        enabled: false,
    },
    plotOptions: {
        area: {
            fillColor: {
                linearGradient: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 1,
                },
                stops: [
                    [0, Highcharts.getOptions().colors[0]],
                    [
                        1,
                        Highcharts.color(Highcharts.getOptions().colors[0])
                            .setOpacity(0)
                            .get('rgba'),
                    ],
                ],
            },
            marker: {
                radius: 2,
            },
            lineWidth: 1,
            states: {
                hover: {
                    lineWidth: 1,
                },
            },
            threshold: null,
        },
    },

    series: [
        {
            type: 'area',
            name: 'Tweet count by sentiment',
            data: [],
        },
    ],
}

export const vaccineMentionsByCountryData = {
    chart: {
        type: 'column',
    },
    title: {
        text: 'Vaccine mention by country',
    },
    xAxis: {
        categories: [],
    },
    yAxis: {
        min: 0,
        title: {
            text: ' Vaccine sentiment by Country',
        },
        stackLabels: {
            enabled: true,
            style: {
                fontWeight: 'bold',
                color:
                    // theme
                    (Highcharts.defaultOptions.title.style &&
                        Highcharts.defaultOptions.title.style.color) ||
                    'gray',
            },
        },
    },
    legend: {
        align: 'right',
        x: -30,
        verticalAlign: 'top',
        y: 25,
        floating: true,
        backgroundColor:
            Highcharts.defaultOptions.legend.backgroundColor || 'white',
        borderColor: '#CCC',
        borderWidth: 1,
        shadow: false,
    },
    tooltip: {
        headerFormat: '<b>{point.x}</b><br/>',
        pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}',
    },
    plotOptions: {
        column: {
            stacking: 'normal',
            dataLabels: {
                enabled: true,
            },
        },
    },
    series: [],
}

export const vaccineCompaniesBySentimentData = {
    chart: {
        type: 'column',
    },
    title: {
        text: 'Covid Vaccine Sentiment',
    },
    xAxis: {
        categories: [],
    },
    yAxis: {
        min: 0,
        title: {
            text: ' Vaccine sentiment',
        },
        stackLabels: {
            enabled: true,
            style: {
                fontWeight: 'bold',
                color:
                    // theme
                    (Highcharts.defaultOptions.title.style &&
                        Highcharts.defaultOptions.title.style.color) ||
                    'gray',
            },
        },
    },
    legend: {
        align: 'right',
        x: -30,
        verticalAlign: 'top',
        y: 25,
        floating: true,
        backgroundColor:
            Highcharts.defaultOptions.legend.backgroundColor || 'white',
        borderColor: '#CCC',
        borderWidth: 1,
        shadow: false,
    },
    tooltip: {
        headerFormat: '<b>{point.x}</b><br/>',
        pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}',
    },
    plotOptions: {
        column: {
            stacking: 'normal',
            dataLabels: {
                enabled: true,
            },
        },
    },
    series: [],
}
