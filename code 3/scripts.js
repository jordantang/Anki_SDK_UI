
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

function addCode(block) {
    var type, text = "", values;
    if(block == "speed") {
        type = "<div class='column' draggable='true' id = 'AddSpeed' data-car data-speed data-accel><header>SPEED</header> <div id='data'></div></div>";
        type.data("speed", speedField.value); 
        text += type.dataset.speed + " ";
        type.getElementById('data').innerHTML = text;
        values = $('input#speedField').val();
        text += values;
        type.getElementById('data').innerHTML = text;
        $("#columns").append(type);
    }
    else if(block == "lights") {
        type = "<div class='column' draggable='true'><header>LIGHTS</header> <div id='data'></div></div>";
        $("#columns").append(type);
    }
    else if(block == "lane") {
        type = "<div class='column' draggable='true'><header>LANE</header> <div id='data'></div></div>";
        $("#columns").append(type);
    }
    else if(block == "wait") {
        type = "<div class='column' draggable='true'><header>WAIT</header> <div id='data></div></div>";
        $("#columns").append(type);        
    }
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

var cols = document.querySelectorAll('#columns .column');
[].forEach.call(cols, function(col) {
  col.addEventListener('dragstart', handleDragStart, false);
  col.addEventListener('dragenter', handleDragEnter, false);
  col.addEventListener('dragover', handleDragOver, false);
  col.addEventListener('dragleave', handleDragLeave, false);
});
    
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

var cols = document.querySelectorAll('#columns .column');
[].forEach.call(cols, function(col) {
  col.addEventListener('dragstart', handleDragStart, false);
  col.addEventListener('dragenter', handleDragEnter, false)
  col.addEventListener('dragover', handleDragOver, false);
  col.addEventListener('dragleave', handleDragLeave, false);
  col.addEventListener('drop', handleDrop, false);
  col.addEventListener('dragend', handleDragEnd, false);
});
    
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
