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
        text: 'Language stats',
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
