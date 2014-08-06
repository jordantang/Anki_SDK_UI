
        $(document).ready(function () {
            $(".difficultybutton").click(function () {
                $(".difficultysettings").toggle();
            });
        });



        $(document).ready(function () {
            $("#basicspeedbutton").click(function () {
                $("#basicspeedform").slideToggle();
            });
        });




        $(document).ready(function () {
            $("#basiclightsbutton").click(function () {
                $("#basiclightsform").slideToggle();
            });
        });


        $(document).ready(function () {
            $("#basicwaitbutton").click(function () {
                $("#basicwaitform").slideToggle();
            });
        });



        $(document).ready(function () {
            $("#basiclanebutton").click(function () {
                $("#basiclaneform").slideToggle();
            });
        });



        $(document).ready(function () {
            $("#advspeedbutton").click(function () {
                $("#advspeedform").slideToggle();
            });
        });


        $(document).ready(function () {
            $("#advlightsbutton").click(function () {
                $("#advlightsform").slideToggle();
            });
        });



        $(document).ready(function () {
            $("#advlanebutton").click(function () {
                $("#advlaneform").slideToggle();
            });
        });


        $(document).ready(function () {
            $("#advwaitbutton").click(function () {
                $("#advwaitform").slideToggle();
            });
        });





        $(document).ready(function () {
            $("li.basicdifficulty").click(function () {
                $(".basicgroup").show(400);
                $(".advancedgroup").hide();
            });
        });


        $(document).ready(function () {
            $("li.advanceddifficulty").click(function () {
                $(".advancedgroup").show(400);
                $(".basicgroup").hide();
            });
        });




        $(function () {
            $('.tags_select a').click(function () {
                var value = $(this).text();
                var input = $('.prntscreenstyle');
                input.val(input.val() + value + ', ');
                return false;
            });
        });




        $(document).ready(function () {
            $("#resetbuttonbasic").click(function () {
                $(".duration-group").hide();
            });
        });

        $(document).ready(function () {
            $("#resetbuttonadv").click(function () {
                $(".duration-groupadv").hide();
            });
        });


        $(document).ready(function () {
            var lightstatus = $('select.lightstatus-dropwdown').val(); //no :selected here

            $('select.lightstatus-dropdown').change(function () {
                lightstatus = $(this).val();
                if (lightstatus == "on_for") {
                    $('.duration-group').show();
                } else {
                    $('.duration-group').hide();
                }
            });
        });

