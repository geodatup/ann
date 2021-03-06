
var pathObj = {
    "signature_ann": {
        "strokepath": [
            {
                "path": "m 175,522.3622 c 0,0 34.28571,-115 65.71429,-162.14285",
                "duration": 800
            },
            {
                "path": "m 224.28571,364.50506 c 0,0 18.57142,81.42857 25,97.85714 6.50714,16.62934 19.28572,30.71429 19.28572,35",
                "duration": 400
            },
            {
                "path": "M 166.42857,465.21935 283.57143,445.93363",
                "duration": 400
            },
            {
                "path": "M 327.14286,393.79078 307.85714,516.64792",
                "duration": 400
            },
            {
                "path": "m 402.14286,404.50506 c 0,0 -27.14286,79.28572 -25.71429,91.42857",
                "duration": 400
            },
            {
                "path": "m 306.42857,404.50506 c 31.81969,21.22013 58.51215,72.79212 94.28572,79.28572",
                "duration": 400
            },
            {
                "path": "m 445,395.21935 c 0,0 -5,74.28571 -15.71429,92.85714",
                "duration": 400
            },
            {
                "path": "m 513.57143,393.07649 c 0,0 -25.71429,77.85714 -2.14286,89.28571",
                "duration": 400
            },
            {
                "path": "m 417.85714,410.21935 c 0,0 74.28572,84.28571 97.14286,46.42857",
                "duration": 400
            },
            {
                "path": "m 632.85714,310.21935 c 0,0 -42.14285,50 -54.28571,123.57143",
                "duration": 400
            },
            {
                "path": "m 607.85714,499.50506 c 0,0 -1.42857,5 5,9.28572",
                "duration": 400
            }
        ],
        "dimensions": {
            "width": 745,
            "height": 1053
        }
    }
}; 
 
 
/* 
 Setup and Paint your lazyline! 
 */

 
 $(document).ready(function(){ 
 $('#signature_ann').lazylinepainter( 
 {
    "svgData": pathObj,
    "strokeWidth": 12,
    "strokeColor": "#777"
}).lazylinepainter('paint'); 
 });