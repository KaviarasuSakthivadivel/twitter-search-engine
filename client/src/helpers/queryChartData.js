import Highcharts from 'highcharts'
import worldMap from '@highcharts/map-collection/custom/world.geo.json'

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
        type: 'spline',
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
        enabled: true,
    },
    plotOptions: {
        series: {
            marker: {
                enabled: false,
            },
        },
        area: {
            fillColor: {
                linearGradient: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 1,
                },
                stops: [
                    [0, Highcharts.getOptions().colors[1]],
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

    series: [],
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
            text: ' Tweets count by country',
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
            text: ' Tweets count by sentiment',
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

export const vaccineHesistancyChart = {
    chart: {
        type: 'column',
    },
    title: {
        text: 'Vaccine Hesistancy',
    },
    accessibility: {
        announceNewData: {
            enabled: true,
        },
    },
    xAxis: {
        type: 'category',
    },
    yAxis: {
        title: {
            text: 'Hesistancy rate',
        },
    },
    legend: {
        enabled: false,
    },
    plotOptions: {
        series: {
            borderWidth: 0,
            dataLabels: {
                enabled: true,
                format: '{point.y:.1f}%',
            },
        },
    },

    tooltip: {
        headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
        pointFormat:
            '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b><br/>',
    },

    series: [
        {
            name: 'Negative Tweets',
            colorByPoint: true,
            data: [],
        },
    ],
}

export const worldMapChart = {
    chart: {
        type: 'map',
        map: worldMap,
    },

    title: {
        text: 'Tweets count by Location',
    },

    mapNavigation: {
        enabled: true,
        enableDoubleClickZoomTo: true,
    },
    colorAxis: {
        min: 1,
        max: 1000,
        type: 'logarithmic',
    },
    series: [
        {
            data: [
                {
                    code3: 'USA',
                    name: 'United States',
                    value: 152573,
                    code: 'US',
                },
                {
                    code3: 'IND',
                    name: 'India',
                    value: 45897,
                    code: 'IN',
                },
                {
                    code3: 'MEX',
                    name: 'Mexico',
                    value: 66346,
                    code: 'MX',
                },
            ],
            joinBy: ['iso-a3', 'code3'],
            name: 'Tweet count',
            states: {
                hover: {
                    color: '#a4edba',
                },
            },
            tooltip: {
                valueSuffix: '',
            },
        },
    ],
}

export const covidVsPoiUSACurve = {
    chart: {
        zoomType: 'xy',
    },
    title: {
        text: 'USA COVID Curve vs POI COVID related tweets',
    },
    xAxis: [
        {
            type: 'catergory',
        },
    ],
    yAxis: [
        {
            // Primary yAxis
            labels: {
                format: '{value}',
                style: {
                    color: Highcharts.getOptions().colors[1],
                },
            },
            title: {
                text: 'COVID Cases',
                style: {
                    color: Highcharts.getOptions().colors[1],
                },
            },
            opposite: true,
        },
        {
            // Secondary yAxis
            gridLineWidth: 0,
            title: {
                text: 'Tweets Count',
                style: {
                    color: Highcharts.getOptions().colors[0],
                },
            },
            labels: {
                format: '{value}',
                style: {
                    color: Highcharts.getOptions().colors[0],
                },
            },
        },
    ],
    tooltip: {
        shared: true,
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        x: 80,
        verticalAlign: 'top',
        y: 55,
        floating: true,
        backgroundColor:
            Highcharts.defaultOptions.legend.backgroundColor || // theme
            'rgba(255,255,255,0.25)',
    },
    series: [
        {
            name: 'COVID Curve',
            type: 'spline',
            yAxis: 1,
            data: [
                1016, 1016, 1015.9, 1015.5, 1012.3, 1009.5, 1009.6, 1010.2,
                1013.1, 1016.9, 1018.2, 1016.7,
            ],
            marker: {
                enabled: false,
            },
            dashStyle: 'shortdot',
        },
        {
            name: 'POI COVID Tweets',
            type: 'spline',
            data: [
                7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9,
                9.6,
            ],
        },
    ],
}
