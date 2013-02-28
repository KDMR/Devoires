<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Slideshow by PHP</title>
    <link rel="stylesheet" type="text/css" href="slideshow.css" />
    <script type="text/javascript" src="../zepto.js"></script>
    <script type="text/javascript" src="slideshow.js" ></script>
    <style type="text/css">
        /* Global Config
        -------------------------------------------------- */

        *{
            padding: 0;
            margin: 0;
        }

        /* SlideShow
        -------------------------------------------------- */

        div.container{
            width       : 980px;
            margin      : 0 auto;
            padding-top : 1px;
        }

        div.slideshow{
            width      : 650px;
            height     : 300px;
            margin     : 30px auto 0;
            overflow   : hidden;
            position   : relative;
            background-image    : url('../images/loading.gif');
            background-repeat   : no-repeat;
            background-position : center center;
            outline:1px solid black;
        }

        div.slideshow div.train{
            width:1000px;
            height : inherit;
        }
        div.slideshow div.train > div{
            height : inherit;
            float  : left;
            background-repeat   : no-repeat;
            background-position : left top;
        }

        div.active {
            -webkit-transform: opacity 1;
            -moz-transform: opacity 1;
            -ms-transform: opacity 1;
            -o-transform: opacity 1;
            transform: opacity 1;
        }

        div.notActive {
            -webkit-transition: opacity 500ms 0.5;
            -moz-transition: opacity 500ms 0.5;
            -ms-transition: opacity 500ms 0.5;
            -o-transition: opacity 500ms 0.5;
            transition: opacity 500ms 0.5;
        }
        </style>
        <script type="text/javascript">
                        $(document).ready(function(){
                $('div.slideshow div.train > div').css('width',Math.ceil(650/5)+'px');
            })


            var divs = getElementsByClassName('train').item(0).getElementsByTagName('div');
            var i;  
            for (i=0 ; i<divs.length ; i++) {
                divs.item(i).className = 'notActive';
            }

            divs.item(i).onmouseover = function () {
                divs.item(i).className = 'active';
            }

            divs.item(i).onmouseout = function () {
                divs.item(i).className = 'notActive';
            }
        </script>
</head>
<body>
    <div class="container">
        <div class="slideshow">
            <div class="train">
                <?php

                $laRoute = '../images';
                $allImages = scandir($laRoute);
                $slidesNum = 0;
                foreach($allImages as $img){
                    $imgs_arr = explode('.', $img);
                    $imgs_type = strtolower( end($imgs_arr) );
                    if ($imgs_type=='jpg') {
                        echo "<div style=\"background-image:url('$laRoute/$img');\"></div>";
                        $slidesNum++;
                    }
                }
                ?>
            </div>
        </div>
    </div>
</body>
</html>
