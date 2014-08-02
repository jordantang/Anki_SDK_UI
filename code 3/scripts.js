
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
