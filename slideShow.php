<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Slideshow by PHP</title>
    <link rel="stylesheet" type="text/css" href="main.css" />
    <script type="text/javascript" src="../zepto.js"></script>
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
            width : 980px;
            margin : 0 auto;
            padding-top : 1px;
        }

        div.slideshow{
            width : 650px;
            height : 300px;
            margin : 30px auto 0;
            overflow : hidden;
            position : relative;
            background-image : url('../images/loading.gif');
            background-repeat : no-repeat;
            background-position : center center;
            outline:1px solid black;
        }

        div.slideshow div.train{
            width:1000px;
            height : inherit;
        }
        div.slideshow div.train > div{
            height : inherit;
            float : left;
            background-repeat : no-repeat;
            background-position : left top;
        }

        .active {
            -webkit-filter: grayscale(0%);
               -moz-filter: grayscale(0%);
                -ms-filter: grayscale(0%);
                 -o-filter: grayscale(0%);
                    filter: grayscale(0%);
        }

        .inactive {
            -webkit-filter: grayscale(100%);
               -moz-filter: grayscale(100%);
                -ms-filter: grayscale(100%);
                 -o-filter: grayscale(100%);
                    filter: grayscale(100%);
        } 
    </style>
    <script type="text/javascript">
        $(document).ready(function(){
            $('div.slideshow div.train > div').css('width',Math.ceil(650/5)+'px');
        })

            window.onload = function (){
                
                var container = document.getElementsByClassName('container').item(0);
                var slideshow = container.getElementsByClassName('slideshow').item(0);
                var train = slideshow.getElementsByClassName('train').item(0);
                var divs = train.getElementsByTagName('div');
               
                

                for (var i=0; i<divs.length; i++) {
                    
                    divs[i].className = 'inactive'; /*This could also be : $('div.slideshow div.train > div').addClass('inactive'); */

                    (function(j){

                        divs.item(j).onmouseout = function (){
                            divs.item(j).className = 'inactive';
                        };

                        divs.item(j).onmouseover = function (){
                            divs.item(j).className = 'active';
                        };


                    })(i);
                }
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
    <script type="text/javascript" src="slideshow.js" ></script>
</body>
</html>