$(document).ready(function () {
            var lightstatus = $('select.lightstatus-dropwdownadv').val(); //no :selected here

            $('select.lightstatus-dropdownadv').change(function () {
                lightstatus = $(this).val();
                if (lightstatus == "on_for") {
                    $('.duration-groupadv').show();
                } else {
                    $('.duration-groupadv').hide();
                }
            });
        });
    
    function addCode(block, mode) {
        var type, text = "", form, count = 0, pulldown;
        if(block == "speed") {
            type = "<div class='column' draggable='true' data-car data-speed data-accel><header>SPEED</header> <body><style='color:#000000'></body></div>";
            if(mode == "bas") {
                form = document.getElementById("basicspeedform");
                pulldown = document.getElementById("speedCar");
            }
            else {
                form = document.getElementById("advspeedform");
                pulldown = document.getElementById("advSpeedCar");
            }
            text += "Car = " + pulldown.options[pulldown.selectedIndex].text + " ";
            text += "Speed = " + form.elements[1].value + " ";
            text += "Acceleration = " + form.elements[2].value;
            $("#columns").append(type);
            document.getElementById("columns").lastChild.innerHTML = '<header>SPEED</header> <body>' + text +' </body>';
        }
        else if(block == "lights") {
            type = "<div class='column' draggable='true' data-car data-loc data-type data-start data-light><header>LIGHTS</header> <body><style='color:#000000' id='data'></body></div>";
            if(mode == "bas") {
                form = document.getElementById("basiclightsform");
                pulldown = document.getElementById("lightCar");
                text += "Car = " + pulldown.options[pulldown.selectedIndex].text + " ";
                pulldown = document.getElementById("location");
                text += "Location = " + pulldown.options[pulldown.selectedIndex].text + " ";
                pulldown = document.getElementById("type");
                text += "Type = " + pulldown.options[pulldown.selectedIndex].text + " ";
                text += "Start Time = " + form.elements[3].value + " ";
                pulldown = document.getElementById("status");
                text += "Status = " + pulldown.options[pulldown.selectedIndex].text;
                if(pulldown.options[pulldown.selectedIndex].text == "On for:") {
                    text += " " + form.elements[5].value + " seconds";
                }
            }
            else {
                form = document.getElementById("advlightsform");
                pulldown = document.getElementById("advLightCar");
                text += "Car = " + pulldown.options[pulldown.selectedIndex].text + " ";
                pulldown = document.getElementById("advLoc");
                text += "Location = " + pulldown.options[pulldown.selectedIndex].text + " ";
                pulldown = document.getElementById("advType");
                text += "Type = " + pulldown.options[pulldown.selectedIndex].text + " ";
                text += "Start Time = " + form.elements[3].value + " ";
                pulldown = document.getElementById("advStatus");
                text += "Status = " + pulldown.options[pulldown.selectedIndex].text;
                if(pulldown.options[pulldown.selectedIndex].text == "On for:") {
                   text += " " + form.elements[5].value + " seconds";
                }
            }
            $("#columns").append(type);
            document.getElementById("columns").lastChild.innerHTML = '<header>LIGHTS</header> <body>' + text +' </body>';
        }
        else if(block == "lane") {
            type = "<div class='column' draggable='true'><header>LANE</header> <body><style='color:#000000' id='data'></body></div>";
            if(mode == "bas") {
                form = document.getElementById("basiclaneform");
                pulldown = document.getElementById("laneCar");
                text += "Car = " + pulldown.options[pulldown.selectedIndex].text + " ";
                text += "Speed = " + form.elements[1].value + " ";
                text += "Lane = " + form.elements[2].value + " ";
            }
            else {
                form = document.getElementById("advlaneform");
                pulldown = document.getElementById("advLaneCar");
                text += "Car = " + pulldown.options[pulldown.selectedIndex].text + " ";
                text += "Speed = " + form.elements[1].value + " ";
                text += "Lane = " + form.elements[2].value + " ";
            }
            $("#columns").append(type);
            document.getElementById("columns").lastChild.innerHTML = '<header>LANE</header> <body>' + text +' </body>';
        }
        else if(block == "wait") {
            type = "<div class='column' draggable='true'><header>WAIT</header> <body><style='color:#000000' id='data></body></div>";
            if(mode == "bas") {
                form = document.getElementById("basicwaitform");
                pulldown = document.getElementById("waitCar");
            }
            else {
                form = document.getElementById("advwaitform");
                pulldown = document.getElementById("advWaitCar");
            }
            text += "Car = " + pulldown.options[pulldown.selectedIndex].text + " ";
            text += form.elements[1].value;
            $("#columns").append(type);
            document.getElementById("columns").lastChild.innerHTML = '<header>WAIT</header> <body>' + text +' </body>';
        }
        //document.getElementById("data").innerHTML = text;
        var cols = document.querySelectorAll('#columns .column');
        [].forEach.call(cols, function(col) {
            col.addEventListener('dragstart', handleDragStart, false);
            col.addEventListener('dragenter', handleDragEnter, false)
            col.addEventListener('dragover', handleDragOver, false);
            col.addEventListener('dragleave', handleDragLeave, false);
            col.addEventListener('drop', handleDrop, false);
            col.addEventListener('dragend', handleDragEnd, false);
        });
       //document.getElementById("data").innerHTML = text;
    }
    
function handleDragStart(e) {
  this.style.opacity = '1';  // this / e.target is the source node.
}

function handleDragOver(e) {
  if (e.preventDefault) {
    e.preventDefault(); // Necessary. Allows us to drop.
  }

  e.dataTransfer.dropEffect = 'move';  // See the section on the DataTransfer object.

  return false;
}

function handleDragEnter(e) {
  // this / e.target is the current hover target.
  this.classList.add('over');
}

function handleDragLeave(e) {
  this.classList.remove('over');  // this / e.target is previous target element.
}
    
function handleDrop(e) {
  // this / e.target is current target element.

  if (e.stopPropagation) {
    e.stopPropagation(); // stops the browser from redirecting.
  }

  // See the section on the DataTransfer object.

  return false;
}

function handleDragEnd(e) {
  // this/e.target is the source node.

  [].forEach.call(cols, function (col) {
    col.classList.remove('over');
  });
}

/*var cols = document.querySelectorAll('#columns .column');
[].forEach.call(cols, function(col) {
  col.addEventListener('dragstart', handleDragStart, false);
  col.addEventListener('dragenter', handleDragEnter, false)
  col.addEventListener('dragover', handleDragOver, false);
  col.addEventListener('dragleave', handleDragLeave, false);
  col.addEventListener('drop', handleDrop, false);
  col.addEventListener('dragend', handleDragEnd, false);
});*/
    
var dragSrcEl = null;

function handleDragStart(e) {
  // Target (this) element is the source node.
  this.style.opacity = '1';

  dragSrcEl = this;

  e.dataTransfer.effectAllowed = 'move';
  e.dataTransfer.setData('text/html', this.innerHTML);
}

function handleDrop(e) {
  // this/e.target is current target element.

  if (e.stopPropagation) {
    e.stopPropagation(); // Stops some browsers from redirecting.
  }

  // Don't do anything if dropping the same column we're dragging.
  if (dragSrcEl != this) {
    // Set the source column's HTML to the HTML of the column we dropped on.
    dragSrcEl.innerHTML = this.innerHTML;
    this.innerHTML = e.dataTransfer.getData('text/html');
    var x = e.dataTransfer.getData('text/html');
  }
  
  return false;
}